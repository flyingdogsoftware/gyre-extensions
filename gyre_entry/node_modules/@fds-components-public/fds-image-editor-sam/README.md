# fds-image-editor-sam 🔧🖼️✨

[![Gyre SDK](https://img.shields.io/badge/Gyre%20SDK-Explore-blue?style=for-the-badge&logo=github)](https://flyingdogsoftware.github.io/gyre-sdk/)
[![Gyre Extensions](https://img.shields.io/badge/Gyre%20Extensions-Repository-blue?style=for-the-badge&logo=github)](https://github.com/flyingdogsoftware/gyre-extensions/)
[![Gyre for ComfyUI](https://img.shields.io/badge/Gyre%20for%20ComfyUI-Explore-blue?style=for-the-badge&logo=github)](https://github.com/flyingdogsoftware/gyre_for_comfyui)
[![Gyre](https://img.shields.io/badge/Gyre-Website-orange?style=for-the-badge&logo=internet-explorer)](https://gyre.ai)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/HyaNtnU5Pw)

<p align="center">
  <img src="https://gyre.ai/images/logo.png" alt="Gyre Logo" width="150px">
</p>

## Overview

The **fds-image-editor-sam** is a SAM Tools Plugin for the Gyre application.

## Update

Now support for new SDK V 1.1 creating linked object layer mask.

## Installation

```sh
npm i @fds-components-public/fds-image-editor-sam
```

Check your ComfyUI server URL and change it in index.html

## Usage in Test Environment

```sh
npm run dev
```

Navigate to: [http://localhost:4010](http://localhost:4010)

### Props

| Prop name  | Kind         | Reactive | Type            | Default value | Description                                   |
| :--------- | :----------- | :------- | :-------------- | :------------ | :-------------------------------------------- |
| tool_layer | <code>let</code> | No      | <code>object</code> | <code>{}</code> | tool layer with private and public information |
| refresh    | <code>function</code> | No      | <code>() => any</code> | <code></code> | Refresh the component by main application      |

### Slots

None.

### Events

None.

## Join Our Developer Community

Want to contribute or just connect with other developers working on Gyre projects? Join our developer group on Discord!

[![Discord](https://img.shields.io/badge/Discord-Join%20Us-7289DA?style=for-the-badge&logo=discord)](https://discord.gg/HyaNtnU5Pw)

 

 
