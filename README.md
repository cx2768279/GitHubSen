# loupython3 项目说明

本文档说明如何使用 Conda 管理虚拟环境、安装依赖及运行项目。

---

## 📦 环境配置

### 1. 创建 Conda 虚拟环境
使用以下命令创建名为 `loupython3` 的虚拟环境（Python 3.9 为例）：
```bash
conda create --name loupython3 python=3.9
```

### 2. 激活环境
- ​**Windows**:
  ```bash
  conda activate loupython3
  ```
- ​**macOS/Linux**:
  ```bash
  conda activate loupython3
  ```

激活后，命令行提示符会显示 `(loupython3)`。

### 3. 安装依赖
#### 方式一：通过 Conda 直接安装
```bash
# 安装单个包（示例：numpy）
conda install numpy

# 安装多个包（示例：numpy + pandas）
conda install numpy pandas
```

#### 方式二：通过 requirements.txt 安装
1. 将依赖包写入 `requirements.txt`（示例内容）：
   ```text
   numpy==1.21.0
   pandas>=1.3.0
   matplotlib
   ```
2. 运行以下命令安装所有依赖：
   ```bash
   pip install -r requirements.txt
   ```

### 4. 退出环境
```bash
conda deactivate
```

---

## 🔄 环境复现与共享

### 导出当前环境配置
生成 `environment.yml` 文件（包含所有依赖的精确版本）：
```bash
conda env export > environment.yml
```

### 从文件复现环境
其他用户可通过以下命令一键创建相同环境：
```bash
conda env create -f environment.yml
```

---

## ❗ 注意事项
1. ​**优先使用 Conda 安装包**：  
   Conda 能更好地解决依赖冲突。若某个包在 Conda 仓库中不存在，再用 `pip` 安装。

2. ​**国内镜像加速**​（可选）  
   在 `loupython3` 环境中运行以下命令配置清华镜像：
   ```bash
   conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
   conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
   conda config --set show_channel_urls yes
   ```

3. ​**更新依赖**  
   - 更新单个包：`conda update 包名`
   - 更新所有包：`conda update --all`

4. ​**删除环境**  
   ```bash
   conda env remove --name loupython3
   ```

---

## ⚡ 快速命令总结
| 操作                     | 命令                                  |
|--------------------------|---------------------------------------|
| 创建环境                 | `conda create --name loupython3 python=3.9` |
| 激活环境                 | `conda activate loupython3`           |
| 退出环境                 | `conda deactivate`                    |
| 安装依赖                 | `conda install 包名` 或 `pip install 包名` |
| 导出环境配置             | `conda env export > environment.yml`  |
| 列出所有环境             | `conda env list`                      |
