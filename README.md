# PR Review Lab Starter

這是課程中的 **PR Lab**：它只提供一個可以被 Agent 審查的真實 Pull Request。

它和 Agent 專案是兩個不同的 repository：

| repository | 用途 |
| --- | --- |
| [langchain-mcp-langgraph-demo](https://github.com/justin0427/langchain-mcp-langgraph-demo) | 實作並執行 LangChain + GitHub MCP + LangGraph Agent。 |
| `pr-review-lab-你的名字/`（本 repo 的 Template） | 修改小程式、跑 CI、開 PR；讓 Agent 有一個目標可以審查。 |

**本 repo 不放 Agent 程式，也不在這裡設定 `.env` 或執行 `main.py`。** PR 建立後，請回到 Agent 專案執行審查。

## 課堂操作

1. 按 **Use this template**，建立自己的 `pr-review-lab-你的名字` repository。
2. Clone 自己的 repository，從 `main` 建立 `exercise/add-validation` 分支。
3. 依課程文章完整覆蓋 `app/price_calculator.py` 和 `tests/test_price_calculator.py`。
4. 跑測試、commit、push，回 GitHub 對自己的 `main` 開 PR。
5. 從 PR 網址記下 repository 名稱與 PR 編號，回到 **Agent 專案**執行審查。

```bash
# 執行位置：pr-review-lab-你的名字/ 專案根目錄
git switch -c exercise/add-validation
# 依課程文章覆蓋 app/price_calculator.py 與 tests/test_price_calculator.py
python3 -m unittest discover -s tests
git add .
git commit -m "feat: add input validation"
git push -u origin exercise/add-validation
```

接著到 GitHub 按 **Compare & pull request**，確認是把 `exercise/add-validation` 合回**你自己的** `main`。

例如 PR 網址是：

```text
https://github.com/amy/pr-review-lab-amy/pull/3
```

請切回 `langchain-mcp-langgraph-demo/`，在那裡執行：

```bash
python3 scripts/lab_helper.py run --repo amy/pr-review-lab-amy --pr 3
```

## 專案結構

```text
pr-review-lab-你的名字/
├── app/
│   └── price_calculator.py       # 這次會修改、被審查的小程式
├── tests/
│   └── test_price_calculator.py  # 單元測試；GitHub Actions 會自動執行
└── .github/workflows/test.yml    # CI
```
