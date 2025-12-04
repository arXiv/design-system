# Brand Reference

<style>
    .button {
        border-radius:0.5em; 
        border-width:0;
        padding:0.5em 1em;
        font-size:1.15em;
        margin-bottom: 1em;
        transition: all 0.5s;
    }
    .button-primary {
        background-color:#1f5e96; 
        color:#f7fafc; 
        box-shadow: 2px 2px 0px 0px #a5d6fe;
    }
    .dark .button-primary {
        box-shadow: 2px 2px 0px 0px #06337aff;
    }
    .button-primary:hover {
        background-color:black; 
    }
    .button-secondary {
        background-color:#f7fafc;
        color:#0067b5; 
        box-shadow: 2px 2px 0px 0px #c0dff7ff;
    }
    .dark .button-secondary {
        box-shadow: 2px 2px 0px 0px #4f81aaff;
    }
    .button-secondary:hover {
        background-color:#a5d6fe;
    }
    .button-disabled {

    }
    .button-minimal {
        font-weight: normal;
        padding: 0.25em 0.5em;
        border-radius:0.35em;
        background-color: #e8e8e8ff;
        color: #2d2d2d;
        box-shadow: 2px 2px 0px 0px #4c4c4cff;
    }
    .dark .button-minimal {
        box-shadow: 2px 2px 0px 0px #7b7b7b;
    }
    .button-danger {

    }
    .button-warning {
        background-color: #ffc107;
        color: black;
        box-shadow: 2px 2px 0px 0px #8a5a00;
    }
    .dark, .light {
        padding: 1em;
    }
    .dark {
        background-color:#1c1a17;
    }
    .light{
        background-color: white;
    }
</style>

## Foundations
This section documents global decisions related to Color and Typography, and perhaps Grid and Spacing units if we get that far.

### Brand Colors
#### Primary
<table style="border-collapse:collapse; width:100%; max-width:1100px; margin-bottom:1rem;">
	<tr>
		<td style="background:#6b6459; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#b31b1b; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#fb595a; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#a5d6fe; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#1f5e96; height:96px; width:20%; border:1px solid #eee;"></td>
	</tr>
	<tr>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Library Grey</strong><br>
			Hex: <code>#6b6459</code><br>
			CMYK: 55, 51, 60, 24<br>
			RGB: 107, 100, 89
		</td>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Cornell Red</strong><br>
			Hex: <code>#b31b1b</code><br>
			CMYK: 21, 100, 100, 12<br>
			RGB: 179, 27, 27
		</td>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Publishing Pink</strong><br>
			Hex: <code>#fb595a</code><br>
			CMYK: 00, 80, 59, 00<br>
			RGB: 251, 89, 90
		</td>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Open Blue</strong><br>
			Hex: <code>#a5d6fe</code><br>
			CMYK: 31, 05, 00, 00<br>
			RGB: 165, 214, 254
		</td>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Archival Blue</strong><br>
			Hex: <code>#1f5e96</code><br>
			CMYK: 92, 66, 16, 02<br>
			RGB: 31, 94, 150
		</td>
	</tr>
</table>

#### Complimentary
<table style="border-collapse:collapse; width:100%; max-width:1100px;">
	<tr>
		<td style="background:#c4d82e; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#1c1a17; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#f7fafc; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#f9f7f7; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:transparent; height:96px; width:20%; border:1px solid #eee;"></td>
	</tr>
	<tr>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Access Lime</strong><br>
			Hex: <code>#c4d82e</code><br>
			CMYK: 2, 0, 100, 0<br>
			RGB: 196, 216, 46
		</td>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Repository Brown</strong><br>
			Hex: <code>#1c1a17</code><br>
			CMYK: 0, 1, 2, 89<br>
			RGB: 28, 26, 23
		</td>
        <td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Cool Wash</strong><br>
			Hex: <code>#f7fafc</code><br>
			CMYK: 02, 00, 00, 00<br>
			RGB: 247, 250, 242
		</td>
        <td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Warm Wash</strong><br>
			Hex: <code>#f9f7f7</code><br>
			CMYK: 21, 100, 100, 12<br>
			RGB: 179, 27, 27
		</td>
        <td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>?</strong><br>
			Hex: <code>?</code><br>
			CMYK: ?<br>
			RGB: ?
		</td>
	</tr>
