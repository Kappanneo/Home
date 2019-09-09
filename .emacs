(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["#2d3743" "#ff4242" "#74af68" "#dbdb95" "#34cae2" "#008b8b" "#00ede1" "#e1e1e0"])
 '(savehist-mode 1)
 '(blink-cursor-mode nil)
 '(column-number-mode t)
 '(cua-mode t nil (cua-base))
 '(custom-enabled-themes (quote (deeper-blue)))
 '(global-linum-mode t)
 '(inhibit-startup-screen t)
 '(initial-frame-alist nil)
 '(scroll-bar-mode nil)
 '(tool-bar-mode nil)
 '(tooltip-mode nil)
 '(indent-tabs-mode nil)
 '(tab-always-indent 'complete)
 '(pop-up-frames t)
 '(truncate-lines t))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(add-to-list 'load-path "~/.emacs.d/lisp/")

(require 'cursor-chg)
(change-cursor-mode 1)

(require 'exec-path-from-shell)
(exec-path-from-shell-initialize)
(when (memq window-system '(mac ns x))
  (exec-path-from-shell-initialize))
(exec-path-from-shell-copy-env "HISTFILE")

(require 'move-text)
(global-set-key (kbd "M-<up>") 'move-text-up)
(global-set-key (kbd "M-<down>") 'move-text-down)

(require 'subset)
(global-set-key (kbd "C-w") 'xah-close-current-buffer)
(global-set-key (kbd "C-S-t") 'xah-open-last-closed)

(require 'bash-completion)
(bash-completion-setup)

;; sanity preservers
(global-set-key (kbd "C-x") 'xah-cut-line-or-region)
(global-set-key (kbd "C-c") 'xah-copy-line-or-region)

(global-set-key (kbd "C-v") 'yank)
(global-set-key (kbd "C-z") 'undo)
(global-set-key (kbd "C-y") 'nil)
(global-set-key (kbd "C-S-z") 'nil)
(global-set-key (kbd "C-s") 'save-buffer)

;; personal preferences
(global-set-key (kbd "C-S-f") 'find-file)
(global-set-key [C-iso-lefttab] 'switch-to-prev-buffer)
(global-set-key [C-tab] 'switch-to-next-buffer)
(global-set-key (kbd "C-f") 'isearch-forward-regexp)

(global-set-key (kbd "C-0") 'nil)
(global-set-key (kbd "C-1") 'nil)
(global-set-key (kbd "C-2") 'nil)
(global-set-key (kbd "C-3") 'nil)
(global-set-key (kbd "C-4") 'nil)
(global-set-key (kbd "C-5") 'nil)
(global-set-key (kbd "C-6") 'nil)
(global-set-key (kbd "C-7") 'nil)
(global-set-key (kbd "C-8") 'nil)
(global-set-key (kbd "C-9") 'nil)

(global-set-key (kbd "C-o") 'nil)
(global-set-key (kbd "C-k") 'nil)
(global-set-key (kbd "C-l") 'nil)
(global-set-key (kbd "C-ò") 'nil)

(global-set-key (kbd "C-u") 'insert-char)
(global-set-key (kbd "C-ù") 'pop-to-mark-command)

(add-hook 'dired-mode-hook 'dired-hide-details-mode)

(global-set-key (kbd "<escape>") 'keyboard-escape-quit)
(global-set-key (kbd "<menu>") 'x-menu-bar-open)

(global-set-key (kbd "<backtab>") 'un-indent-by-removing-4-spaces)
(defun un-indent-by-removing-4-spaces ()
  "remove 4 (or less) spaces from beginning of of line"
  (interactive)
  (save-excursion
    (save-match-data
      (beginning-of-line)
      ;; get rid of tabs at beginning of line
      (when (looking-at "^\\s-+")
        (untabify (match-beginning 0) (match-end 0)))
      (when (looking-at "^ \\{1,4\\}")
        (replace-match "")))))
(put 'scroll-left 'disabled nil)

(server-start)
