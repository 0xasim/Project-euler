start:
      mov   numa,3

   @@:
      mov   ecx,perim
      sub   ecx,numa
      mov   eax,ecx
      shl   ecx,1
      sub   eax,numa
      mul   perim
      div   ecx
      or    edx,edx
      .if   ZERO?
            inc   numof
      .else
            .if   eax <= numa
                  jmp   @F
            .endif
      .endif
      inc   numa
      jmp   @B

   @@:
      mov   eax,numof
      .if   eax > bestnum
            mov   bestnum,eax
            push  perim
            pop   bestp
      .endif
      mov   eax,perim
      add   eax,2
      cmp   eax,999
      ja    endcalc
      mov   perim,eax

      mov   numof,0
      jmp   start

 endcalc:
     ;display result (bestp)

