---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: Git
---

# Git Cheat Sheet
Git is a version control framework allowing multiple people to work on a single library and/or to branch off from a certain location in the project version.

Basic methodology is to make some changes to a file, stage that file (`git add`), commit the changes with a message (`git commit -m`), and finally push that file to the git server (known as origin, `git push origin <branch>`). You can also pull changes others made from the server (`git pull origin <branch>`). If you made a nice feature, you should definitely merge those with the master branch! (`(master) git merge <feature>`).

# Tutorial videos
+ https://www.youtube.com/watch?v=duqBHik7nRo

# Add files
`git add <filename>`

# Check status
`git status`

Run this to see what is staged to be committed!

#  Commit
`git commit -m "blablabla"` : commit changes, "-m" option to write comment inline
`git commit -a -m "blablabla"` : commit all tracked files

# Diff
`git diff --staged`: shows differences of staged file vs previous version

# Tracked files
`git ls-tree -r master --name-only`: print list of files that are tracked
`git ls-tree`: does the same ^

# Making a branch
`git checkout -b newBranch`

# Merging a branch
`git commit` to go forward
`git checkout master` go back to master
`git commit` again
`git merge` to merge it back

or

on `checkout newBranch`
`git rebase`
then `checkout master`
and `git commit` to bring it to date

# Delete a branch
locally:
`git branch -d "branchname"`

origin:
`git push origin --delete "branchname"`

# Moving the head
`git checkout hash`
`git checkout HEAD^` moves up a commit/node

`git checkout HEAD~4` goes up 4

`git branch -f master HEAD~4` moves master branch up by 4 relative to the head
(master usually)

# Reversing a change
`git reset HEAD`: local to HEAD
`git reset <hash>`: local to hash
`git revert HEAD pushed` (copies old commit forward past commit to erase)

# Moving work around
`git cherry-pick <commit1> <commit2> ...` puts these commit right under the HEAD

`git rebase -i` makes it interactive (opens vim)

# Locally stacked commits
Useful when troubleshooting a bug, add print statements and checks, find the
bug, fix the bug, but you don't want all the checks, just the fix

use these to copy only what is needed
`git rebase -i`
`git cherry-pick`

go back to master, `git cherry-pick hash` of the change you want

# Juggling commits
`git commit --amend`
...
check tutorial again

# git describe
`git describe <ref>`

# remote work
origin is the name of the main copy (on the cloud) -> origin/master
`git checkout origin master`
`git commit` -> origin doesn't update because that one is synced with the remote server

# git fetch: move stuff around in the remote copy
`git fetch` gets the commits from the remote server and adds it to the local one,
commits local to move it forward

`git fetch` does not update the files, it downloads the changes and has them ready
but they are not applied yet

`git pull` = `git fetch` + `git merge` (or `rebase`, `cherry-pick`)

# git don't merge: rebase!
`git pull origin master -r`

# check difference between branches
`git diff 25f27bd cc02ab8 > newbug.patch`

# Draw the git tree
`git log --oneline --decorate --all --graph`

use that in your bash file!
```bash
alias glo='git log --oneline --decorate --all --graph'
```

# Difference between rebase and merge
`rebase` will move the whole branch up as to stack the commits relative to the updated master

`merge` will simply look at the differences between the feature branch and the updated master; it will not move the whole branch up

From: https://stackoverflow.com/questions/3876977/update-git-branches-from-master

People like this approach because it retains a linear history in all branches. However, this linear history is a lie, and you should be aware that it is. Consider this commit graph:

```
A --- B --- C --- D <-- master
 \
  \-- E --- F --- G <-- b1
```
The merge results in the true history:
```
A --- B --- C --- D <-- master
 \                 \
  \-- E --- F --- G +-- H <-- b1
```
The rebase, however, gives you this history:
```
A --- B --- C --- D <-- master
                   \
                    \-- E' --- F' --- G' <-- b1
```
The point is, that the commits E', F', and G' never truly existed, and have likely never been tested. They may not even compile. It is actually quite easy to create nonsensical commits via a rebase, especially when the changes in master are important to the development in b1.