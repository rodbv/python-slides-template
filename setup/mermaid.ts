import { defineMermaidSetup } from '@slidev/types'

// Slidev draws each diagram inside a shadow root, so styles/index.css never reaches it.
// themeCSS goes inside the SVG, and the brand variables inherit through the shadow root.
const brandCSS = `
  .node rect, .node polygon, .node path { fill: var(--card) !important; stroke: var(--text) !important; stroke-width: 2px !important; }
  .nodeLabel, .edgeLabel, .edgeLabel p { color: var(--text) !important; fill: var(--text) !important; font-family: var(--font-sans) !important; }
  .edgeLabel, .labelBkg, .edgeLabel p { background: var(--bg) !important; background-color: var(--bg) !important; }
  .edgeLabel rect { fill: var(--bg) !important; opacity: 1 !important; }
  .flowchart-link { stroke: var(--text) !important; stroke-width: 2px !important; }
  marker path { fill: var(--text) !important; stroke: var(--text) !important; }
  .background { fill: transparent !important; }
  text { fill: var(--text) !important; font-family: var(--font-sans) !important; }
  .plot rect { fill: var(--fill) !important; stroke: var(--fill-edge) !important; stroke-width: 3px !important; }
  .left-axis path, .bottom-axis path { stroke: var(--text) !important; }
`

export default defineMermaidSetup(() => ({
  themeCSS: brandCSS,
  xyChart: {
    width: 820,
    height: 300,
    xAxis: { labelFontSize: 26, titleFontSize: 24 },
    yAxis: { labelFontSize: 22, titleFontSize: 24 },
  },
}))
