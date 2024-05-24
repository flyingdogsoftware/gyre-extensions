/**
 * Generate a sprite using the canvas API
 * @param {number} width
 * @param {number} height
 * @param {(ctx: CanvasRenderingContext2D, w: number, h: number) => void} fn
 */
export default function createSprite(width: number, height: number, fn: (ctx: CanvasRenderingContext2D, w: number, h: number) => void): HTMLCanvasElement;
