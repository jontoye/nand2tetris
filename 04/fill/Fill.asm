// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.


(LOOP) 
	@SCREEN
	D=A
	@address
	M=D					// address = SCREEN (resets address)

	@8192
	D=A
	@count
	M=D					// count = 8192 (resets count)

	@KBD
	D=M
	@WHITE
	D;JEQ				// if RAM[KBD] = 0 goto WHITE
	@BLACK
	D;JNE				// if RAM[KBD] != 0 goto BLACK

(WHITE)
	@count
	D=M
	@LOOP
	D;JEQ				// if count = 0 goto LOOP
	@address
	A=M
	M=0					// sets 16 pixels at address to white 
	@address
	M=M+1				// address = address + 1
	@count
	M=M-1				// count++
	@WHITE
	0;JMP				// goto WHITE

(BLACK)
	@count
	D=M
	@LOOP
	D;JEQ				// if count = 0 goto LOOP
	@address
	A=M
	M=-1				// sets 16 pixels at address to black
	@address
	M=M+1				// address = address + 1
	@count
	M=M-1				// count++
	@BLACK
	0;JMP				// goto BLACK