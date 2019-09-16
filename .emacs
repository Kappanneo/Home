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
 '(cua-mode nil)
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
 '(delete-selection-mode t)
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
(global-set-key (kbd "C-z") 'undo-only)
(global-set-key (kbd "C-y") 'nil)
(global-set-key (kbd "C-S-z") 'nil)
(global-set-key (kbd "C-s") 'save-buffer)

(global-set-key (kbd "<C-mouse-4>") 'text-scale-increase)
(global-set-key (kbd "<C-mouse-5>") 'text-scale-decrease)
(global-set-key (kbd "C-+") 'text-scale-increase)
(global-set-key (kbd "C--") 'text-scale-decrease)
(global-set-key (kbd "C-0") 'text-scale-adjust)

;; file navigation
(global-set-key (kbd "M-C-f") 'find-file)
(global-set-key [C-iso-lefttab] 'switch-to-prev-buffer)
(global-set-key [C-tab] 'switch-to-next-buffer)

;; delete
(global-set-key (kbd "M-<delete>") 'delete-line)
(global-set-key (kbd "M-<backspace>") 'delete-line)
(global-set-key (kbd "C-<delete>") 'delete-word)
(global-set-key (kbd "C-<backspace>") 'backward-delete-word)

(defun delete-line ()
  (interactive)
  (beginning-of-line)
  (delete-region (point) (progn (end-of-line) (point))))

(defun delete-word ()
  (interactive)
  (if (use-region-p)
      (delete-region (region-beginning) (region-end))
    (if (looking-at "[[:blank:]]")
        (let ((p (point)))
          (re-search-forward "[^[:blank:]]" nil :no-error)
          (backward-char)
          (delete-region p (point)))
      (if (looking-at "[[:word:]]")
          (let ((p (point)))
            (re-search-forward "[^[:word:]]" nil :no-error)
            (backward-char)
            (delete-region p (point)))
        (delete-char 1)))))

(defun backward-delete-word ()
  (interactive)
  (if (use-region-p)
      (delete-region (region-beginning) (region-end))
    (if (save-excursion (backward-char) (looking-at "[[:blank:]]"))
        (let ((p (point)))
          (re-search-backward "[^[:blank:]]" nil :no-error)
          (delete-region p (point)))
      (if (save-excursion (backward-char) (looking-at "[[:word:]]"))
          (let ((p (point)))
            (re-search-backward "[^[:word:]]" nil :no-error)
            (delete-region p (point)))
        (delete-char -1)))))

;; search
(global-set-key (kbd "C-f") 'isearch-forward)
(define-key isearch-mode-map "\C-f" 'isearch-repeat-forward)
(define-key isearch-mode-map "\C-v" 'isearch-yank-pop)
(define-key isearch-mode-map [return] 'isearch-repeat-forward)
(define-key isearch-mode-map [S-return] 'isearch-repeat-backward)
(define-key isearch-mode-map [backspace] 'isearch-del-char)

(global-set-key (kbd "<mouse-3>") 'xah-mouse-click-to-search) ; right button
(global-set-key (kbd "<S-mouse-4>") 'scroll-right)
(global-set-key (kbd "<S-mouse-5>") 'scroll-left)

(defun xah-mouse-click-to-search (@click)
  "Mouse click to start `isearch-forward-symbol-at-point' (emacs 24.4) at clicked point.
URL `http://ergoemacs.org/emacs/emacs_mouse_click_highlight_word.html'
Version 2016-07-18"
  (interactive "e")
  (let ((p1 (posn-point (event-start @click))))
    (goto-char p1)
    (save-excursion (isearch-forward-symbol-at-point))))

;; replace
(global-set-key (kbd "C-r") 'query-replace)
(global-set-key (kbd "C-S-r") 'query-replace-regexp)

;; unused
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

(add-hook 'before-save-hook 'delete-trailing-whitespace)

(server-start)
