# gitq.py - Git Enhanced Navigation Tool with Deque and Queues (Full Version)

import os
import json
import subprocess
import argparse
from collections import deque

GITQ_DIR = ".gitq"
FORWARD_QUEUE_FILE = os.path.join(GITQ_DIR, "forward_queue.json")
BACKWARD_QUEUE_FILE = os.path.join(GITQ_DIR, "backward_queue.json")


def run_git_command(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def get_commit_list():
    log = run_git_command(["git", "log", "--pretty=format:%H"])
    return deque(log.split("\n"))


def load_queue(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return []


def save_queue(path, queue):
    with open(path, "w") as f:
        json.dump(queue, f)


def ensure_gitq_dir():
    if not os.path.exists(GITQ_DIR):
        os.makedirs(GITQ_DIR)


def smart_checkout(target_commit):
    ensure_gitq_dir()

    commits = get_commit_list()
    if target_commit not in commits:
        print(f"Error: Commit {target_commit} not found in history.")
        return

    forward_queue = load_queue(FORWARD_QUEUE_FILE)
    backward_queue = load_queue(BACKWARD_QUEUE_FILE)

    index = commits.index(target_commit)
    mid = len(commits) // 2

    if index > mid:
        # Closer to HEAD (pop from right)
        while commits[0] != target_commit:
            popped = commits.popleft()
            backward_queue.append(popped)
    else:
        # Closer to root (pop from left)
        while commits[-1] != target_commit:
            popped = commits.pop()
            forward_queue.append(popped)

    save_queue(FORWARD_QUEUE_FILE, forward_queue)
    save_queue(BACKWARD_QUEUE_FILE, backward_queue)

    run_git_command(["git", "checkout", target_commit])
    print(f"Checked out to {target_commit}")
    print(f"Forward queue: {forward_queue}")
    print(f"Backward queue: {backward_queue}")


def undo():
    backward_queue = load_queue(BACKWARD_QUEUE_FILE)
    if not backward_queue:
        print("No previous commits to undo.")
        return
    last_commit = backward_queue.pop()
    save_queue(BACKWARD_QUEUE_FILE, backward_queue)

    forward_queue = load_queue(FORWARD_QUEUE_FILE)
    forward_queue.append(last_commit)
    save_queue(FORWARD_QUEUE_FILE, forward_queue)

    run_git_command(["git", "checkout", last_commit])
    print(f"Undone to {last_commit}")


def redo():
    forward_queue = load_queue(FORWARD_QUEUE_FILE)
    if not forward_queue:
        print("No forward commits to redo.")
        return
    next_commit = forward_queue.pop()
    save_queue(FORWARD_QUEUE_FILE, forward_queue)

    backward_queue = load_queue(BACKWARD_QUEUE_FILE)
    backward_queue.append(next_commit)
    save_queue(BACKWARD_QUEUE_FILE, backward_queue)

    run_git_command(["git", "checkout", next_commit])
    print(f"Redone to {next_commit}")


def reset():
    save_queue(FORWARD_QUEUE_FILE, [])
    save_queue(BACKWARD_QUEUE_FILE, [])
    print("Git queues reset.")


def main():
    parser = argparse.ArgumentParser(description="Git Queue Navigation Tool")
    subparsers = parser.add_subparsers(dest="command")

    parser_checkout = subparsers.add_parser("checkout")
    parser_checkout.add_argument("commit", help="Commit hash to checkout")

    subparsers.add_parser("undo")
    subparsers.add_parser("redo")
    subparsers.add_parser("reset")

    args = parser.parse_args()

    if args.command == "checkout":
        smart_checkout(args.commit)
    elif args.command == "undo":
        undo()
    elif args.command == "redo":
        redo()
    elif args.command == "reset":
        reset()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
