import { AKElement } from "@goauthentik/elements/Base";

import { TemplateResult, html, nothing } from "lit";
import { customElement, property } from "lit/decorators.js";

@customElement("ak-textarea-input")
export class AkTextareaInput extends AKElement {
    // Render into the lightDOM. This effectively erases the shadowDOM nature of this component, but
    // we're not actually using that and, for the meantime, we need the form handlers to be able to
    // find the children of this component.
    //
    // TODO: This abstraction is wrong; it's putting *more* layers in as a way of managing the
    // visual clutter and legibility issues of ak-form-elemental-horizontal and patternfly in
    // general.
    protected createRenderRoot() {
        return this;
    }

    @property({ type: String })
    name!: string;

    @property({ type: String })
    label = "";

    @property({ type: String })
    value = "";

    @property({ type: Boolean })
    required = false;

    @property({ type: String })
    help = "";

    @property({ type: Object })
    bighelp!: TemplateResult | TemplateResult[];

    renderHelp() {
        return [
            this.help ? html`<p class="pf-c-form__helper-textarea">${this.help}</p>` : nothing,
            this.bighelp ? this.bighelp : nothing,
        ];
    }

    render() {
        return html`<ak-form-element-horizontal
            label=${this.label}
            ?required=${this.required}
            name=${this.name}
        >
            <textarea class="pf-c-form-control" ?required=${this.required} name=${this.name}>
${this.value !== undefined ? this.value : ""}</textarea
            >
            ${this.renderHelp()}
        </ak-form-element-horizontal> `;
    }
}

export default AkTextareaInput;
