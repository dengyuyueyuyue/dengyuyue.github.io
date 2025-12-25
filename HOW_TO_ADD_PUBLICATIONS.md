# 如何添加文章到 Publications 页面

## 方法 1: 使用脚本自动获取（推荐）

### 步骤：

1. **找到文章的 DOI**
   - 打开文章页面（如 ScienceDirect）
   - 在页面上找到 DOI，通常格式为 `10.xxxx/xxxxx`
   - 例如：`10.1016/j.jenvman.2024.123456`

2. **运行脚本**
   ```bash
   py scripts/add_publication.py "10.1016/j.jenvman.2024.123456"
   ```

3. **复制输出**
   - 脚本会输出 YAML 格式的数据
   - 复制输出的内容

4. **添加到配置文件**
   - 打开 `data/publications.yaml`
   - 找到 `publications:` 列表
   - 将复制的 YAML 内容添加到列表末尾

5. **添加分类和标签**（可选）
   - 编辑刚添加的条目
   - 在 `categories:` 和 `tags:` 下添加相关分类

### 示例

对于你的文章 `https://www.sciencedirect.com/science/article/pii/S0301479724038659`：

1. 在文章页面上找到 DOI（通常是 `10.1016/j.jenvman.2024.xxxxx` 格式）
2. 运行：
   ```bash
   py scripts/add_publication.py "10.1016/j.jenvman.2024.xxxxx"
   ```
3. 复制输出到 `data/publications.yaml`

## 方法 2: 手动添加

如果脚本无法获取信息，可以手动添加：

1. 打开 `data/publications.yaml`
2. 在 `publications:` 列表下添加新条目：

```yaml
publications:
  - title: "文章标题"
    authors:
      - "作者1"
      - "作者2"
    journal: "期刊名称"
    year: 2024
    volume: "123"  # 可选
    pages: "1-10"  # 可选
    doi: "10.xxxx/xxxxx"  # 可选
    url: "https://www.sciencedirect.com/science/article/pii/S0301479724038659"
    abstract: "文章摘要..."
    categories:
      - "分类1"
      - "分类2"
    tags:
      - "标签1"
      - "标签2"
```

## 如何找到 DOI

### ScienceDirect 文章
- 在文章页面右侧或底部通常有 DOI 信息
- 格式：`https://doi.org/10.1016/j.jenvman.2024.xxxxx`
- 或者直接看页面上的 "DOI:" 标签

### 其他来源
- 大多数学术文章都会显示 DOI
- 可以在文章页面搜索 "DOI" 关键词
- 或者查看文章的引用信息

## 注意事项

- DOI 格式必须是 `10.xxxx/xxxxx`
- 如果找不到 DOI，可以直接使用文章 URL
- `categories` 和 `tags` 需要手动添加，用于分类和搜索
- 保存文件后，Hugo 会自动重新生成页面



