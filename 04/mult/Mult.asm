// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// PSEUDO-CODE:
// sum = 0
// n = R1
// i = 0

// LOOP:
// 	if i = n goto PROD
// 	sum = sum + R0
// 	i = i + 1
// 	goto LOOP

// PROD:
// 	R2 = sum

// END:
// 	goto END


	@sum
	M=0				// sum = 0

	@R1
	D=M
	@n
	M=D				// n = RAM[1]

	@i
	M=0 			// i = 0

(LOOP)
	@i
	D=M
	@n
	D=D-M
	@PROD
	D;JEQ			// if i = n goto PROD

	@R0
	D=M
	@sum
	M=M+D			// sum = sum + R0

	@i
	M=M+1			// i++		
	@LOOP
	0;JMP

(PROD)
	@sum
	D=M
	@R2
	M=D				// RAM[2] = sum
	@END
	0;JMP

(END)
	@END
	0;JMP			// end program	




