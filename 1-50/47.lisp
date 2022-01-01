(defun prime-factor (n)
  (when (> n 1)
    (let ((limit (1+ (isqrt n))))
      (do ((i 2 (1+ i))) ((> i limit) (list n))
        (when (zerop (mod n i))
          (return-from prime-factor
            (cons i (prime-factor (/ n i)))))))))

(defun euler47 (&optional (consec 4) (n 645))
  (if (= consec
         (length (remove-duplicates (prime-factor n)))
         (length (remove-duplicates (prime-factor (+ n 1))))
         (length (remove-duplicates (prime-factor (+ n 2))))
         (length (remove-duplicates (prime-factor (+ n 3)))))
      n
      (euler47 consec (1+ n))))
(time (print (euler47)))
