# TapNote

TapNote is a minimalist, self-hosted publishing platform inspired by Telegra.ph, focusing on instant Markdown-based content creation. It provides a distraction-free writing experience with instant publishing capabilities, making it perfect for quick notes, blog posts, or documentation sharing.

![Demo](media/demo.gif)
<p align="center">
  <a href="https://tapnote-production.up.railway.app/" target="_blank" style="text-decoration:none;">
    <img src="https://img.shields.io/badge/Live%20Demo-Tap%20Here-blue?style=for-the-badge" alt="Live Demo">
  </a>
</p>

## Features

- **Minimalist Writing Experience**
  - Clean, distraction-free Markdown editor
  - No account required
  - Instant publishing with a single click
  - Support for full Markdown syntax
  - Self-hosted: maintain full control over your content

- **Content Management**
  - Unique URL for each post
  - Edit functionality with secure tokens
  - Proper rendering of all Markdown elements
  - Support for images and code snippets

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/vorniches/tapnote.git
cd tapnote
```

2. Start the application using Docker:
```bash
chmod +x setup.sh
./setup.sh
```

3. Access TapNote at `http://localhost:9009`

## Examples

```Markdown
# Heading 1
Some paragraph text here.

![Image](https://themepreview.home.blog/wp-content/uploads/2019/07/boat.jpg)

## Heading 2
Another paragraph of text with some **bold** text, *italic* text, and ~~strikethrough~~ text.

### Heading 3
1. An ordered list item
2. Another ordered list item

'```python
# Some Python code snippet
def greet(name):
    return f"Hello, {name}!"
```'

#### Heading 4
A quote block:
> This is a blockquote!

- Sub list item (unordered)
- Sub list item (unordered)

#### Table Example
| Column A | Column B |
|----------|----------|
| Cell 1A  | Cell 1B  |
| Cell 2A  | Cell 2B  |

https://youtu.be/vz91QpgUjFc?si=6nTE2LeukJprXiw1
```

> Note: For correct rendering of code exmaple remove `'` symbols.

## Deploying

Deploy TapNote on a server in a few clicks and connect a custom domain with [RailWay](https://railway.com?referralCode=eKC9tt) or your preferred service.

## Contributing

Feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)

## Acknowledgments

- Inspired by [Telegra.ph](https://telegra.ph)
- Built with Django and Tailwind CSS
- Kickstarted in minutes using [Prototype](https://github.com/vorniches/prototype), [snap2txt](https://github.com/vorniches/snap2txt) and [Cursor](https://cursor.so)
- Uses Space Mono font by Google Fonts

## Support

- Create an issue for bug reports or feature requests
- Star the repository if you find it useful
- Fork it to contribute or create your own version