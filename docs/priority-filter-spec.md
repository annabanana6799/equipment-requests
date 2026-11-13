# Priority Filter Feature Specification

## Goal

Help managers focus on equipment requests that need attention by showing open requests in priority order, while keeping every priority level visible.

## User Need

Managers need to see the most urgent open requests first so they can work through them without losing sight of medium- and low-priority requests. They also need a way to include closed requests when they want to review them.

## Functional Rules

- On launch, show open requests and hide closed requests.
- Provide a checkbox that managers can use to show or hide closed requests. It is unchecked by default.
- Show all three priority levels; do not remove medium- or low-priority requests from the list.
- Order requests by priority: High, then Medium, then Low.
- Within each priority, order requests by request ID in ascending order, with older request IDs first.
- When the manager checks the box, include closed requests using the same priority and request ID ordering. Unchecking it hides closed requests again.
- The checkbox changes only which requests are displayed; it does not change request data.
- If no requests match the current display setting, show a message instead of a blank list (for example, “No open requests” when there are no open requests).

## Constraints

- Use the existing request data and its priority and status fields.
- Work without a login or database.
- Preserve all existing requests and their data.

## Acceptance Criteria

1. When the app starts, only requests with status `Open` are displayed.
2. On startup, displayed requests are grouped in the order High, Medium, Low.
3. Within each priority group, request IDs appear in ascending order.
4. Every open request is displayed, including requests with Medium or Low priority.
5. Checking the closed requests checkbox displays both Open and Closed requests, in the same priority and request ID order.
6. Unchecking the checkbox hides Closed requests and leaves Open requests visible.
7. Showing or hiding Closed requests does not modify the underlying request data.
8. If there are no requests to display, such as when all requests are Closed and the checkbox is unchecked, the app displays a message such as “No open requests” instead of a blank list.

## Out of Scope

- Login or user accounts.
- A database or persistent preference storage.
- Creating, editing, or deleting requests, including changing their priority or status.
- Hiding Medium or Low requests, or adding other filters or sorting options.

## Verification Results

1. **Pass** — Manually tested by the user: launch showed only Open requests.
2. **Pass** — Manually tested by the user: priorities appeared High, Medium, then Low.
3. **Pass** — Manually tested by the user: request IDs ascended within each priority.
4. **Pass** — Manually tested by the user: Medium and Low open requests remained visible.
5. **Pass** — Manually tested by the user: checking **Show Closed** displayed Open and Closed requests in the required order.
6. **Pass** — Manually tested by the user: unchecking **Show Closed** hid Closed requests while Open requests remained visible.
7. **Pass** — `requests.json` was unchanged from the committed original before the empty-state test. Afterward, it was restored from an exact backup and its SHA-256 hash matched the original (`DF36D6F9886C9D014BC372DFDF549103526D28675230F6A910DEE8D40E3D5105`); Git also confirmed it is unchanged from `HEAD`.
8. **Pass** — Temporarily set all 10 requests to Closed, launched the app with **Show Closed** unchecked, and confirmed the app displayed “No open requests.” Restored the original request data after the app was closed.
