# A Design System for arXiv
arXiv's DNA for product design and frontend development

## Design Tokens

We attempt a CSS organization in three tiers (or levels), to maximize reuse.

There is a lot of variation, but also a lot of adoption, of this pattern. Some interesting articles: 

- [The Many Faces of Themeable Design Systems](https://bradfrost.com/blog/post/the-many-faces-of-themeable-design-systems/) by Brad Frost

- [Managing context thanks to the middle tier](https://frontside.com/blog/2021-01-15-design-tokens-and-components/) while using the [BEM naming](https://getbem.com/naming/) philosophy in design tokens.

### Base/Primitves/Values Tier

The foundation is a set of global rules giving names to atomic CSS quantities, possibly in all [CSS data types](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_values_and_units/CSS_data_types). We
notably define brand `<color>`, `<dimension>`, `<string>` entities and calculations thereof.

The accepted naming rule is to add a common organization prefix (`--arxiv` here) followed by an optional design-oriented note (such as `-brand-`).

The main part of the name should reflect the foundational design role of the value.

Examples in this tier: 

```css
:root {
  --arxiv-brand-color-cornell-red: #b31b1b;
  --arxiv-border-thin            : solid 1px;
  --arxiv-font-base-size         : 1rem;
}
```

### Semantic/Alias/Theme Tier

The second tier provides names that aim to capture the "intent" of how a primitive is used. Is a certain color to become the "primary" in a design? Is it meant to apply to strokes? Is it the "inverted" variant in a pair of colors? Ideally the names are chosen in a way abstract enough to allow reuse in multiple components and layouts, but not so abstract that they are vague.

The accepted convention is to mark all names in this tier with the same prefix, which also indicates their internal nature. The frontend CSS is NOT meant to use the names in this layer. MUI uses `-sys-`, which we adopt for now.

Examples in this tier: 

```css
:root {
  --arxiv-sys-color-primary                  : var(--arxiv-brand-color-archival-blue);
  --arxiv-sys-color-primary--invert          : var(--arxiv-brand-color-open-blue);
  --arxiv-sys-color-stroke-on-primary        : var(--arxiv-brand-color-cool-wash);
  --arxiv-sys-color-stroke-on-primary--invert: var(--arxiv-brand-color-repository-brown);
}
```

### Component/Layout Tier

Lastly, each frontend component - as well as layout, needs to satisfy its concrete needs by picking from the previous Semantic/Alias/Theme tier.

A useful convention that _some_ design systems use is to distinguish between component rules and layout rules via a letter prefix (`--c` and `--l`).

Modifier pieces in a name are often separated with two dashes instead of one, such as `--hover`. But the component tier is also the most flexible, as these variables are the final dictionary in use by frontend app developers. As long as we indicate the component/layout name clearly in the variable names, we are on target.

```css
:root {
  --c-btn-primary-bg-color       : var(--arxiv-sys-color-primary);
  --c-btn-primary-fg-color       : var(--arxiv-sys-color-stroke-on-primary);
  --c-btn-primary-bg-color--hover: var(--arxiv-sys-color-primary--invert);
  --c-btn-primary-fg-color--hover: var(--arxiv-sys-color-stroke-on-primary--invert);
}
```

### Putting it all together

In a top-level CSS for our application (or component) we can import the design tokens using a CSS [`@layer`]() for each tier, to minimize chances of collisions:

```css
@import "./base.css" layer(base);
@import "./theme-primary.css" layer(theme);
/* @import "./theme-dark.css" layer(theme); */
@import "./components.css" layer(components);

@layer base, theme, components;
```

Note that this is where one can select the active theme. There may be more pluggable ways of achieving the same effect, such as loading it as the final layer e.g. 

```css
@layer base, theme, components, theme-active;
```

Then the frontend developers can attach component-tier properties as: 

```html
<button class="c-btn c-btn-primary" type="submit">Accept and Continue</button>
```

```css
.c-btn-primary {
  background-color: var(--c-btn-primary-bg-color);
  color           : var(--c-btn-primary-fg-color);
}
.c-btn-primary:hover {
  background-color: var(--c-btn-primary-bg-color--hover);
  color           : var(--c-btn-primary-fg-color--hover);
}
```
