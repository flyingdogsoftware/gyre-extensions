# fds-gradient-editor

Simple gradient editor made with Svelte as web component so it can be used in Gyre form editor as an element for the Gyre user interface.

## Installation
npm i ??? /fds-gradient-editor

## Usage 
``` html
<script src="fds-gradient-editor.js"></script>

<fds-gradient-editor value="gradient definitions"></fds-gradient-editor>

```

## Example
``` html
        <fds-gradient-editor value="0:255,0,0
        25:255,255,255
        50:0,255,0
        75:0,0,255" onchange="console.log(this.value)"></fds-gradient-editor>

```

produces output


 ![alt text](image.png)

 
So value is a list with gradient stops (0 to 100 max) a colon and color for each line.
