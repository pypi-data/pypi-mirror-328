import { brush } from "https://esm.sh/d3-brush@3";
import { select, selectAll } from "https://esm.sh/d3-selection@3";
import RBush from 'https://cdn.jsdelivr.net/npm/rbush/+esm';

class MyRBush extends RBush {
    toBBox(node) { return { id: node.id, minX: node.cx, minY: node.cy, maxX: node.cx, maxY: node.cy }; }
    compareMinX(a, b) { return a.cx - b.cx; }
    compareMinY(a, b) { return a.cy - b.cy; }
}

let tree;
let svg_g;

const create_rtree = (data) => {
    tree = new MyRBush();
    tree.load(data);
    return tree;
}

function render({ model, el }) {
    let svg_string = model.get("svg");
    let input_svg;

    // Initialize SVG structure ONCE
    if (!svg_g) {
        let parser = new DOMParser();
        let svg_doc = parser.parseFromString(svg_string, "image/svg+xml");
        input_svg = svg_doc.documentElement;

        // Use D3 to create the SVG element within the widget
        let svg = select(el).append("svg")
            .attr("width", input_svg.getAttribute("width"))
            .attr("height", input_svg.getAttribute("height"));

        svg_g = svg.append("g"); // Add a group for the SVG content
        svg_g.html(svg_string); // Set the SVG content using the string.

    } else {
        // Update SVG content if the string changes.
        let current_svg = svg_g.html();
        if(current_svg != svg_string) {
            svg_g.html(svg_string);
        }
    }

    // let svg = model.get("svg");
    // el.innerHTML = svg;

    // let parser = new DOMParser();
    // let svg_doc = parser.parseFromString(svg, "image/svg+xml");
    // let input_svg = svg_doc.documentElement;
    let svg_width = input_svg.getAttribute("width");
    let svg_height = input_svg.getAttribute("height");

    let brush_active = false;

    let brushable_items = svg_g.selectAll(".brushable");
    let brushable_items_data = Array.from(brushable_items).map(brushable_item => ({
        id: brushable_item.getAttribute("id"),
        cx: parseFloat(brushable_item.getAttribute("cx")),
        cy: parseFloat(brushable_item.getAttribute("cy"))
    }));
    tree = create_rtree(brushable_items_data);

    let overlay = select(el).select("svg")
        .append("svg")
        .attr("id", "overlay")
        .attr("class", "notebook")
        .style("position", "absolute")
        .style("top", 0)
        .style("left", 0)
        .style("width", svg_width)
        .style("height", svg_height)
        .style("pointer-events", "none");

    let activate_brush = () => {
        brush_active = true;
        el.style.pointerEvents = "none";
        overlay.style.pointerEvents = "auto";

        if (!overlay.select("#brush_group").empty()) return;
        overlay.insert("g", ":first-child")
            .attr("id", "brush_group")
            .attr("class", "brush")
            .call(my_brush);
    }

    let disactivate_brush = () => {
        brush_active = false;
        el.style.pointerEvents = "auto";
        overlay.style.pointerEvents = "none";

        overlay.select("#brush_group").remove();
    }

    let brushed = (event) => {
        if (event.selection) {
            brush_active = true;
            let [[x0_screen, y0_screen], [x1_screen, y1_screen]] = event.selection;
            let bbox = {
                minX: Math.min(x0_screen, x1_screen),
                minY: Math.min(y0_screen, y1_screen),
                maxX: Math.max(x0_screen, x1_screen),
                maxY: Math.max(y0_screen, y1_screen)
            };
            let selected_points = tree.search(bbox);
            let selected_ids = selected_points.map(node => node.id);
            model.set("selected_ids", selected_ids);
            model.save_changes();
        }
    };

    let my_brush = brush()
        .filter((event) => {
            // Prevent contextual menu on Ctrl-click (macOS)
            if (event.ctrlKey && event.button === 0) {
                event.preventDefault();
            }
            return (
                !event.button && // Ignore mouse buttons other than left-click
                (event.metaKey || event.ctrlKey || event.target.__data__.type !== "overlay")
            );
        })
        .extent([[0, 0], [svg_width, svg_height]])
        .on("start brush end", brushed);

    model.on("change:selected_ids", () => {
        let selected_ids = model.get("selected_ids");
        svg_g.selectAll('.brushable')
            .classed('brushed', function() {
                return selected_ids.includes(this.id);
        });
    })

    window.addEventListener("keydown", (e) => {
        if (e.metaKey && !brush_active) { activate_brush(); }
    });
    window.addEventListener("dblclick", (e) => {
        if (brush_active) { disactivate_brush(); }
    });

}
export default { render };