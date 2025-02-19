# pptx-editor

📌 **pptx-editor** is a Python library for modifying PowerPoint slides, allowing users to:
- **Navigate between slides** (next, previous, jump to a specific slide).
- **Add a red dot** to highlight areas in a presentation.

---

## 🚀 Features

✅ Change slides (Next, Previous, Jump to Specific Slide)  
✅ Add a **red dot** anywhere on a slide  
✅ Save modified presentations  

---

## 🚀 Installation

1. Copy the entire pptx_editor folder to your new project.
2. Navigate to the root directory where setup.py is located. 
3. Install it using

```sh
pip install -e 
```

---

## 📖 Usage

### **1️⃣ Import the Library**
```python
from pptx_editor.editor import PPTXEditor
```

---

# 📌 pptx-editor Functions Documentation

## 1️⃣ Navigation Functions

| Function | Description |
|----------|------------|
| `next_slide()` | Moves to the **next slide** (if available). |
| `previous_slide()` | Moves to the **previous slide** (if available). |
| `go_to_slide(slide_index: int)` | Moves to a **specific slide** by index. |
| `get_current_slide_index()` | Returns the **current slide index**. |
| `get_total_slides()` | Returns the **total number of slides** in the presentation. |

---

## 2️⃣ Editing Functions

| Function | Description |
|----------|------------|
| `add_red_dot(x: float, y: float, size: float = 0.3)` | Adds a **red dot** to the current slide at position `(x, y)` in inches. |
| `save_presentation(output_path: str)` | Saves the **modified PowerPoint file** to `output_path`. |

---
