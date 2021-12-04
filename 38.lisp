(defun digits (num)
  (map 'list 
       #'(lambda (char) (read-from-string (string char)))
       (prin1-to-string num)))

(defun euler38 ()
  (loop for i from 9999 downto 1
        if (let ((digs (append (digits i) (digits (* 2 i)))))
             (equal '(1 2 3 4 5 6 7 8 9) (sort digs #'<)))
          return (list i (* 2 i))))

(print (funcall #'euler38))
