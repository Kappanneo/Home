(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["#2d3743" "#ff4242" "#74af68" "#dbdb95" "#34cae2" "#008b8b" "#00ede1" "#e1e1e0"])
 '(blink-cursor-mode nil)
 '(column-number-mode t)
 '(cua-mode t nil (cua-base))
 '(custom-enabled-themes (quote (deeper-blue)))
 '(global-linum-mode t)
 '(inhibit-startup-screen t)
 '(initial-frame-alist nil)
 '(scroll-bar-mode nil)
 '(tool-bar-mode nil)
 '(tooltip-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

(require 'package)
(add-to-list 'package-archives
             '("melpa-stable" . "http://stable.melpa.org/packages/") t)


(add-to-list 'load-path "~/.emacs.d/lisp/")

(require 'undo-tree)
(global-undo-tree-mode 1)

;(require 'xah-fly-keys)
;(xah-fly-keys-set-layout "qwerty")
;(xah-fly-keys 1)

;; sanity preservers
(global-set-key (kbd "C-x") 'xah-cut-line-or-region)
(global-set-key (kbd "C-c") 'xah-copy-line-or-region)
(global-set-key (kbd "C-v") 'yank)
(global-set-key (kbd "C-z") 'undo)
(global-set-key (kbd "C-y") 'redo)
(global-set-key (kbd "C-s") 'save-buffer)

;; personal preferences
(global-set-key (kbd "C-f") 'find-file)
(global-set-key (kbd "C-d") 'delete-other-windows)
(global-set-key (kbd "C-w") 'kill-this-buffer)
(global-set-key [C-iso-lefttab] 'switch-to-prev-buffer)
(global-set-key [C-tab] 'switch-to-next-buffer)

(global-set-key (kbd "M-f") 'search-forward-regexp)
(global-set-key (kbd "M-c") 'delete-forward-char)
(global-set-key (kbd "M-d") 'delete-backward-char)

(global-set-key (kbd "C-r") 'isearch-forward-regexp)

(prefer-coding-system 'utf-8)