</table>

#### Reserved Colors
<table style="border-collapse:collapse; width:100%; max-width:1100px;">
	<tr>
		<td style="background:#0067b5; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#1e8bc3; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#dc3545; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#ffc107; height:96px; width:20%; border:1px solid #eee;"></td>
		<td style="background:#28a745; height:96px; width:20%; border:1px solid #eee;"></td>
	</tr>
	<tr>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Link Blue - Light Mode</strong><br>
			Hex: <code>#0067b5</code><br>
			CMYK: 2, 0, 100, 0<br>
			RGB: 196, 216, 46
		</td>
        <td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Link Blue - Dark Mode</strong><br>
			Hex: <code>#1e8bc3</code><br>
			CMYK: 65, 22, 0, 24<br>
			RGB: 30, 139, 195
		</td>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Error Red (main)</strong><br>
			Hex: <code>#dc3545</code><br>
			CMYK: 0, 76, 69, 14<br>
			RGB: 220, 53, 69
		</td>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Warning Yellow (main)</strong><br>
			Hex: <code>#ffc107</code><br>
			CMYK: 0, 24, 97, 0<br>
			RGB: 255, 193, 7
		</td>
		<td style="padding:10px; vertical-align:top; text-align:center; border:1px solid #eee;">
			<strong>Success Green (main)</strong><br>
			Hex: <code>#28a745</code><br>
			CMYK: 76, 0, 59, 35<br>
			RGB: 40, 167, 69
		</td>
	</tr>
</table>

#### Status colors

<table style="border-collapse:collapse; width:100%; max-width:1100px;">
	<tr>
		<td style="background:#dc3545; height:96px; width:33.333%; border:1px solid #eee;"></td>
		<td style="background:#ffc107; height:96px; width:33.333%; border:1px solid #eee;"></td>
		<td style="background:#28a745; height:96px; width:33.333%; border:1px solid #eee;"></td>
	</tr>
	<tr>
		<td style="padding:10px; vertical-align:top; text-align:left; border:1px solid #eee;">
			<strong>Error</strong><br>
			Wash: <code>#f8d7da</code><br>
			Accent: <code>#dc3545</code><br>
			Headings: <code>#b71c1c</code><br>
			Text: <code>#721c24</code><br>
		</td>
		<td style="padding:10px; vertical-align:top; text-align:left; border:1px solid #eee;">
			<strong>Warning</strong><br>
			Wash: <code>#fff3cd</code><br>
			Accent: <code>#ffc107</code><br>
			Headings: <code>#8a5a00</code><br>
			Text: <code>#856404</code><br>
		</td>
		<td style="padding:10px; vertical-align:top; text-align:left; border:1px solid #eee;">
			<strong>Success</strong><br>
			Wash: <code>#d4edda</code><br>
			Accent: <code>#28a745</code><br>
			Headings: <code>#1b5e20</code><br>
			Text: <code>#155724</code><br>
		</td>
	</tr>
</table>

#### Accessible color contrast notes for status colors

- Error: Heading (`#b71c1c`) and Text (`#721c24`) both pass on the Wash (`#f8d7da`). Header areas with Accent (`#dc3545`) as a background should use white heading text.
- Warning: Heading (`#8a5a00`) and Text (`#856404`) both pass on the Wash (`#fff3cd`). Header areas with Accent (`#ffc107`) as a background should use black heading text. 
- Success: Heading (`#1b5e20`) and Text (`#155724`) pass on the Wash (`#d4edda`). Header areas with Accent (`#28a745`) as a background should use black heading text.

