# fds-gradient-editor 🌈🖌️✨

[![Gyre SDK](https://img.shields.io/badge/Gyre%20SDK-Explore-blue?style=for-the-badge&logo=github)](https://flyingdogsoftware.github.io/gyre-sdk/)
[![Gyre Extensions](https://img.shields.io/badge/Gyre%20Extensions-Repository-blue?style=for-the-badge&logo=github)](https://github.com/flyingdogsoftware/gyre-extensions/)
[![Gyre for ComfyUI](https://img.shields.io/badge/Gyre%20for%20ComfyUI-Explore-blue?style=for-the-badge&logo=github)](https://github.com/flyingdogsoftware/gyre_for_comfyui)
[![Gyre](https://img.shields.io/badge/Gyre-Website-orange?style=for-the-badge&logo=internet-explorer)](https://gyre.ai)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/HyaNtnU5Pw)

<p align="center">
  <img src="https://gyre.ai/images/logo.png" alt="Gyre Logo" width="150px">
</p>

## Overview

The **fds-gradient-editor** is a simple gradient editor made with Svelte as a Web Component. It can be used in the Gyre form editor as an element for the Gyre user interface.

## Installation

```sh
npm i @fds-components-public/fds-gradient-editor
```

## Usage

```html
<script src="<Path>/fds-gradient-editor.js"></script>

<fds-gradient-editor value="gradient definitions"></fds-gradient-editor>
```

## Example

```html
<fds-gradient-editor value="0:255,0,0
25:255,255,255
50:0,255,0
75:0,0,255" onchange="console.log(this.value)"></fds-gradient-editor>
```

produces output:

![alt text](image.png)

So value is a list with gradient stops (0 to 100 max), a colon, and color for each line.

## Join Our Developer Community

Want to contribute or just connect with other developers working on Gyre projects? Join our developer group on Discord!

[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/HyaNtnU5Pw)

This README follows a similar format with badges, links, and an overview of the gradient editor.
