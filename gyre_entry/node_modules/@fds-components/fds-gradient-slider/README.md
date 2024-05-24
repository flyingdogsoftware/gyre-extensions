# fds-gradient-slider

Slider component showing color gradients with support for one and two handles. It can be used in Gyre form editor as an element for the Gyre user interface.

## Run it with a test page
``` 
npm install
npm run dev
```

## Installation as npm package
``` 
npm i @fds-components/fds-gradient-slider
```

## Usage 
``` html
    <script src="{path to js file}/fds-gradient-slider.js"></script>
    two handles, gradient from black to red and value range from 0 to 255:
    <fds-gradient-slider 
    from_color="{color}" to_color="{color}"
    min="{number}" max="{number}" 
    value="{values separated by semicolon}" 
    value_type="{integer/float}"
    num_handles="{one/two}"
    ></fds-gradient-slider>
```

## Examples
``` html

    two handles, gradient from black to red and value range from 0 to 255:
    <fds-gradient-slider from_color="black" to_color="red" min="0" max="255" value="64;127" onchange="console.log(e.detail)" value_type="integer"></fds-gradient-slider>
    one handle:
    <fds-gradient-slider from_color="black" to_color="grey" min="0" max="255" value="127" num_handles="one" onchange="console.log(e.detail)" value_type="integer"></fds-gradient-slider>
    using float values:
    <fds-gradient-slider from_color="black" to_color="blue" min="0.0" max="1.0" value="0.0;0.5" onchange="console.log(e.detail)" value_type="float"></fds-gradient-slider>

```


produces output


![alt text](image.png)
 

 
