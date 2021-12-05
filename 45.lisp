
(defun fill-triangle-hash (lim figure-hash)
  (loop for i from 1 to lim
        do (let ((tri (* i (1+ i) 1/2)))
             (incf (gethash tri figure-hash 0)))))

(defun fill-pentagon-hash (lim figure-hash)
  (loop for i from 1 to lim
        do (let ((tri (* i (1- (* 3 i)) 1/2)))
             (incf (gethash tri figure-hash 0)))))

(defun fill-hexagon-hash (lim figure-hash)
  (loop for i from 1 to lim
        do (let ((tri (* i (1- (* 2 i)))))
             (incf (gethash tri figure-hash 0)))))

(defglobal figure-hash (make-hash-table))
(defun euler29 ()
  (let ((limit 100000))
    (fill-triangle-hash limit figure-hash)
    (fill-pentagon-hash limit figure-hash)
    (fill-hexagon-hash limit figure-hash))
  (loop for key being each hash-key of figure-hash
        if (>= (gethash key figure-hash) 3)
          collect key)
  (print figure-hash)
  (maphash #'(lambda (k v) (format t "~a => ~a~%" k v)) figure-hash))

(euler29)
