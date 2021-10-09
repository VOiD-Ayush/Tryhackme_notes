console.log("hii")

var variableOne = 'Linus Torvalds';

let variableTwo = 50;

const variableThree = 'Creator of the Linux Kernel';

if (5 === 10) 
{
console.log('Hello World!'); // Skips this code
} 
else if (10 === 10) 
{
console.log(variableThree); // Prints Hello World! to the console
}



const animal = 3;
switch (animal)
{
	case 1: document.write('Cow');
			break;

	case 2: document.write('Chicken');
			break;

	case 3: document.write('Monkey');
			break;

	default: document.write('Animal?');

} 			// Outputs Monkey


const func = (a, b) => {
    let nums = a * b;
    document.write('\n',nums); // Outputs 250
}

func(25, 10);

arr = [1,10,5,15,2,7,28,900,45,18,27]

for(i=0;i<11;i++)
{
	console.log(arr[i])
}