#### Status message examples

<div style="background:#f8d7da; border:2px solid #dc3545; color:#721c24; border-radius:6px; padding:0; margin:0;">
  <div style="background-color:#dc3545; margin:0 0 1em 0; padding:0; display: block; width:100%; float:left;"><h2 style="border:0;margin:0.5em;color:white;font-size:1.2em;">Changes did not save</h2></div>
  <strong style="color:#b71c1c; margin:1em;">Error</strong>
  <p style="color:#721c24; margin: 0 1em;">There was a problem with saving your changes. Please try again.</p>
  <br>
</div>
<br>

<div style="background:#fff3cd; border:2px solid #ffc107; color:#721c24; border-radius:6px; padding:0; margin:0;">
  <div style="background-color:#ffc107; margin:0 0 1em 0; padding:0; display: block; width:100%; float:left;"><h2 style="border:0;margin:0.5em;color:black;font-size:1.2em;">You are unsubmitting</h2></div>
  <strong style="color:#8a5a00; margin:1em;">Warning</strong>
  <p style="color:#856404; margin: 0 1em;">Unsubmitting your work will take it out of the announcement queue. Resubmitting will place it at the back of the line. Do you want to proceed?</p><br>
  <div style="display:flex; justify-content:flex-end; gap:0.5em; margin-right:1em; clear:both;">
  <button class="button button-minimal">Cancel</button>
  <button class="button button-warning">Proceed and unsubmit</button>
  </div>
</div>
<br>

<div style="background:#d4edda; border:2px solid #28a745; color:#721c24; border-radius:6px; padding:0; margin:0;">
  <div style="background-color:#28a745; margin:0 0 1em 0; padding:0; display: block; width:100%; float:left;"><h2 style="border:0;margin:0.5em;color:black;font-size:1.2em;">Changes are saved</h2></div>
  <strong style="color:#1b5e20; margin:1em;">Success</strong>
  <p style="color:#155724; margin: 0 1em;">Your changes have saved. You may leave this page.</p><br>
</div>

## Components
This section includes documentation for individual UI components like Button, Input field, Card, etc. We will grow this list incrementally as we make progress and the different repos are ready for further implementation.

### Links
<p style="display:block; background-color:white; color:black; padding:1em;">This paragraph passes color contrast compliance for links in Light Mode. It uses <a href="#" style="color:#0067b5;text-decoration:underline;">Link Blue - Light Mode</a>, the surrounding text is black, and the background is white.</p>

<p style="display: block; background-color:#1c1a17; color:white; padding: 1em;">This paragraph passes color contrast compliance for links in Dark Mode. It uses <a href="#" style="color:#1e8bc3;text-decoration:underline;">Link Blue - Dark Mode</a>, the surrounding text is white, and the background is Repository Brown.</p>

### Buttons
The following button styles pass color contrast compliance. Use the visual display as a basic color reference only, not as a detailed style guide.

<table style="border-collapse:collapse; width:100%; max-width:1100px;">
	<tr>
		<td>Light Mode</td>
        <td>Dark Mode</td>
    </tr>
    <tr>
		<td class="light">
            <button class="button-primary button">Primary Button</button>
            <button class="button-secondary button">Secondary Button</button>
            <button class="button-minimal button">Minimal Button</button>
        </td>
        <td class="dark">
            <button class="button-primary button">Primary Button</button>
            <button class="button-secondary button">Secondary Button</button>
            <button class="button-minimal button">Minimal Button</button>
        </td>
    </tr>
</table>


## Patterns
This section will include complex, multi-component decisions. For example Forms, Navigation, and Data display tables. This work will be part of a later design system phase.

## Logos and Icons
arXiv's suite of logos and related icons (ie: smileybones) are available as vector graphics. This section will document decisions around those vector files.