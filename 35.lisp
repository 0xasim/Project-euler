(defun digits (num)
  (map 'list 
       #'(lambda (char) (read-from-string (string char)))
       (prin1-to-string num)))

(defun digit-val (digits)
  (read-from-string (format nil "~{~D~}" digits)))

(defun seq-list (min max)
  (loop for i from min to max collect i))

(defun sieve (lst)
  (let ((primes '())
        (last (car (last lst))))
    (loop while (and lst (> last (* (car lst) (car lst))))
          do (let ((factor (car lst)))
               (setq primes (cons factor primes))
               (setq lst (remove-if
                          #'(lambda (n)
                              (= (mod n factor) 0))
                          (cdr lst)))))
    (append (reverse primes) lst)))

(defun all-primes (limit)
  (sieve (seq-list 2 limit)))

(defun generate-all-primes (limit)
  (setq all-primes (all-primes limit))
  (setq primehash (make-hash-table))
  (loop for p in all-primes
        do (setf (gethash p primehash) p)))

(defun primep (p)
  (gethash p primehash))

(defun rotate (lst)
  (append (las lst) (butlast lst)))

(defun all-digit-rotations (num)
  (let ((digits (digits num)))
    (loop for i from 1 to (length digits)
          do (setf digits (rotate digits))
          collect (digit-val digits))))

(defun all-rotatable-primes (limit)
  (generate-all-primes limit)
  (loop for p in all-primes
        if (every #'primep (all-digit-rotations p)))
          collect (p))

(defun euler35 ()
  (length (all-rotatable-primes 1000000)))
