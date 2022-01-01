(defun generate-all-primes (limit)
  (setq all-primes (all-primes limit))
  (defglobal primehash (make-hash-table))
  (loop for p in all-primes
        do (setf (gethash p primehash) p)))

(defun primep (p)
  (gethash p primehash))

(defun all-odd-composites (limit)
  (remove-if #'(lambda (k) (gethash k primehash))
             (remove-if #'evenp
                        (seq-list 3 limit))))

(defun goldbach-decompose (n)
  (loop for s from 1 to (isqrt n)
        as p = (- n (* 2 s s))
        if (primep p)
           return (list p s)))

(defun euler46 ()
  (generate-all-primes 100000)
  (car (remove-if #'goldbach-decompose (all-odd-composites 100000))))
