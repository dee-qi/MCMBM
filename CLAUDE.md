# CLAUDE.md — MCMBM (My Course Must Be Mine)

## Project Overview

MCMBM is a single-file Python script that automates course registration ("抢课") for students at Shandong University (SDU). It polls the university's course selection system at a fixed interval until a target course is successfully registered.

**Repository language:** Python 3
**Lines of code:** ~87
**Files:** `choose_course.py`, `README.md`

---

## Repository Structure

```
MCMBM/
├── choose_course.py   # Entire application — login, polling loop, time formatter
└── README.md          # Chinese/English usage instructions
```

There is no package structure, configuration file, test suite, or dependency manifest.

---

## Code Architecture

### `choose_course.py`

Three functions plus a `__main__` block:

| Symbol | Purpose |
|---|---|
| `time_spent(t)` | Returns a human-readable Chinese string of elapsed seconds since `t` (e.g. `3分钟20秒`) |
| `login(session, j_username, j_password)` | MD5-hashes the password, POSTs credentials to `bkjwxk.sdu.edu.cn/b/ajaxLogin`, returns `True` on success |
| `start_fucking_the_server(session, j_username, j_password, kch, kxh)` | Polling loop — POSTs to `/b/xk/xs/add/<kch>/<kxh>` every 3 seconds until success or an invalid-course response |
| `__main__` block | Collects credentials and course codes via `input()`, calls `login()` then `start_fucking_the_server()` |

### Key implementation details

- **Authentication:** Password is MD5-hashed client-side before transmission. The session cookie is maintained via `requests.Session`.
- **Polling interval:** Hard-coded `time.sleep(3)` inside `start_fucking_the_server`. The README warns not to go below 1.8 s to avoid server-side rate limiting.
- **Success detection:** String match `'成功'` (Chinese for "success") in the response body.
- **Invalid course detection:** String match `'缓存'` ("cache") in the response body triggers re-prompting and a recursive retry.
- **Target endpoint:** `http://bkjwxk.sdu.edu.cn` (HTTP, not HTTPS).

---

## Development Conventions

### Language

- All user-facing print statements are in Chinese (Simplified).
- Code comments are in English.
- Keep this bilingual convention for any new output strings.

### Style

- No linter or formatter is enforced. The file uses 4-space indentation throughout — maintain this.
- No type annotations. Do not add them unless the scope of the change requires it.
- Keep the script as a single file. Do not introduce modules or packages for small changes.

### Dependencies

There is no `requirements.txt`. The only third-party dependency is:

```
requests
```

Install manually:

```bash
pip install requests
```

No virtual-environment tooling is configured; the project expects a plain system/user Python 3 install.

---

## Running the Script

```bash
python choose_course.py
# or, if python defaults to Python 2 on the system:
python3 choose_course.py
```

The script is fully interactive — it will prompt for:
1. Student number (`学号`)
2. Course selection password (`选课密码`)
3. Course code (`课程号`, e.g. `sd03031770`)
4. Section number (`课序号`, e.g. `100`)

Press `Ctrl+C` at any time to abort.

---

## Changing the Polling Interval

Edit the `time.sleep(3)` call in `start_fucking_the_server()`. **Do not set the interval below 1.8 seconds** — the SDU course server enforces a rate limit at that threshold.

---

## Known Limitations / Notes for AI Assistants

- **No tests.** There is no test framework. Manual testing against the live server is the only validation path.
- **Recursive call on invalid course.** `start_fucking_the_server` calls itself recursively when an invalid course is detected, which can cause unbounded recursion if the user keeps entering bad input.
- **HTTP only.** The target host does not appear to support HTTPS (circa 2018). Do not silently upgrade to HTTPS without verifying server support.
- **Hard-coded host.** All URLs reference `bkjwxk.sdu.edu.cn` directly. If the university changes its domain, every URL must be updated.
- **MD5 password hashing.** MD5 is cryptographically weak; this is a constraint of the server API, not a design choice to "improve."
- **Do not add features beyond what is asked.** The script intentionally handles one course per run. Batch registration is out of scope.

---

## Git History Summary

| Commit | Message |
|---|---|
| `368ea7a` | record running time — added `time_spent()` and status print in polling loop |
| `be96f8a` | recode running time — refactored time formatting logic |
| `2d78635` | add a README :) |
| `7b3a4e1` | 1st version |
