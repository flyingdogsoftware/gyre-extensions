# Gyre Extensions

Welcome to the Gyre Extensions repository! Here, you'll find several examples of extension systems compatible with the Gyre middleware.

## Featured Extensions

- **Gradient-Editor**: A user interface component for editing color gradients.
- **Gradient-Slider**: A slider component that supports two handles. This slider is capable of splitting the value into multiple ComfyUI values for each handle (left and right).

## How It Works

The Gyre middleware scans all other extension folders for a subfolder named `gyre_entry`. Installing a Gyre extension follows the same process as any other ComfyUI extension, whether through the Manager, `git clone`, or unzipping. These can be added to existing ComfyUI extensions.

### Supported Extension Types

- **UI Elements**: These will appear in the "Add Element" menu of the form editor in the middleware.
- **Custom Layer Types**: Capable of hosting complex applications. Our internal 3D or Pose layers use this type of extension.
- **Custom Brushes**
- **Other Plugins**

Currently, UI elements are fully supported, with custom layers and brushes expected to be supported soon, as they utilize a similar mechanism.

The main Gyre application loads these extensions through an initialization script from the ComfyUI server, which calls each extension's initialization scripts. Thus, the ComfyUI installation and extension mechanism are applicable, even though they are hosted on different servers.

## Setting Up Your Own Extension

1. Create your folder under `custom_nodes` like any other ComfyUI extension.
2. Add a subfolder `gyre_entry` and include a JavaScript file named `gyre_init.js`. Load your extensions through this file.
3. Define custom elements with their own tags using the Shadow DOM, ensuring they are isolated from the main application. Use a unique prefix to avoid conflicts (e.g., "yourname-yourcompany-gradient-slider" instead of "gradient-slider").
4. Include files like `gyre_ui_components.json`, `layers_components.json`, or `brushes.json` in the `gyre_entry` folder.
5. Install node packages necessary for your custom tags.

### Configuration of UI elements (`gyre_ui_components.json`)

Check out our example that provides two custom UI elements: [Insert URL here]

This file should define:
- The tag name.
- A descriptive name for the element.
- A list of parameters for the tag, with inputs in the form editor requiring "name", "value", and "label".
- Parameters may support inputs of types "text" or "textarea".
- Attributes like `split_value_num` and `split_value_type` allow splitting the "value" parameter into multiple fields.

#### Example

```html
<fds-gradient-slider name="gradient" value="0;1.0"></fds-gradient-slider>
```

Using split_value_num=2 and split_value_type=number, the above example will provide:

- A field "gradient" with the value string "0;1.0".
- Field "gradient_0" with the float value 0.
- Field "gradient_1" with the float value 1.0.
- These fields are utilized in Gyre mappings.


Feel free to adjust the example link and any specifics to better match your actual content.

#### Environment 

In globalThis.gyre an extension can have access to a global extension API:

- `loadScript` method for loading scripts
- `paletteValues` access to UI values of the tools (e.g. inpainting brush size).  
- `currentLayer` for access to the selected layer. 
- `layers` layer data structure (can have groups/sub-folders)
- `formElements` form elements of open form including current values
- `workflowId` unique internal ID of the current workflow

