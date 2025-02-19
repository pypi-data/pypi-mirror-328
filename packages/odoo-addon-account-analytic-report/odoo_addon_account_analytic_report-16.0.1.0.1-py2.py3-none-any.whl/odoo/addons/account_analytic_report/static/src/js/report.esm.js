
/** @odoo-module */

import { useComponent, useEffect } from "@odoo/owl";

function toggleGroupArrow(element) {
    element.classList.toggle("fa-caret-right");
    element.classList.toggle("fa-caret-down");
}

function toggleChildrenVisibility(element) {
    function showChildren(parentRow) {
        const parentLevel = parseInt(parentRow.getAttribute("data-group-level"), 10);
        let nextRow = parentRow.nextElementSibling;

        while (nextRow) {
            const childLevel = parseInt(nextRow.getAttribute("data-group-level"), 10);

            if (childLevel === parentLevel + 1) {
                // Show direct children
                nextRow.classList.remove("d-none");
            } else if (childLevel <= parentLevel) {
                // Stop if we encounter a row at the same or higher level
                break;
            }

            nextRow = nextRow.nextElementSibling;
        }
    }

    function hideChildren(parentRow) {
        const parentLevel = parseInt(parentRow.getAttribute("data-group-level"), 10);
        let nextRow = parentRow.nextElementSibling;

        while (nextRow) {
            const childLevel = parseInt(nextRow.getAttribute("data-group-level"), 10);

            if (childLevel > parentLevel) {
                // Hide all rows deeper in the hierarchy
                nextRow.classList.add("d-none");

                // Reset arrow for any nested group
                const arrow = nextRow.querySelector(".fa-caret-down");
                if (arrow) {
                    toggleGroupArrow(arrow);
                }
            } else {
                // Stop hiding when we reach a sibling or parent level
                break;
            }

            nextRow = nextRow.nextElementSibling;
        }
    }

    const parentRow = element.closest(".lines");
    if (element.classList.contains("fa-caret-down")) {
        // Unfold: Show children
        parentRow.classList.add("unfolded_group");
        showChildren(parentRow);
    } else {
        // Fold: Hide children
        const parentLevel = parseInt(parentRow.getAttribute("data-group-level"), 10);
        if (parentLevel > 1) {
            parentRow.classList.remove("unfolded_group");
        }
        hideChildren(parentRow);
    }
}

function enrich(component, targetElement, selector, isIFrame = false) {
    let doc = window.document;
    let contentDocument = targetElement;

    // If we are in an iframe, we need to take the right document
    // both for the element and the doc
    if (isIFrame) {
        contentDocument = targetElement.contentDocument;
        doc = contentDocument;
    }

    // If there is a selector, we may have multiple blocks of code to enrich
    const targets = [];
    if (selector) {
        targets.push(...contentDocument.querySelectorAll(selector));
    } else {
        targets.push(contentDocument);
    }

    // Search the elements with the selector, update them and bind an action.
    for (const currentTarget of targets) {
        const elementsToWrap = currentTarget.querySelectorAll("[res-model][domain]");
        for (const element of elementsToWrap.values()) {
            const wrapper = doc.createElement("a");
            wrapper.setAttribute("href", "#");
            wrapper.addEventListener("click", async (ev) => {
                ev.preventDefault();
                ev.stopImmediatePropagation();
                try {
                    const action = await component.env.services.orm.call(
                        element.getAttribute("res-model"),
                        "get_analytic_entries_action",
                        [element.getAttribute("domain")],
                    )
                    component.env.services.action.doAction(action);
                } catch (e) {
                    console.error(e);
                }
            });
            element.parentNode.insertBefore(wrapper, element);
            wrapper.appendChild(element);
        }

        const elementsToToggle = currentTarget.querySelectorAll(
            ".fa.fa-caret-right,.fa.fa-caret-down,.grouping"
        );
        for (const element of elementsToToggle.values()) {
            element.addEventListener("click", () => {
                toggleGroupArrow(element);
                toggleChildrenVisibility(element);
            });
        }
    }
}

export function useEnrichWithActionLinks(ref, selector = null) {
    const comp = useComponent();

    useEffect(
        (element) => {
            // If we get an iframe, we need to wait until everything is loaded
            if (element.matches("iframe")) {
                element.addEventListener("load", () =>
                    enrich(comp, element, selector, true)
                );
            } else {
                enrich(comp, element, selector);
            }
        },
        () => [ref.el]
    );
}