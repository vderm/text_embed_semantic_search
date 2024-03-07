---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: Tmux
---

# Tmux Main Shortcuts
+ Got inspired by [this video](https://www.youtube.com/watch?v=DzNmUNvnB04&ab_channel=DreamsofCode) and copied his dotfile over. Just need to install Tmux TPM first.

Session > Window (tabs) > Panes (splits)

## Sessions
+ `tmux new -s mysession`
+ `tmux kill-session -t mysession`
+ `tmux kill-session -a` kill all except current
+ `<prefix> $` rename
+ `<prefix> d` detach
+ `tmux ls`
+ `<prefix> s` show all sessions
+ `tmux attach` or `tmux a` or `tmux a -t mysession`
+ `<prefix> w` session and window preview
+ `<prefix> (` `<prefix> )` move to previous/next session

## Windows
+ `<prefix> c` create window
+ `<prefix> &` close
+ `<prefix> w` window list
+ `<prefix> n` next window
+ `<prefix> 0..9` goto window 0..9
+ `<prefix> l` last

## Panes
+ `<prefix> %` split horizontally
+ `<prefix> "` split vertically
+ `<prefix> {` or `<prefix> }` move pane left/right
+ `<prefix> o` new pane
+ `<prefix> q` show numbers
+ `<prefix> z` zoom
+ `<prefix> !` convert pane to window
+ `<prefix> <arrow keys>` resize
+ `<prefix> x` close pane

## Copy Model
+ `<prefix> [` enter copy mode, `q` to quit
+ `space` start selection, `Esc` clear selection, `Enter` copy selection
+ `<prefix> ]` paste contents

## Misc
+ `<prefix> :` enter command mode