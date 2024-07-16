/*
   Caligraphy brush
    inspired by https://openprocessing.org/sketch/793375 by BUN, CreativeCommons Attribution ShareAlike
*/
// eslint-disable-next-line no-unused-vars
class brush_Caligraphy {
    constructor() {
        this.values = {}
    }

    refresh(globalValues) {
        this.globalValues = globalValues
    }
    draw(context, point) {
        if (!this.values) return
        if (!this.vx) this.vx = 0
        if (!this.vy) this.vy = 0
        if (!this.v) this.v = 0
        if (!this.r) this.r = 0

        /*
          Draw multiple lines with different positions and thicknesses, 
          and make it look like a brush
        */
        /*
          Parameters used
            size : Brush size
            spring : Spring constant(Larger value means stronger spring)
            friction : Friction(Smaller value means, the more slippery)
            splitNum : Number of divisions from old coordinates to new coordinates
            diff : Misalignment of different lines
        */
        let mouseX = point[0]
        let mouseY = point[1]
        this.vx += ((mouseX - this.x) * this.values.spring) / 1000
        this.vy += ((mouseY - this.y) * this.values.spring) / 1000
        this.vx *= this.values.friction / 1000
        this.vy *= this.values.friction / 1000

        this.v += Math.sqrt(this.vx * this.vx + this.vy * this.vy) - this.v
        this.v *= 0.6

        this.oldR = this.r
        this.r = this.globalValues.brushSize - this.v

        for (let i = 0; i < this.values.splitNum; ++i) {
            this.oldX = this.x
            this.oldY = this.y
            this.x += this.vx / this.values.splitNum
            this.y += this.vy / this.values.splitNum
            this.oldR += (this.r - this.oldR) / this.values.splitNum
            if (this.oldR < 1) {
                this.oldR = 1
            }
            context.lineWidth = this.oldR + this.values.diff // AMEND: oldR -> oldR+diff
            let rgb = tinycolor(this.globalValues.brushColor).toRgb()
            let color = 'rgba(' + rgb.r + ',' + rgb.g + ',' + rgb.b + ',' + this.globalValues.brushOpacity + ')'
            context.strokeStyle = color
            context.beginPath()
            context.moveTo(this.x, this.y)
            context.lineTo(this.oldX, this.oldY)
            context.closePath()
            context.stroke()

            context.lineWidth = this.oldR // ADD
            context.beginPath()
            context.moveTo(this.x + this.values.diff * 2, this.y + this.values.diff * 2)
            context.lineTo(this.oldX + this.values.diff * 2, this.oldY + this.values.diff * 2) // ADD
            context.closePath()
            context.stroke()
            context.beginPath()
            context.moveTo(this.x - this.values.diff, this.y - this.values.diff)
            context.lineTo(this.oldX - this.values.diff, this.oldY - this.values.diff) // ADD
            context.closePath()
            context.stroke()
        }
    }

    start(context, point) {
        this.currentAngle = undefined
        this.latestPoint = point
        this.f = false
        this.vx = this.vy = 0
        let mouseX = point[0]
        let mouseY = point[1]
        this.x = mouseX
        this.y = mouseY
    }
    continue(context, newPoint) {
        this.draw(context, newPoint)
    }
    end() {}
}



// @ts-ignore
globalThis.brush_Caligraphy = brush_Caligraphy;

