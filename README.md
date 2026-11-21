# Krita Hide Welcome Panels

[English](#english) | [中文](#中文)

---

## English

A tiny Krita Python plugin that hides the **Start** column (new/open buttons and help links) and the **News** column of Krita's welcome page, leaving only the recent-documents list. The welcome page appears when no document is open.

Unlike hiding them with a Qt style sheet, this plugin hides the columns **before they are first shown**, so they don't flash at startup.

### Compatibility

- Krita 5.3.x (Qt5 / PyQt5)
- Krita 6.0.x (Qt6 / PyQt6)
- Not available on Android (Krita does not support Python plugins there)

### Installation

1. Download `hide_welcome_panels-x.y.z.zip` from [Releases](../../releases). Don't unzip it.
2. In Krita: **Tools → Scripts → Import Python Plugin from File…**, then select the zip.
3. Go to **Settings → Configure Krita → Python Plugin Manager** and enable **Hide Welcome Panels**.
4. Restart Krita.

#### Manual installation

Copy the contents of `src/` into the `pykrita` folder in Krita's resource folder (**Settings → Manage Resources → Open Resource Folder**). The `.desktop` file and the plugin folder must sit side by side:

```
pykrita/
├── hide_welcome_panels.desktop
└── hide_welcome_panels/
```

### Configuration

Edit `HIDE_NAMES` near the top of `hide_welcome_panels/hide_welcome_panels.py`:

| Name | Column |
|---|---|
| `widgetCenter` | Start: new/open buttons and help links (hidden by default) |
| `widgetRight` | News, update notifications, support message (hidden by default) |
| `widgetRecentImagesColumn` | Recent documents. Add it to get a completely blank background. |

These object names come from Krita's [`libs/ui/forms/KisWelcomePage.ui`](https://invent.kde.org/graphics/krita/-/blob/master/libs/ui/forms/KisWelcomePage.ui).

With the Start column hidden, use **Ctrl+N** to create a document and **Ctrl+O** to open one. Dropping a file onto the window also still opens it.

### How it works

`Extension.setup()` runs before Krita creates its main window. There, the plugin installs an application-wide event filter. When a widget with one of the configured names is polished or shown inside `KisWelcomePage`, the filter hides it before it is ever painted.

### Releasing

Push a tag that starts with `v`. GitHub Actions then packages the plugin and publishes a release with the zip attached:

```bash
git tag v1.0.0
git push origin v1.0.0
```

You can also run the **Release** workflow manually from the Actions tab.

---

## 中文

一个很小的 Krita Python 插件，用来隐藏 Krita 开始页面（没有打开任何文档时显示的页面）上的 **Start 栏**（新建、打开按钮和帮助链接）和 **News 栏**，只保留最近文件列表。

用 Qt 样式表隐藏的话，这两栏会在启动时先闪一下。这个插件在它们**第一次显示之前**就把它们隐藏掉，所以不会闪。

### 兼容性

- Krita 5.3.x（Qt5 / PyQt5）
- Krita 6.0.x（Qt6 / PyQt6）
- 不支持 Android 版（Krita 在 Android 上不支持 Python 插件）

### 安装

1. 从 [Releases](../../releases) 下载 `hide_welcome_panels-x.y.z.zip`，不用解压。
2. 在 Krita 里点 **工具 → 脚本 → 从文件导入 Python 插件**，选择这个 zip。
3. 到 **设置 → 配置 Krita → Python 插件管理器**，勾选 **Hide Welcome Panels**。
4. 重启 Krita。

#### 手动安装

把 `src/` 里的内容复制到 Krita 资源文件夹下的 `pykrita` 文件夹里（资源文件夹可以从 **设置 → 管理资源 → 打开资源文件夹** 打开）。`.desktop` 文件和插件文件夹要并排放：

```
pykrita/
├── hide_welcome_panels.desktop
└── hide_welcome_panels/
```

### 配置

修改 `hide_welcome_panels/hide_welcome_panels.py` 顶部的 `HIDE_NAMES`：

| 名称 | 对应的栏 |
|---|---|
| `widgetCenter` | Start 栏：新建、打开按钮和帮助链接（默认隐藏） |
| `widgetRight` | News 栏：新闻、更新提示和赞助信息（默认隐藏） |
| `widgetRecentImagesColumn` | 最近文件。加上它，开始页面就是一片空白背景。 |

这些对象名来自 Krita 源码 [`libs/ui/forms/KisWelcomePage.ui`](https://invent.kde.org/graphics/krita/-/blob/master/libs/ui/forms/KisWelcomePage.ui)。

隐藏 Start 栏之后，用 **Ctrl+N** 新建文档、**Ctrl+O** 打开文档。把文件直接拖进窗口也能打开。

### 原理

Krita 会在创建主窗口之前调用插件的 `Extension.setup()`。插件在这里给整个应用装了一个事件过滤器。当 `KisWelcomePage` 里名字匹配的控件被初始化或者要显示时，过滤器就把它隐藏掉，这些控件一次都不会画出来。

### 发布

推送一个以 `v` 开头的标签，GitHub Actions 就会自动打包插件，创建一个附带 zip 的 Release：

```bash
git tag v1.0.0
git push origin v1.0.0
```

也可以在 Actions 页面手动运行 **Release** 工作流。
