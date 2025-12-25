# Callout Shortcode 使用指南

## 简介

`callout` shortcode 是一个用于在 Hugo 内容中创建美观提示框的组件。它支持多种类型和自定义标题。

## 基本用法

### 语法

```markdown
{{< callout type="类型" title="标题（可选）" >}}
这里是内容
{{< /callout >}}
```

### 支持的类型

- `info` - 信息提示（蓝色）
- `tip` - 提示/建议（绿色）
- `warning` - 警告（橙色）
- `note` - 笔记（紫色）
- `quote` - 引用（灰色）
- `success` - 成功（绿色）
- `danger` - 危险/错误（红色）

## 使用示例

### 1. 带标题的 Callout

```markdown
{{< callout type="info" title="Quick take" >}}
I am inviting collaborators from ForestGEO and other FDP networks to test whether *structural diversity* can reduce long-term stability.
{{< /callout >}}
```

### 2. 不带标题的 Callout（使用类型名作为标题）

```markdown
{{< callout type="warning" >}}
This is a warning without a custom title.
{{< /callout >}}
```

### 3. 假设/研究提示

```markdown
{{< callout type="tip" title="Hypothesis" >}}
In species-rich natural tropical forests, higher structural diversity may **destabilize** long-term function.
{{< /callout >}}
```

### 4. 重要说明

```markdown
{{< callout type="note" title="Why FDP plots matter" >}}
Long-term FDP censuses are one of the few data infrastructures that can directly test these questions.
{{< /callout >}}
```

### 5. 成功提示

```markdown
{{< callout type="success" title="Success" >}}
Your operation completed successfully!
{{< /callout >}}
```

### 6. 危险/错误提示

```markdown
{{< callout type="danger" title="Important" >}}
This is a critical warning that requires immediate attention.
{{< /callout >}}
```

## 自定义图标

你也可以自定义图标（使用 Font Awesome 图标类名）：

```markdown
{{< callout type="info" title="Custom Icon" icon="fa-star" >}}
This callout uses a custom star icon.
{{< /callout >}}
```

## 在 Markdown 中使用

Callout shortcode 支持 Markdown 语法，包括：

- **粗体** 和 *斜体*
- 链接
- 列表
- 代码块

示例：

```markdown
{{< callout type="tip" title="Tips" >}}
- Use **bold** for emphasis
- Use *italic* for subtle emphasis
- Add [links](https://example.com) as needed
{{< /callout >}}
```

## 替换旧的 Callout 格式

如果你之前使用的是 Markdown blockquote 格式：

```markdown
> **Callout | Quick take**
> Your content here
```

可以替换为：

```markdown
{{< callout type="info" title="Quick take" >}}
Your content here
{{< /callout >}}
```

## 样式特性

- 响应式设计，适配移动设备
- 支持深色模式
- 左侧彩色边框标识类型
- 图标和标题清晰可见
- 内容区域支持 Markdown 渲染

## 查看示例

访问 `/elements` 页面查看所有 callout 类型的实际效果。

