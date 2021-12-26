	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 0
	.globl	__Z7isprimei                    ; -- Begin function _Z7isprimei
	.p2align	2
__Z7isprimei:                           ; @_Z7isprimei
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32                     ; =32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16                    ; =16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	str	w0, [sp, #8]
	ldr	w8, [sp, #8]
	subs	w8, w8, #1                      ; =1
	b.gt	LBB0_2
; %bb.1:
	mov	w8, #0
	and	w8, w8, #0x1
	sturb	w8, [x29, #-1]
	b	LBB0_9
LBB0_2:
	mov	w8, #2
	str	w8, [sp, #4]
LBB0_3:                                 ; =>This Inner Loop Header: Depth=1
	ldr	w8, [sp, #4]
	str	w8, [sp]                        ; 4-byte Folded Spill
	ldr	w0, [sp, #8]
	bl	__ZL4sqrtIiENSt3__19enable_ifIXsr3std11is_integralIT_EE5valueEdE4typeES2_
	ldr	w8, [sp]                        ; 4-byte Folded Reload
	fmov	d1, #1.00000000
	fadd	d0, d0, d1
	fcvtzs	w9, d0
	subs	w8, w8, w9
	b.gt	LBB0_8
; %bb.4:                                ;   in Loop: Header=BB0_3 Depth=1
	ldr	w8, [sp, #8]
	ldr	w10, [sp, #4]
	sdiv	w9, w8, w10
	mul	w9, w9, w10
	subs	w8, w8, w9
	cbnz	w8, LBB0_6
; %bb.5:
	mov	w8, #0
	and	w8, w8, #0x1
	sturb	w8, [x29, #-1]
	b	LBB0_9
LBB0_6:                                 ;   in Loop: Header=BB0_3 Depth=1
; %bb.7:                                ;   in Loop: Header=BB0_3 Depth=1
	ldr	w8, [sp, #4]
	add	w8, w8, #1                      ; =1
	str	w8, [sp, #4]
	b	LBB0_3
LBB0_8:
	mov	w8, #1
	and	w8, w8, #0x1
	sturb	w8, [x29, #-1]
LBB0_9:
	ldurb	w8, [x29, #-1]
	and	w0, w8, #0x1
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32                     ; =32
	ret
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function _ZL4sqrtIiENSt3__19enable_ifIXsr3std11is_integralIT_EE5valueEdE4typeES2_
__ZL4sqrtIiENSt3__19enable_ifIXsr3std11is_integralIT_EE5valueEdE4typeES2_: ; @_ZL4sqrtIiENSt3__19enable_ifIXsr3std11is_integralIT_EE5valueEdE4typeES2_
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #16                     ; =16
	.cfi_def_cfa_offset 16
	str	w0, [sp, #12]
	ldr	s1, [sp, #12]
                                        ; implicit-def: $d0
	mov.16b	v0, v1
	sshll.2d	v0, v0, #0
                                        ; kill: def $d0 killed $d0 killed $q0
	scvtf	d0, d0
	fsqrt	d0, d0
	add	sp, sp, #16                     ; =16
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3                               ; -- Begin function _Z9falseConji
lCPI2_0:
	.quad	0x3ee4f8b588e368f1              ; double 1.0000000000000001E-5
	.section	__TEXT,__text,regular,pure_instructions
	.globl	__Z9falseConji
	.p2align	2
__Z9falseConji:                         ; @_Z9falseConji
	.cfi_startproc
; %bb.0:
	stp	x28, x27, [sp, #-32]!           ; 16-byte Folded Spill
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16                    ; =16
	mov	w9, #6048
	adrp	x16, ___chkstk_darwin@GOTPAGE
	ldr	x16, [x16, ___chkstk_darwin@GOTPAGEOFF]
	blr	x16
	sub	sp, sp, #1, lsl #12             ; =4096
	sub	sp, sp, #1952                   ; =1952
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w27, -24
	.cfi_offset w28, -32
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	stur	x8, [x29, #-24]
	str	w0, [sp, #36]
	mov	w8, #3
	str	w8, [sp, #32]
	str	wzr, [sp, #28]
LBB2_1:                                 ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB2_5 Depth 2
	ldr	w8, [sp, #32]
	ldr	w9, [sp, #36]
	subs	w8, w8, w9
	b.ge	LBB2_15
; %bb.2:                                ;   in Loop: Header=BB2_1 Depth=1
	ldr	w0, [sp, #32]
	bl	__Z7isprimei
	tbz	w0, #0, LBB2_4
; %bb.3:                                ;   in Loop: Header=BB2_1 Depth=1
	ldr	w8, [sp, #32]
	ldrsw	x10, [sp, #28]
	mov	x9, x10
	add	w9, w9, #1                      ; =1
	str	w9, [sp, #28]
	add	x9, sp, #40                     ; =40
	str	w8, [x9, x10, lsl #2]
	b	LBB2_11
LBB2_4:                                 ;   in Loop: Header=BB2_1 Depth=1
	str	wzr, [sp, #24]
LBB2_5:                                 ;   Parent Loop BB2_1 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [sp, #24]
	ldr	w9, [sp, #28]
	subs	w8, w8, w9
	b.ge	LBB2_10
; %bb.6:                                ;   in Loop: Header=BB2_5 Depth=2
	ldr	w8, [sp, #32]
	ldrsw	x10, [sp, #24]
	add	x9, sp, #40                     ; =40
	ldr	w9, [x9, x10, lsl #2]
	subs	w8, w8, w9
	mov	w9, #2
	sdiv	w0, w8, w9
	bl	__ZL4sqrtIiENSt3__19enable_ifIXsr3std11is_integralIT_EE5valueEdE4typeES2_
	str	d0, [sp, #16]
	ldr	d0, [sp, #16]
	ldr	d1, [sp, #16]
	fcvtzs	w8, d1
	scvtf	d1, w8
	fsub	d0, d0, d1
	adrp	x8, lCPI2_0@PAGE
	ldr	d1, [x8, lCPI2_0@PAGEOFF]
	fcmp	d0, d1
	b.pl	LBB2_8
; %bb.7:                                ;   in Loop: Header=BB2_1 Depth=1
	b	LBB2_10
LBB2_8:                                 ;   in Loop: Header=BB2_5 Depth=2
; %bb.9:                                ;   in Loop: Header=BB2_5 Depth=2
	ldr	w8, [sp, #24]
	add	w8, w8, #1                      ; =1
	str	w8, [sp, #24]
	b	LBB2_5
LBB2_10:                                ;   in Loop: Header=BB2_1 Depth=1
LBB2_11:                                ;   in Loop: Header=BB2_1 Depth=1
	ldr	w8, [sp, #24]
	ldr	w9, [sp, #28]
	subs	w8, w8, w9
	b.ne	LBB2_13
; %bb.12:
	b	LBB2_15
LBB2_13:                                ;   in Loop: Header=BB2_1 Depth=1
; %bb.14:                               ;   in Loop: Header=BB2_1 Depth=1
	ldr	w8, [sp, #32]
	add	w8, w8, #2                      ; =2
	str	w8, [sp, #32]
	b	LBB2_1
LBB2_15:
	ldr	w8, [sp, #32]
	str	w8, [sp, #12]                   ; 4-byte Folded Spill
	adrp	x8, ___stack_chk_guard@GOTPAGE
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
	ldr	x8, [x8]
	ldur	x9, [x29, #-24]
	subs	x8, x8, x9
	b.ne	LBB2_17
; %bb.16:
	ldr	w0, [sp, #12]                   ; 4-byte Folded Reload
	add	sp, sp, #1, lsl #12             ; =4096
	add	sp, sp, #1952                   ; =1952
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #32             ; 16-byte Folded Reload
	ret
LBB2_17:
	bl	___stack_chk_fail
	.cfi_endproc
                                        ; -- End function
	.globl	_main                           ; -- Begin function main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32                     ; =32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16                    ; =16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	mov	w0, #10
	mov	w1, #4
	bl	__ZL3powIiiENSt3__19_MetaBaseIXaasr3std13is_arithmeticIT_EE5valuesr3std13is_arithmeticIT0_EE5valueEE13_EnableIfImplINS0_9__promoteIS2_S3_vEEE4typeES2_S3_
	fcvtzs	w0, d0
	bl	__Z9falseConji
	stur	w0, [x29, #-4]
	ldur	w9, [x29, #-4]
                                        ; implicit-def: $x8
	mov	x8, x9
	adrp	x0, l_.str@PAGE
	add	x0, x0, l_.str@PAGEOFF
	mov	x9, sp
	str	x8, [x9]
	bl	_printf
	mov	w0, #0
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32                     ; =32
	ret
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function _ZL3powIiiENSt3__19_MetaBaseIXaasr3std13is_arithmeticIT_EE5valuesr3std13is_arithmeticIT0_EE5valueEE13_EnableIfImplINS0_9__promoteIS2_S3_vEEE4typeES2_S3_
__ZL3powIiiENSt3__19_MetaBaseIXaasr3std13is_arithmeticIT_EE5valuesr3std13is_arithmeticIT0_EE5valueEE13_EnableIfImplINS0_9__promoteIS2_S3_vEEE4typeES2_S3_: ; @_ZL3powIiiENSt3__19_MetaBaseIXaasr3std13is_arithmeticIT_EE5valuesr3std13is_arithmeticIT0_EE5valueEE13_EnableIfImplINS0_9__promoteIS2_S3_vEEE4typeES2_S3_
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #32                     ; =32
	stp	x29, x30, [sp, #16]             ; 16-byte Folded Spill
	add	x29, sp, #16                    ; =16
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	stur	w0, [x29, #-4]
	str	w1, [sp, #8]
	ldur	s1, [x29, #-4]
                                        ; implicit-def: $d0
	mov.16b	v0, v1
	sshll.2d	v0, v0, #0
                                        ; kill: def $d0 killed $d0 killed $q0
	scvtf	d0, d0
	ldr	s2, [sp, #8]
                                        ; implicit-def: $d1
	mov.16b	v1, v2
	sshll.2d	v1, v1, #0
                                        ; kill: def $d1 killed $d1 killed $q1
	scvtf	d1, d1
	bl	_pow
	ldp	x29, x30, [sp, #16]             ; 16-byte Folded Reload
	add	sp, sp, #32                     ; =32
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"%d\n"

.subsections_via_symbols
