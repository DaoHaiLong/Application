# Javascript

Javascript NoteBook for Beginners from CodeXplore

# Table of contents

- [Table of contents](#table-of-contents)
- [Basics](#basics)
   - Variables
   - Control Flow
   - Function
   - Array
   - Object
   - Loop
   - Type Coercion
- [Document Object Model](#document-object-model)
- [FAQ](#faq)



# Basics 

1. **Variables: var, let, const**
    - **var:** the scope is quite similar to let; but a little bit confusing, so not recommend to use
    - **let (ES6):** the scope is only within {}
    - **const (ES6):** cannot be re-assigned the variable; use to assign for variables which we will not re- like: Function; Object<br>
    cannot be re-assigned means: const a = {}; a = 1; => Error <br>
    const a = function() {}; a is a function; const a: to make sure nobody assign something else to function a
	```Javascript
	var firstName = "Code";
	var lastName = "Xplore";

	let experience = 100;

	const a = function() {
		console.log("Hello World");
	};
	```
2. **Control Flow**<br>
    - **Ternary Operator**
    ```Javascript
    condition ? expr1: expr2;
    ```
    - **Switch**
    ```Javascript
	switch(expression) {
	  case x:
	    // code block
	    break;
	  case y:
	    // code block
	    break;
	  default:
	    // code block
	}
    ```
3. **Functions**
    - **Function Expression**
    ```Javascript
    //Function Expression: Anonymouse Function, meaning function has no name
    //Only able to access via variable "sayBye"

    var sayBye = function () {
      console.log("Bye");
    };
    sayBye()
    ```
    - **Arrow Function**
    ```Javascript

    const add = (a,b) => {
    	return a + b;;
    };
    ```
    
    - **Currying:** process of converting the function taking multiple inputs to the function that can access the input one by one at the time
    ```Javascript
	//Currying
	const multiply = (a, b) => a * b;
	const curriedMultiply = (a) => (b) => a * b;
	curriedMultiply(3)(4);
	
	//curriedMultiply(5) = (b) => 5 * b
	const multiplyBy5 = curriedMultiply(5);
    ```
4. **String** 
    - **How to  a string**
    ```JavaScript
    	var str1 = 'The morning is upon us.';
	var str2 = str1.slice(4, -2);
    
    ```

   - **How to sort a string**
   
   ```JavaScript
    //need to .split("") the string to sort the array
    //JS dont have .sort() for string, only for array

    //need to .join("") after sorted to compare to string
    //Since === cannot compare 2 arrays
    var sortedStringOne = stringOne.split("").sort().join("");
   ```
5. **Array**
    ```Javascript
	const array = [1, 2, 10, 16];
    ```

   - **forEach**: only loop over something (suggest to use map instead of forEach)
    ```Javascript
	const double = [];
	array.forEach((num) => {
	  double.push(num * 2);
	});
    ```
    - **map**: loop over something & return a new array (diff from forEach)<br>
    Note: Need to **return in map**
    ```Javascript
	const mapArray = array.map((num) => {
	  return num * 2; //Need to return in Map
	});
    ```
    - **filter**: loop, filter & return a new array <br>
    Note: Need to **return in filter**
    ```Javascript
	const filterArray = array.filter((num) => {
	  return num > 5;
	});
    ```

6. **Object**

```JavaScript
const user = {
  name: "CodeXplore",
  age: 25,
  //Array inside Object
  hobby: ["Footbal", "Swimming"],
  isMarried: false,
  //Method inside Object
  shout: function () {
    console.log("TD, I love you");
  },
};
```
**ES6 Feature for Objects:**
```JavaScript
//Object Destruction:

const { name, hobby } = user

//Object Construction:

const a = "Simon";
const b = true;
const c = {};
const obj = {a,b,c}
```
6. **Loop: for, while, forEach**
     - **for**
     ```Javascript
	for (let index of array) {
   		const mask = 1 << index;
	}
    ```
     
     - **forEach**
     ```Javascript
      todos.forEach(function (todo, index) {
          todo = todo + " at index: " + index;
          console.log(todo);
      });
    ```
7. **Type Coercion**:
     ```Javascript
	//Type coercion: since JS is dynamic type
	console.log(1 == "1"); //returns True as JS convert '1' to 1 = Type coercion
	console.log(1 === "1"); //return False to prevent Type Coercion
    ```

[(Back to top)](#table-of-contents)

# Document Object Model 
1. **DOM Selectors**:

```JavaScript
document.getElementsByTagName("h2")
document.getElementsByClassName("second")
document.getElementById("first")

document.querySelector("h1") //Only select First item
document.querySelectorAll("h1")
```
   **Parent and Children Selector**

```JavaScript
document.querySelector("li").parentElement
document.querySelector("ul").children
```

2. **DOM Change innerHTML textContent**:
```JavaScript
var h1Tag = document.querySelector("h1")
h1Tag.innterHTML = "Welcome to CodeXplore"

var css = document.querySelector("h3");
css.textContent = body.style.background + ";";

```

3. **DOM Event Listener**
```JavaScript
var button = document.getElementsByTagName("button")[0];

//Method 1:
button.addEventListener("click", function () {
	console.log("CLICK !!!!");
});
//Method 2:
//addListAfterClick = Callback function (without added ()):
//the function now automatically gets run (auto-gets added the ()) every time the click happens. So we are passing a reference to the function without running it (without added ()).
button.addEventListener("click", addListAfterClick);

//Method 3:
button.onclick = addListAfterClick;
```

**Method 4: Add Event Listener directly in HTML Tag**<br>
Using: onclick, onsubmit, oninput in HTML tags
```HTML
<button onclick="myFunction()">Click me</button>
<input oninput="setGradient()" class="color1" type="color" name="color1" value="#00ff00">

```

**Method 5: Add Event Listener directly in JSX - React**<br>

```JSX
const ImageLinkForm = () => {
      return (
	   <button onClick={onButtonSubmit}>
		    Detect
	   </button>
	   
	   //If you want to pass the input, for ex: "home", to Event Handler functionm => use Arrow Function to prevent default auto-trigger with () 
	   <input onClick={() => onRouteChange("home")} />
	   
	)
	
```
      

[(Back to top)](#table-of-contents)

# FAQ
1. **Why JQuery is not popular nowadays**?<br>
    JQuery has 1 issue, it make the code imperative, you have to tell the program what to do 1-by-1. When website get scaled, jQuery becomes a issue as 1 action depends on other actions, and depends on another action, more bugs. 


