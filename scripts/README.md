# Publication Fetcher Script

## 使用方法

### 安装依赖
```bash
pip install requests pyyaml
```

### 运行脚本

#### 方法 1: 使用 DOI
```bash
python scripts/fetch_publication.py "10.1016/j.jenvman.2024.123456"
```

#### 方法 2: 使用 ScienceDirect URL
```bash
python scripts/fetch_publication.py "https://www.sciencedirect.com/science/article/pii/S0301479724038659"
```

#### 方法 3: 使用 DOI URL
```bash
python scripts/fetch_publication.py "https://doi.org/10.1016/j.jenvman.2024.123456"
```

### 输出

脚本会输出 YAML 格式的数据，你可以直接复制到 `data/publications.yaml` 文件中。

### 示例

对于你提供的文章：
```bash
python scripts/fetch_publication.py "https://www.sciencedirect.com/science/article/pii/S0301479724038659?via%3Dihub"
```

脚本会：
1. 自动提取 DOI
2. 从 Crossref API 获取元数据
3. 生成 YAML 格式输出
4. 你可以直接复制到 `data/publications.yaml` 的 `publications:` 列表下

### 注意事项

- 如果 Crossref API 没有数据，脚本会尝试从 ScienceDirect 页面直接抓取
- 某些字段（如 categories 和 tags）需要手动添加
- 如果自动获取失败，你可以手动编辑 YAML 文件



