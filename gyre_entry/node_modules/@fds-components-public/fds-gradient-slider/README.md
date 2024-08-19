# fds-gradient-slider 🎨🔧✨

[![Gyre SDK](https://img.shields.io/badge/Gyre%20SDK-Explore-blue?style=for-the-badge&logo=github)](https://flyingdogsoftware.github.io/gyre-sdk/)
[![Gyre Extensions](https://img.shields.io/badge/Gyre%20Extensions-Repository-blue?style=for-the-badge&logo=github)](https://github.com/flyingdogsoftware/gyre-extensions/)
[![Gyre for ComfyUI](https://img.shields.io/badge/Gyre%20for%20ComfyUI-Explore-blue?style=for-the-badge&logo=github)](https://github.com/flyingdogsoftware/gyre_for_comfyui)
[![Gyre](https://img.shields.io/badge/Gyre-Website-orange?style=for-the-badge&logo=internet-explorer)](https://gyre.ai)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/HyaNtnU5Pw)

<p align="center">
  <img src="https://gyre.ai/images/logo.png" alt="Gyre Logo" width="150px">
</p>

## Overview

The **fds-gradient-slider** is a slider component showing color gradients with support for one and two handles. It can be used in the Gyre form editor as an element for the Gyre user interface.

## Run it with a Test Page

```sh
npm install
npm run dev
```

## Installation as npm Package

```sh
npm i @fds-components-public/fds-gradient-slider
```

## Usage

```html
<script src="{path to js file}/fds-gradient-slider.js"></script>

<fds-gradient-slider 
    from_color="{color}" 
    to_color="{color}" 
    min="{number}" 
    max="{number}" 
    value="{values separated by semicolon}" 
    value_type="{integer/float}" 
    num_handles="{one/two}">
</fds-gradient-slider>
```

## Examples

```html
<!-- Two handles, gradient from black to red, and value range from 0 to 255 -->
<fds-gradient-slider 
    from_color="black" 
    to_color="red" 
    min="0" 
    max="255" 
    value="64;127" 
    onchange="console.log(e.detail)" 
    value_type="integer">
</fds-gradient-slider>

<!-- One handle -->
<fds-gradient-slider 
    from_color="black" 
    to_color="grey" 
    min="0" 
    max="255" 
    value="127" 
    num_handles="one" 
    onchange="console.log(e.detail)" 
    value_type="integer">
</fds-gradient-slider>

<!-- Using float values -->
<fds-gradient-slider 
    from_color="black" 
    to_color="blue" 
    min="0.0" 
    max="1.0" 
    value="0.0;0.5" 
    onchange="console.log(e.detail)" 
    value_type="float">
</fds-gradient-slider>
```

produces output:

![alt text](image.png)

## Join Our Developer Community

Want to contribute or just connect with other developers working on Gyre projects? Join our developer group on Discord!

[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/HyaNtnU5Pw)

