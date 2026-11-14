# Generated from sdks/openapi.json by `pnpm sdk:generate` — do not edit.
from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional, Union

from .._runtime import Requester, RequestOptions, _Resource, _deprecated, _pick, _seg
from .types import *  # noqa: F401,F403


class AbTestsResource(_Resource):
    """A/B tests — The stored A/B test rows of builder pages. A test reaches visitors only through the page's A/B actions (`pages.abTestAction`), which take variant B live through the publish gates; these operations create and edit drafts, read results and apply a winner to the page's draft.
    """

    def create(self, body: CreateAbTestInput, *, options: Optional[RequestOptions] = None) -> AbTest:
        """Creates an A/B test on a page, as a draft.
        
        Needs `page:update` in the page's workspace and a plan with A/B testing. The test is stored as a draft; it reaches visitors only when started from the page's A/B actions (`pages.abTestAction`).
        
        `POST /api/ab-tests`
        """
        return _pick(self._request("POST", f"/api/ab-tests", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, test_id: str, *, options: Optional[RequestOptions] = None) -> AbTestsDeleteResponse:
        """Deletes an A/B test with its recorded events and visitor sessions.
        
        Needs `page:update`.
        
        `DELETE /api/ab-tests/{testId}`
        """
        return self._request("DELETE", f"/api/ab-tests/{_seg(test_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, test_id: str, *, options: Optional[RequestOptions] = None) -> AbTest:
        """Returns one A/B test.
        
        `GET /api/ab-tests/{testId}`
        """
        return _pick(self._request("GET", f"/api/ab-tests/{_seg(test_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, page_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AbTest]:
        """Lists the A/B tests of one page, or without a page the tests the caller created.
        
        `GET /api/ab-tests`
        """
        return _pick(self._request("GET", f"/api/ab-tests", query={"pageId": page_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def promote(self, test_id: str, body: AbTestsPromoteBody, *, options: Optional[RequestOptions] = None) -> AbTestsPromoteResponseData:
        """Applies the winning variant to the page's draft and ends the test.
        
        Needs `page:update`. Variant B's live snapshot becomes the page's draft (unpublished work it replaces is filed as a version first); for A the live page already is the winner and the draft is left alone. Nothing goes live: publishing the page is a separate step.
        
        `POST /api/ab-tests/{testId}/promote`
        """
        return _pick(self._request("POST", f"/api/ab-tests/{_seg(test_id)}/promote", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, test_id: str, body: UpdateAbTestInput, *, options: Optional[RequestOptions] = None) -> AbTest:
        """Changes a draft A/B test's variants, split, goal or dates.
        
        Needs `page:update`. A test that runs or ran on the live site, or a change to `running`, answers 409 `USE_PAGE_AB_TEST`: those go through the page's A/B actions.
        
        `PUT /api/ab-tests/{testId}`
        """
        return _pick(self._request("PUT", f"/api/ab-tests/{_seg(test_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class AdsConnectionsResource(_Resource):

    def create(self, body: AdsConnectionsCreateBody, *, options: Optional[RequestOptions] = None) -> AdConnection:
        """Connects a Meta dataset or a TikTok pixel with a pasted access token.
        
        Meta needs `account.datasetId` (digits) and `credentials.accessToken`, optionally `account.testEventCode`; TikTok needs `account.pixelCode` and `credentials.accessToken`, optionally `account.offlineEventSetId`. Google Ads and LinkedIn are refused (`field: "network"`): they are connected by signing in, in the dashboard. A field that does not fit answers 400 `adConnectionInvalid` with the `field`; 403 `journeysNetworkNotOnPlan` when the network is not on the plan. The token is stored encrypted and never shown again.
        
        `POST /api/ads/connections`
        """
        return _pick(self._request("POST", f"/api/ads/connections", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> AdsConnectionsDeleteResponse:
        """Disconnects an ad account and deletes its stored credentials and delivery log.
        
        A Google refresh token is also revoked at Google. A project that named the connection keeps the id; nothing is sent to a connection that no longer exists.
        
        `DELETE /api/ads/connections/{connectionId}`
        """
        return self._request("DELETE", f"/api/ads/connections/{_seg(connection_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> List[AdConnection]:
        """Lists an organization's ad connections, without their credentials.
        
        `GET /api/ads/connections`
        """
        return _pick(self._request("GET", f"/api/ads/connections", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def test(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> AdsConnectionsTestResponseData:
        """Sends one test event through an ad connection and returns the network's answer.
        
        Meta and TikTok receive an event under the connection's test event code (Meta keeps it in the dataset like any other); Google Ads validates the request without taking it in; LinkedIn is only read. No data about any person is sent. A refused token marks the connection `error`.
        
        `POST /api/ads/connections/{connectionId}/test`
        """
        return _pick(self._request("POST", f"/api/ads/connections/{_seg(connection_id)}/test", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, connection_id: str, body: AdsConnectionsUpdateBody, *, options: Optional[RequestOptions] = None) -> AdConnection:
        """Renames an ad connection, changes its account ids, replaces its access token or switches it off and on.
        
        `account` is merged into the stored ids (an empty string removes one). A new `credentials.accessToken` replaces the stored one and clears an error; a connection made by signing in takes no pasted token. 400 `adConnectionInvalid` with the `field` that does not fit.
        
        `PATCH /api/ads/connections/{connectionId}`
        """
        return _pick(self._request("PATCH", f"/api/ads/connections/{_seg(connection_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class AdsResource(_Resource):
    """Ad connections — The ad accounts an organization reports website conversions to (Visitor Journeys): Meta, TikTok, Google Ads and LinkedIn. Every operation needs `ads:manage_connections` in the organization (its administrators by default), and the network must be on the plan. Google Ads and LinkedIn — and Meta or TikTok by sign-in — are connected in the dashboard, where the person signs in to the network.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.connections = AdsConnectionsResource(request)


class AgentsGroupsResource(_Resource):

    def create(self, body: AgentsGroupsCreateBody, *, options: Optional[RequestOptions] = None) -> AgentGroup:
        """Creates an agent group.
        
        Needs `agent:create` and the Agent Hub on the plan; counts against the plan's group limit when an `organizationId` is given.
        
        `POST /api/agents/groups`
        """
        return _pick(self._request("POST", f"/api/agents/groups", query=None, body=body, multipart=False, options=options), "group")  # type: ignore[no-any-return]

    def delete(self, group_id: str, *, options: Optional[RequestOptions] = None) -> AgentsGroupsDeleteResponse:
        """Deletes an agent group and moves its agents to the trash.
        
        Needs `agent:delete`. Refused (409) while any of its agents is started — stop them first.
        
        `DELETE /api/agents/groups/{groupId}`
        """
        return self._request("DELETE", f"/api/agents/groups/{_seg(group_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: Optional[str] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AgentGroup]:
        """Lists the agent groups the caller may see, with their member counts.
        
        `GET /api/agents/groups`
        """
        return _pick(self._request("GET", f"/api/agents/groups", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "groups")  # type: ignore[no-any-return]

    def update(self, group_id: str, body: AgentsGroupsUpdateBody, *, options: Optional[RequestOptions] = None) -> AgentGroup:
        """Renames, recolours or changes an agent group.
        
        Needs `agent:create`. Only the fields sent change.
        
        `PATCH /api/agents/groups/{groupId}`
        """
        return _pick(self._request("PATCH", f"/api/agents/groups/{_seg(group_id)}", query=None, body=body, multipart=False, options=options), "group")  # type: ignore[no-any-return]


class AgentsMemoryResource(_Resource):

    def add(self, body: AgentsMemoryAddBody, *, options: Optional[RequestOptions] = None) -> AgentsMemoryAddResponse:
        """Adds a fact to a workspace's shared memory, which every agent and the assistant read.
        
        Needs `ai_persona:manage_workspace` in that workspace. When the platform has memory switched off nothing is stored, and the answer says `stored: false`.
        
        `POST /api/agents/brain`
        """
        return self._request("POST", f"/api/agents/brain", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def forget(self, *, id: Optional[str] = None, ids: Optional[str] = None, options: Optional[RequestOptions] = None) -> float:
        """Forgets memory entries.
        
        A shared entry needs `ai_persona:manage_workspace` in its workspace; an agent's private one, the right to manage that agent. Entries the caller may not forget are left alone.
        
        `DELETE /api/agents/brain`
        """
        return _pick(self._request("DELETE", f"/api/agents/brain", query={"id": id, "ids": ids}, body=None, multipart=False, options=options), "deleted")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, workspace_id: Optional[str] = None, agent_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AgentMemoryEntry]:
        """Lists what the agents know: the workspace memory of the caller's workspaces, at most 500 entries, latest first.
        
        An agent's private notes are listed only to who may manage that agent. Personal notes are not here.
        
        `GET /api/agents/brain`
        """
        return _pick(self._request("GET", f"/api/agents/brain", query={"organizationId": organization_id, "workspaceId": workspace_id, "agentId": agent_id}, body=None, multipart=False, options=options), "entries")  # type: ignore[no-any-return]


class AgentsQuestionsResource(_Resource):

    def answer(self, question_id: str, body: AgentsQuestionsAnswerBody, *, options: Optional[RequestOptions] = None) -> Union[str, List[str], bool]:
        """Answers an agent's question, and the work goes on.
        
        Needs `agent:execute`; only the run's owner may answer. The answer's type follows the question's `kind`: text for `text`, one option value for `single`, a list for `multi`, true or false for `confirm` (a yes runs the held-back step, with the owner's access checked again). 409 when it was answered already.
        
        `POST /api/agents/questions/{questionId}`
        """
        return _pick(self._request("POST", f"/api/agents/questions/{_seg(question_id)}", query=None, body=body, multipart=False, options=options), "answer")  # type: ignore[no-any-return]

    def decline(self, question_id: str, *, options: Optional[RequestOptions] = None) -> AgentsQuestionsDeclineResponse:
        """Declines to answer, which stops the run.
        
        Needs `agent:execute`. Every open question of the run is closed and its queued and waiting tasks are cancelled.
        
        `DELETE /api/agents/questions/{questionId}`
        """
        return self._request("DELETE", f"/api/agents/questions/{_seg(question_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: Optional[str] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AgentQuestion]:
        """Lists what the agents need the caller to decide, oldest first.
        
        Needs `agent:read`. A question about a resource (a database, a project…) carries as options what the caller may choose from right now.
        
        `GET /api/agents/questions`
        """
        return _pick(self._request("GET", f"/api/agents/questions", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "questions")  # type: ignore[no-any-return]


class AgentsRunsResource(_Resource):

    def cancel(self, run_id: str, *, options: Optional[RequestOptions] = None) -> AgentsRunsCancelResponse:
        """Cancels a run that is still going.
        
        Needs `agent:execute`. Queued and waiting tasks are cancelled; a task already running finishes. 409 when the run has finished.
        
        `PATCH /api/agents/runs/{runId}`
        """
        return self._request("PATCH", f"/api/agents/runs/{_seg(run_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete(self, run_id: str, *, options: Optional[RequestOptions] = None) -> AgentsRunsDeleteResponse:
        """Deletes a finished run with its tasks, timeline and questions.
        
        Needs `agent:delete`. 409 while the run is still going — cancel it first.
        
        `DELETE /api/agents/runs/{runId}`
        """
        return self._request("DELETE", f"/api/agents/runs/{_seg(run_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, run_id: str, *, options: Optional[RequestOptions] = None) -> AgentsRunsGetResponse:
        """One run with its task tree, its timeline, its questions and the agents involved.
        
        `GET /api/agents/runs/{runId}`
        """
        return self._request("GET", f"/api/agents/runs/{_seg(run_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: Optional[str] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AgentRun]:
        """Lists the 50 latest runs the caller may see.
        
        `GET /api/agents/runs`
        """
        return _pick(self._request("GET", f"/api/agents/runs", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "runs")  # type: ignore[no-any-return]

    def retry(self, run_id: str, *, options: Optional[RequestOptions] = None) -> AgentRun:
        """Tries a finished run again: the tasks that did not succeed run again, the ones that did are kept.
        
        Needs `agent:execute`, and only the run's owner may retry it. A run that never planned anything is planned again. 409 while it is still going.
        
        `POST /api/agents/runs/{runId}/retry`
        """
        return _pick(self._request("POST", f"/api/agents/runs/{_seg(run_id)}/retry", query=None, body=None, multipart=False, options=options), "run")  # type: ignore[no-any-return]

    def start(self, body: AgentsRunsStartBody, *, options: Optional[RequestOptions] = None) -> AgentRun:
        """Starts a run: agents work towards a goal in the background.
        
        Needs `agent:execute` and the Agent Hub on the plan. A supervised run (the default) is planned by a supervisor that hands out tasks; a collaborative run (its own plan feature) lets two or more agents of one group talk in rounds. The run spends the caller's AI allowance, within `tokenBudget`.
        
        `POST /api/agents/runs`
        """
        return _pick(self._request("POST", f"/api/agents/runs", query=None, body=body, multipart=False, options=options), "run")  # type: ignore[no-any-return]


class AgentsSchedulesResource(_Resource):

    def create(self, body: AgentsSchedulesCreateBody, *, options: Optional[RequestOptions] = None) -> AgentSchedule:
        """Creates a schedule that starts a run every so many minutes.
        
        Needs `agent:execute` and the Agent Hub on the plan; counts against the plan's schedule limit when an `organizationId` is given. Its first run starts on the next tick.
        
        `POST /api/agents/schedules`
        """
        return _pick(self._request("POST", f"/api/agents/schedules", query=None, body=body, multipart=False, options=options), "schedule")  # type: ignore[no-any-return]

    def delete(self, schedule_id: str, *, options: Optional[RequestOptions] = None) -> AgentsSchedulesDeleteResponse:
        """Deletes one of the caller's schedules; runs it already started stay.
        
        `DELETE /api/agents/schedules/{scheduleId}`
        """
        return self._request("DELETE", f"/api/agents/schedules/{_seg(schedule_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AgentsSchedulesListResponseSchedulesItem]:
        """Lists the runs that start themselves: the caller's schedules, and those of the workspace named.
        
        `GET /api/agents/schedules`
        """
        return _pick(self._request("GET", f"/api/agents/schedules", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options), "schedules")  # type: ignore[no-any-return]

    def update(self, schedule_id: str, body: AgentsSchedulesUpdateBody, *, options: Optional[RequestOptions] = None) -> AgentSchedule:
        """Pauses, resumes or changes one of the caller's schedules.
        
        Needs `agent:execute`. Resuming counts against the plan's schedule limit. A changed interval counts from now.
        
        `PATCH /api/agents/schedules/{scheduleId}`
        """
        return _pick(self._request("PATCH", f"/api/agents/schedules/{_seg(schedule_id)}", query=None, body=body, multipart=False, options=options), "schedule")  # type: ignore[no-any-return]


class AgentsResource(_Resource):
    """Agents — The Agent Hub: agents that work towards a goal in the background, acting as their owner — their groups, runs, questions, schedules and shared memory.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.groups = AgentsGroupsResource(request)
        self.memory = AgentsMemoryResource(request)
        self.questions = AgentsQuestionsResource(request)
        self.runs = AgentsRunsResource(request)
        self.schedules = AgentsSchedulesResource(request)

    def activity(self, agent_id: str, *, options: Optional[RequestOptions] = None) -> AgentsActivityResponse:
        """What an agent has done: its 50 latest tasks with their results, and today's spend.
        
        Needs `agent:read`.
        
        `GET /api/agents/{agentId}/activity`
        """
        return self._request("GET", f"/api/agents/{_seg(agent_id)}/activity", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def create(self, body: AgentsCreateBody, *, options: Optional[RequestOptions] = None) -> Agent:
        """Creates an agent in a group.
        
        Needs the `agent:create` permission and the Agent Hub on the plan. The agent acts as its creator, with their access. Counts against the plan's agent limit when an `organizationId` is given.
        
        `POST /api/agents`
        """
        return _pick(self._request("POST", f"/api/agents", query=None, body=body, multipart=False, options=options), "agent")  # type: ignore[no-any-return]

    def delete(self, agent_id: str, *, options: Optional[RequestOptions] = None) -> AgentsDeleteResponse:
        """Moves an agent to the trash.
        
        Needs `agent:delete`. Its past runs keep their history. Restored from the trash, it comes back stopped.
        
        `DELETE /api/agents/{agentId}`
        """
        return self._request("DELETE", f"/api/agents/{_seg(agent_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: Optional[str] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Agent]:
        """Lists the agents the caller may use: their own, and those shared with the workspace or organisation named.
        
        `GET /api/agents`
        """
        return _pick(self._request("GET", f"/api/agents", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "agents")  # type: ignore[no-any-return]

    def queue(self, *, workspace_id: Optional[str] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AgentsQueueResponseTasksItem]:
        """Everything queued, running, waiting or stuck across the runs the caller may see, in execution order.
        
        Needs `agent:read`.
        
        `GET /api/agents/queue`
        """
        return _pick(self._request("GET", f"/api/agents/queue", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "tasks")  # type: ignore[no-any-return]

    def tools(self, *, workspace_id: str, organization_id: str, options: Optional[RequestOptions] = None) -> List[AgentsToolsResponseDataGrantsItem]:
        """What each agent grant opens: the platform tools behind it, and whether the caller could run each of them here.
        
        An agent acts as its owner, so a tool its owner cannot use (permissions, the plan, the administrator's switches) is one their agent cannot use either.
        
        `GET /api/agents/tools`
        """
        return _pick(self._request("GET", f"/api/agents/tools", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "data.grants")  # type: ignore[no-any-return]

    def update(self, agent_id: str, body: AgentsUpdateBody, *, options: Optional[RequestOptions] = None) -> Agent:
        """Changes an agent, or starts and stops it with `isActive`.
        
        Needs `agent:create`. Only the fields sent change. Stopping an agent lets a task already running finish; the next one is refused.
        
        `PATCH /api/agents/{agentId}`
        """
        return _pick(self._request("PATCH", f"/api/agents/{_seg(agent_id)}", query=None, body=body, multipart=False, options=options), "agent")  # type: ignore[no-any-return]


class AiChatsResource(_Resource):

    def create(self, body: AiChatsCreateBody, *, options: Optional[RequestOptions] = None) -> AIChat:
        """Creates an empty assistant chat in a workspace.
        
        `POST /api/ai/chats`
        """
        return _pick(self._request("POST", f"/api/ai/chats", query=None, body=body, multipart=False, options=options), "chat")  # type: ignore[no-any-return]

    def delete(self, chat_id: str, *, options: Optional[RequestOptions] = None) -> AiChatsDeleteResponse:
        """Deletes one of the caller's assistant chats and the files attached in it.
        
        `DELETE /api/ai/chats/{chatId}`
        """
        return self._request("DELETE", f"/api/ai/chats/{_seg(chat_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, chat_id: str, *, options: Optional[RequestOptions] = None) -> AiChatsGetResponse:
        """Returns one of the caller's assistant chats with its messages, oldest first.
        
        `GET /api/ai/chats/{chatId}`
        """
        return self._request("GET", f"/api/ai/chats/{_seg(chat_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> List[AIChatSummary]:
        """Lists the caller's 50 most recent assistant chats in a workspace.
        
        A chat is its owner's alone. Chats without a message are left out.
        
        `GET /api/ai/chats`
        """
        return _pick(self._request("GET", f"/api/ai/chats", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options), "chats")  # type: ignore[no-any-return]

    def rename(self, chat_id: str, body: AiChatsRenameBody, *, options: Optional[RequestOptions] = None) -> AIChatSummary:
        """Renames one of the caller's assistant chats.
        
        `PATCH /api/ai/chats/{chatId}`
        """
        return _pick(self._request("PATCH", f"/api/ai/chats/{_seg(chat_id)}", query=None, body=body, multipart=False, options=options), "chat")  # type: ignore[no-any-return]


class AiMarkingResource(_Resource):

    def export_activity(self, *, format: Optional[Literal["csv", "json"]] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the AI generations of the organizations the caller administers as a CSV or JSON file, for an audit.
        
        Same access as the activity list; at most the newest 10,000 events. Answers the file itself (`text/csv` or `application/json`). No receipt's share link, and a prompt preview only on the caller's own events.
        
        `GET /api/ai-marking/activity/export`
        """
        return self._request("GET", f"/api/ai-marking/activity/export", query={"format": format, "organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_policy(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> Literal["optional", "recommended", "required"]:
        """Returns an organization's policy for labelling AI-generated content.
        
        `optional`: unlabelled unless the person asks. `recommended`: labelled unless the person declines. `required`: always labelled. Any member may read it.
        
        `GET /api/ai-marking/policy`
        """
        return _pick(self._request("GET", f"/api/ai-marking/policy", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.policy")  # type: ignore[no-any-return]

    def list_activity(self, *, organization_id: Optional[str] = None, user_id: Optional[str] = None, kind: Optional[Literal["image", "video", "audio", "text", "transcript", "translation", "other"]] = None, marked: Optional[Literal["0", "1"]] = None, limit: Optional[int] = None, before: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AIGenerationEvent]:
        """Lists the AI generations of the organizations the caller administers, newest first — what was made, by whom, and whether it was labelled.
        
        Needs the admin or owner role in the organization (without `organizationId`, every organization the caller administers). `promptPreview` is filled only on the caller's own events. Page with `before`: the `createdAt` of the last event seen.
        
        `GET /api/ai-marking/activity`
        """
        return _pick(self._request("GET", f"/api/ai-marking/activity", query={"organizationId": organization_id, "userId": user_id, "kind": kind, "marked": marked, "limit": limit, "before": before}, body=None, multipart=False, options=options), "data.events")  # type: ignore[no-any-return]

    def set_policy(self, body: AiMarkingSetPolicyBody, *, options: Optional[RequestOptions] = None) -> Literal["optional", "recommended", "required"]:
        """Sets an organization's policy for labelling AI-generated content.
        
        Needs the admin or owner role in the organization.
        
        `PUT /api/ai-marking/policy`
        """
        return _pick(self._request("PUT", f"/api/ai-marking/policy", query=None, body=body, multipart=False, options=options), "data.policy")  # type: ignore[no-any-return]


class AiPersonasResource(_Resource):

    def clear(self, *, options: Optional[RequestOptions] = None) -> AiPersonasClearResponse:
        """Removes the caller's own assistant persona.
        
        `DELETE /api/ai/personas`
        """
        return self._request("DELETE", f"/api/ai/personas", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def clear_organization(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> AiPersonasClearOrganizationResponse:
        """Removes an organization's assistant persona.
        
        Needs `ai_persona.manage_organization` in the organization.
        
        `DELETE /api/ai/personas/organization/{organizationId}`
        """
        return self._request("DELETE", f"/api/ai/personas/organization/{_seg(organization_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def clear_workspace(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> AiPersonasClearWorkspaceResponse:
        """Removes a workspace's assistant persona.
        
        Needs `ai_persona.manage_workspace` in the workspace.
        
        `DELETE /api/ai/personas/workspace/{workspaceId}`
        """
        return self._request("DELETE", f"/api/ai/personas/workspace/{_seg(workspace_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def derive_from_samples(self, body: AiPersonasDeriveFromSamplesBody, *, options: Optional[RequestOptions] = None) -> AIDerivedPersona:
        """Derives a brand voice — persona fields — from 3 to 15 samples of the organization's writing.
        
        Needs the `brand_voice_trainer` feature and `ai_persona.manage_organization` in the organization. Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. Saves nothing: apply the result with PUT /api/ai/personas/organization/{organizationId}. Samples shorter than 20 characters are ignored; each is read up to 4,000.
        
        `POST /api/ai/persona/from-samples`
        """
        return _pick(self._request("POST", f"/api/ai/persona/from-samples", query=None, body=body, multipart=False, options=options), "data.persona")  # type: ignore[no-any-return]

    def get(self, *, options: Optional[RequestOptions] = None) -> AIPersona:
        """Returns the caller's own assistant persona, or null.
        
        `GET /api/ai/personas`
        """
        return _pick(self._request("GET", f"/api/ai/personas", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_organization(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> AIPersona:
        """Returns an organization's assistant persona, or null.
        
        Needs `ai_persona.manage_organization` in the organization.
        
        `GET /api/ai/personas/organization/{organizationId}`
        """
        return _pick(self._request("GET", f"/api/ai/personas/organization/{_seg(organization_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_workspace(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> AIPersona:
        """Returns a workspace's assistant persona, or null.
        
        Needs `ai_persona.manage_workspace` in the workspace.
        
        `GET /api/ai/personas/workspace/{workspaceId}`
        """
        return _pick(self._request("GET", f"/api/ai/personas/workspace/{_seg(workspace_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def preview(self, body: AiPersonasPreviewBody, *, options: Optional[RequestOptions] = None) -> str:
        """Answers a prompt in the voice of a persona that is not saved yet, to try it before rolling it out.
        
        Needs the `brand_voice_trainer` feature and `ai_persona.manage_organization` in the organization. Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up.
        
        `POST /api/ai/persona/preview`
        """
        return _pick(self._request("POST", f"/api/ai/persona/preview", query=None, body=body, multipart=False, options=options), "data.reply")  # type: ignore[no-any-return]

    def set(self, body: AIPersonaInput, *, options: Optional[RequestOptions] = None) -> AIPersona:
        """Saves the caller's own assistant persona — who they are, their work, tone, reply length and format.
        
        `PUT /api/ai/personas`
        """
        return _pick(self._request("PUT", f"/api/ai/personas", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_organization(self, organization_id: str, body: AISharedPersonaInput, *, options: Optional[RequestOptions] = None) -> AIPersona:
        """Saves an organization's assistant persona.
        
        Needs `ai_persona.manage_organization` in the organization.
        
        `PUT /api/ai/personas/organization/{organizationId}`
        """
        return _pick(self._request("PUT", f"/api/ai/personas/organization/{_seg(organization_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_workspace(self, workspace_id: str, body: AISharedPersonaInput, *, options: Optional[RequestOptions] = None) -> AIPersona:
        """Saves a workspace's assistant persona.
        
        Needs `ai_persona.manage_workspace` in the workspace.
        
        `PUT /api/ai/personas/workspace/{workspaceId}`
        """
        return _pick(self._request("PUT", f"/api/ai/personas/workspace/{_seg(workspace_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class AiReceiptsResource(_Resource):

    def get(self, receipt_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> AIReceipt:
        """Returns one receipt of an AI generation.
        
        Needs the `ai_receipts` feature. The caller's own, or any of the organization's with `ai_usage.view_all` there; anything else answers 404.
        
        `GET /api/ai/receipts/{receiptId}`
        """
        return _pick(self._request("GET", f"/api/ai/receipts/{_seg(receipt_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "receipt")  # type: ignore[no-any-return]

    def list(self, *, scope: Optional[Literal["own", "org"]] = None, organization_id: Optional[str] = None, kind: Optional[str] = None, surface: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[AIReceipt]:
        """Lists the receipts of AI generations — the caller's own, or a whole organization's.
        
        Needs the `ai_receipts` feature. `scope=org` needs `organizationId` and `ai_usage.view_all` there.
        
        `GET /api/ai/receipts`
        """
        return _pick(self._request("GET", f"/api/ai/receipts", query={"scope": scope, "organizationId": organization_id, "kind": kind, "surface": surface, "limit": limit}, body=None, multipart=False, options=options), "receipts")  # type: ignore[no-any-return]

    def share(self, receipt_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> AiReceiptsShareResponse:
        """Makes a public link token for a receipt, or returns the one it has.
        
        Same access as reading the receipt. Anyone with the token can read the receipt (without the token itself) until it is revoked.
        
        `POST /api/ai/receipts/{receiptId}/share`
        """
        return self._request("POST", f"/api/ai/receipts/{_seg(receipt_id)}/share", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def unshare(self, receipt_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> AiReceiptsUnshareResponse:
        """Revokes a receipt's public link.
        
        `DELETE /api/ai/receipts/{receiptId}/share`
        """
        return self._request("DELETE", f"/api/ai/receipts/{_seg(receipt_id)}/share", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class AiSkillsResource(_Resource):

    def add_template(self, body: AiSkillsAddTemplateBody, *, options: Optional[RequestOptions] = None) -> AISkill:
        """Adds a built-in template as a skill, in the caller's language.
        
        Without a level it becomes the caller's own skill, switched on. At a workspace or organization it needs that level's manage permission, and starts approved only for somebody who may approve there. Once per template and level: a second add answers 409 `alreadyAdded` with the existing skill's id.
        
        `POST /api/ai/skills/templates`
        """
        return _pick(self._request("POST", f"/api/ai/skills/templates", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def approve(self, skill_id: str, body: AiSkillsApproveBody, *, options: Optional[RequestOptions] = None) -> AISkill:
        """Approves and switches on, or rejects and switches off, a workspace's or organization's skill.
        
        Needs `ai_skill.approve` in the skill's own workspace or organization. A person's own skill needs no approval (400).
        
        `POST /api/ai/skills/{skillId}/approve`
        """
        return _pick(self._request("POST", f"/api/ai/skills/{_seg(skill_id)}/approve", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: AICreateSkillInput, *, options: Optional[RequestOptions] = None) -> AISkill:
        """Creates an assistant skill of the caller's own.
        
        `POST /api/ai/skills`
        """
        return _pick(self._request("POST", f"/api/ai/skills", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_organization(self, organization_id: str, body: AICreateSharedSkillInput, *, options: Optional[RequestOptions] = None) -> AISkill:
        """Creates an assistant skill shared with an organization.
        
        Needs `ai_skill.manage_organization` in the organization. It starts approved and on for somebody with `ai_skill.approve` there, pending and off otherwise.
        
        `POST /api/ai/skills/organization/{organizationId}`
        """
        return _pick(self._request("POST", f"/api/ai/skills/organization/{_seg(organization_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_workspace(self, workspace_id: str, body: AICreateSharedSkillInput, *, options: Optional[RequestOptions] = None) -> AISkill:
        """Creates an assistant skill shared with a workspace.
        
        Needs `ai_skill.manage_workspace` in the workspace. It starts approved and on for somebody with `ai_skill.approve` there, pending and off otherwise.
        
        `POST /api/ai/skills/workspace/{workspaceId}`
        """
        return _pick(self._request("POST", f"/api/ai/skills/workspace/{_seg(workspace_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, skill_id: str, *, options: Optional[RequestOptions] = None) -> AiSkillsDeleteResponse:
        """Deletes an assistant skill.
        
        `DELETE /api/ai/skills/{skillId}`
        """
        return self._request("DELETE", f"/api/ai/skills/{_seg(skill_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, skill_id: str, *, options: Optional[RequestOptions] = None) -> AISkill:
        """Returns one assistant skill.
        
        The caller's own skill, or a workspace's or organization's skill where the caller manages that level's skills.
        
        `GET /api/ai/skills/{skillId}`
        """
        return _pick(self._request("GET", f"/api/ai/skills/{_seg(skill_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, options: Optional[RequestOptions] = None) -> List[AISkill]:
        """Lists the caller's own assistant skills, most recently changed first.
        
        `GET /api/ai/skills`
        """
        return _pick(self._request("GET", f"/api/ai/skills", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_organization(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> List[AISkill]:
        """Lists an organization's shared assistant skills.
        
        Needs `ai_skill.manage_organization` in the organization.
        
        `GET /api/ai/skills/organization/{organizationId}`
        """
        return _pick(self._request("GET", f"/api/ai/skills/organization/{_seg(organization_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_templates(self, *, workspace_id: Optional[str] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AiSkillsListTemplatesResponseDataItem]:
        """Lists the built-in skill templates and which of them were already added.
        
        Without a level, as the caller's own skills; with `workspaceId` or `organizationId` (one of them), at that level, which needs its manage permission there.
        
        `GET /api/ai/skills/templates`
        """
        return _pick(self._request("GET", f"/api/ai/skills/templates", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_tools(self, *, workspace_id: str, organization_id: str, options: Optional[RequestOptions] = None) -> List[AiSkillsListToolsResponseDataHubsItem]:
        """Lists, by hub, the assistant tools the caller may use in a workspace — what a skill may suggest.
        
        `GET /api/ai/skills/tools`
        """
        return _pick(self._request("GET", f"/api/ai/skills/tools", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "data.hubs")  # type: ignore[no-any-return]

    def list_workspace(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> List[AISkill]:
        """Lists a workspace's shared assistant skills.
        
        Needs `ai_skill.manage_workspace` in the workspace.
        
        `GET /api/ai/skills/workspace/{workspaceId}`
        """
        return _pick(self._request("GET", f"/api/ai/skills/workspace/{_seg(workspace_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_override(self, skill_id: str, body: AiSkillsSetOverrideBody, *, options: Optional[RequestOptions] = None) -> AiSkillsSetOverrideResponseData:
        """Switches an inherited workspace or organization skill off, or back on, for the caller alone.
        
        Refused (403) for a skill its level enforces.
        
        `PUT /api/ai/skills/{skillId}/override`
        """
        return _pick(self._request("PUT", f"/api/ai/skills/{_seg(skill_id)}/override", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, skill_id: str, body: AIUpdateSkillInput, *, options: Optional[RequestOptions] = None) -> AISkill:
        """Changes an assistant skill.
        
        The caller's own skill, or a shared one where the caller manages that level's skills. An edit of a shared skill by somebody who may not approve there sends it back for approval; switching a shared skill on or off is POST /api/ai/skills/{skillId}/approve.
        
        `PATCH /api/ai/skills/{skillId}`
        """
        return _pick(self._request("PATCH", f"/api/ai/skills/{_seg(skill_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class AiVideoResource(_Resource):

    def create(self, body: AiVideoCreateBody, *, options: Optional[RequestOptions] = None) -> AiVideoCreateResponse:
        """Starts a video or GIF generation job and answers its id.
        
        The job runs in the background; poll GET /api/ai/video/{jobId}. The duration is capped at the platform's maximum. `screenshot-walkthrough` needs a public `url` and captures it step by step. Plan limits and the platform's video settings apply.
        
        `POST /api/ai/video`
        """
        return self._request("POST", f"/api/ai/video", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, job_id: str, *, options: Optional[RequestOptions] = None) -> AIVideoJob:
        """Returns a video generation job's status and, once complete, its result.
        
        The caller's own job, or one made for an organization they belong to; any other id answers 404.
        
        `GET /api/ai/video/{jobId}`
        """
        return self._request("GET", f"/api/ai/video/{_seg(job_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class AiResource(_Resource):
    """AI — The platform's AI: generating and checking content, the assistant's chats, personas and skills, the receipts of what was generated, and the organization's AI-labelling policy and activity. Every generation counts against the organization's AI quota on its plan.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.chats = AiChatsResource(request)
        self.marking = AiMarkingResource(request)
        self.personas = AiPersonasResource(request)
        self.receipts = AiReceiptsResource(request)
        self.skills = AiSkillsResource(request)
        self.video = AiVideoResource(request)

    def analyze_image(self, body: AiAnalyzeImageBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Describes an image and derives a colour palette, light and dark website themes, fonts and design suggestions from it.
        
        Needs image AI on the organization's plan. Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. The image is fetched from `imageUrl`; the same route also takes a multipart form with `file` (JPEG, PNG, WebP or GIF, 10 MB at most), `organizationId` and `focus`. The analysis is the AI's answer: its fields (`description`, `mood`, `colors`, `palette`, `darkPalette`, `typography`, `designSuggestions`) are asked for but not guaranteed.
        
        `POST /api/ai/analyze-image`
        """
        return _pick(self._request("POST", f"/api/ai/analyze-image", query=None, body=body, multipart=False, options=options), "analysis")  # type: ignore[no-any-return]

    def analyze_url(self, body: AiAnalyzeUrlBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Reads a public web page and describes its sections, colours, fonts and content, to recreate or take inspiration from it.
        
        Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. Only public pages are fetched (3 MB at most). The analysis is the AI's answer: its fields (`title`, `description`, `pageType`, `layout`, `sections`, `colors`, `darkColors`, `fonts`, `content`, `designNotes`) are asked for but not guaranteed.
        
        `POST /api/ai/analyze-url`
        """
        return _pick(self._request("POST", f"/api/ai/analyze-url", query=None, body=body, multipart=False, options=options), "analysis")  # type: ignore[no-any-return]

    def bulk_operation(self, body: AiBulkOperationBody, *, options: Optional[RequestOptions] = None) -> AiBulkOperationResponseData:
        """Rewrites or translates every text of a page's component tree at once and answers the changed tree.
        
        Needs `project.create`. Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. Off when the platform administrator switched bulk operations off (403). Nothing is saved: the tree comes back for the caller to store.
        
        `POST /api/ai/bulk-operations`
        """
        return _pick(self._request("POST", f"/api/ai/bulk-operations", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def check_accessibility(self, body: AiCheckAccessibilityBody, *, options: Optional[RequestOptions] = None) -> AIAccessibilityReport:
        """Checks a page's component tree for accessibility problems and answers the issues with WCAG criteria and fixes.
        
        Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. Off when the platform administrator switched the checker off (403).
        
        `POST /api/ai/accessibility-check`
        """
        return _pick(self._request("POST", f"/api/ai/accessibility-check", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def component_action(self, body: AiComponentActionBody, *, options: Optional[RequestOptions] = None) -> AiComponentActionResponse:
        """Rewrites, generates or improves the content of one builder component, or suggests a layout for it.
        
        Answers only the props that changed, to merge into the component. Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. Off when the platform administrator switched component actions off (403). With a `projectId` the caller may read, the project's facts and tone go into the copy operations.
        
        `POST /api/ai/component`
        """
        return self._request("POST", f"/api/ai/component", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def generate_content(self, body: AiGenerateContentBody, *, options: Optional[RequestOptions] = None) -> AiGenerateContentResponseData:
        """Writes text from a prompt — a headline, a description, a post — in the requested format, tone and length.
        
        Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. Off when the platform administrator switched content generation off (403). With a `projectId` the caller may read, the project's facts, avoided words and tone go into the prompt. The organization's AI-labelling policy decides whether a visible "generated with AI" line is added (`marked`); `markAsAi` chooses where the policy lets the person choose.
        
        `POST /api/ai/generate-content`
        """
        return _pick(self._request("POST", f"/api/ai/generate-content", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def generate_image(self, body: AiGenerateImageBody, *, options: Optional[RequestOptions] = None) -> AiGenerateImageResponseData:
        """Generates an image from a prompt and keeps it as an asset of the organization.
        
        Needs `asset.ai_generate` and `asset.create` in the organization, image generation on its plan and room in its storage; counts against its image quota. The image lands in the asset library with the organization's default visibility; `url` is the asset's own.
        
        `POST /api/ai/generate-image`
        """
        return _pick(self._request("POST", f"/api/ai/generate-image", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def generate_project(self, body: AiGenerateProjectBody, *, options: Optional[RequestOptions] = None) -> AiGenerateProjectResponseData:
        """Builds a whole project from a description — its pages, and the databases and endpoints it needs.
        
        Needs `project.create`; the workspace must belong to the organization. Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. Plans the project, then generates page by page, and answers when everything is made — this can take minutes. Pages that could not be made are listed in `errors`; the rest of the project stays.
        
        `POST /api/ai/generate-project`
        """
        return _pick(self._request("POST", f"/api/ai/generate-project", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def generate_seo(self, body: AiGenerateSeoBody, *, options: Optional[RequestOptions] = None) -> AiGenerateSeoResponseData:
        """Suggests a meta title, a meta description and keywords for a page.
        
        Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. Off when the platform administrator switched SEO generation off (403).
        
        `POST /api/ai/generate-seo`
        """
        return _pick(self._request("POST", f"/api/ai/generate-seo", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_time_saved(self, *, days: Optional[int] = None, options: Optional[RequestOptions] = None) -> AITimeSavedReport:
        """Estimates the time the caller's own AI actions saved, per surface and per month.
        
        `GET /api/ai/time-saved`
        """
        return self._request("GET", f"/api/ai/time-saved", query={"days": days}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_usage(self, *, organization_id: Optional[str] = None, user_id: Optional[str] = None, days: Optional[int] = None, options: Optional[RequestOptions] = None) -> AIUsageRollup:
        """Returns AI usage per day and per surface, for the caller or for an organization.
        
        Without `organizationId` (or with `userId`) it is the caller's own usage. `organizationId` alone is the whole organization's and needs `ai_usage:view` there; with `userId` as well, that member's usage in that organization (same permission).
        
        `GET /api/ai/usage`
        """
        return _pick(self._request("GET", f"/api/ai/usage", query={"organizationId": organization_id, "userId": user_id, "days": days}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def query_databases(self, body: AiQueryDatabasesBody, *, options: Optional[RequestOptions] = None) -> AiQueryDatabasesResponseData:
        """Answers a question in plain language over the organization's databases the caller may read, as figures ready for a chart.
        
        Answers 503 `aiNotConfigured` when the platform has no AI configured, 403 when the person opted out of AI processing (Settings → Privacy), and 429 when the organization's AI quota is used up. The AI picks one database and a filter, grouping and aggregation; the platform runs it with the caller's row permissions. `truncated` says only the first `cap` records were counted.
        
        `POST /api/ai/db-query`
        """
        return _pick(self._request("POST", f"/api/ai/db-query", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def rewrite_document_text(self, body: AiRewriteDocumentTextBody, *, options: Optional[RequestOptions] = None) -> str:
        """Improves, shortens, expands, corrects, continues, summarizes or translates a selection from a document page.
        
        Needs `document.update` and edit access to the document, AI switched on for the document and for the workspace. Refused on vault and restricted pages and for a selection containing text marked sensitive. 20 calls a minute per person. Nothing is saved: the text comes back for the caller to place.
        
        `POST /api/ai/documents/rewrite`
        """
        return _pick(self._request("POST", f"/api/ai/documents/rewrite", query=None, body=body, multipart=False, options=options), "text")  # type: ignore[no-any-return]

    def subtitles(self, body: AiSubtitlesBody, *, options: Optional[RequestOptions] = None) -> List[Any]:
        """Polishes or translates subtitle cues, keeping their timings, or finds chapter markers in them.
        
        Needs `asset.record_video`, video recording on the organization's plan and the `video:ai_subtitles` feature. `polish` and `translate` answer the cues; `chapters` answers 3 to 8 `{ time, title }` markers, the first at 0.
        
        `POST /api/ai/subtitles`
        """
        return _pick(self._request("POST", f"/api/ai/subtitles", query=None, body=body, multipart=False, options=options), "result")  # type: ignore[no-any-return]


class AnalyticsResource(_Resource):
    """Analytics — Visitor events of builder pages: recording them from a page, the click and scroll heatmaps they make, and refreshing the daily summaries the dashboards read.
    """

    def aggregate(self, *, project_id: Optional[str] = None, date: Optional[str] = None, days: Optional[int] = None, options: Optional[RequestOptions] = None) -> AnalyticsAggregateResponse:
        """Recomputes a project's daily page and project summaries from its recorded events.
        
        Without `date` or `days`, today. Without `projectId` only a platform administrator may run it. The answer counts the summaries written.
        
        `POST /api/analytics/aggregate`
        """
        return self._request("POST", f"/api/analytics/aggregate", query={"projectId": project_id, "date": date, "days": days}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def heatmap(self, *, page_id: str, type_: Optional[Literal["click", "scroll"]] = None, days: Optional[int] = None, options: Optional[RequestOptions] = None) -> Union[AnalyticsHeatmapResponseData, AnalyticsHeatmapResponseData2]:
        """Returns a page's click or scroll heatmap for a period.
        
        Clicks come as normalised `[x, y, count]` points on a 200×200 grid plus clicks per component; scrolls as ten depth bands with the visitors who reached each.
        
        `GET /api/analytics/heatmap`
        """
        return _pick(self._request("GET", f"/api/analytics/heatmap", query={"pageId": page_id, "type": type_, "days": days}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def track(self, body: AnalyticsEvent, *, options: Optional[RequestOptions] = None) -> AnalyticsTrackResponse:
        """Records a visitor event on a page.
        
        Needs no token: published pages call it. Limited to 120 events a minute per address (beyond that it answers 204 and drops the event); while the platform's analytics are off it answers success and records nothing.
        
        `POST /api/analytics/track` — No token needed.
        """
        return self._request("POST", f"/api/analytics/track", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class AnnouncementsResource(_Resource):
    """Announcements
    """

    def dismiss(self, id: str, *, options: Optional[RequestOptions] = None) -> AnnouncementsDismissResponseData:
        """Dismisses an announcement for the caller.
        
        Dismissing it twice is harmless (`alreadyDismissed: true`).
        
        `POST /api/announcements/{id}/dismiss`
        """
        return _pick(self._request("POST", f"/api/announcements/{_seg(id)}/dismiss", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_active(self, *, options: Optional[RequestOptions] = None) -> List[Announcement]:
        """Lists the platform's announcements that are live now and addressed to the caller.
        
        Only announcements within their time window and whose audience includes the caller, dismissed ones too (`dismissed: true`). Pinned first, then by priority, then newest.
        
        `GET /api/announcements/active`
        """
        return _pick(self._request("GET", f"/api/announcements/active", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ApprovalsResource(_Resource):
    """Approvals
    """

    def approve(self, approval_id: str, body: ApprovalsApproveBody, *, options: Optional[RequestOptions] = None) -> Approval:
        """Approves the current step of an approval as the caller.
        
        When the last step is approved the approval completes, and what it was for takes effect (a page publish, for instance).
        
        `POST /api/approvals/{approvalId}/approve`
        """
        return _pick(self._request("POST", f"/api/approvals/{_seg(approval_id)}/approve", query=None, body=body, multipart=False, options=options), "data.workflow")  # type: ignore[no-any-return]

    def bulk(self, body: ApprovalsBulkBody, *, options: Optional[RequestOptions] = None) -> List[ApprovalsBulkResponseDataResultsItem]:
        """Approves, rejects or cancels up to 50 approvals at once.
        
        Each approval is decided on its own; `results` says which worked.
        
        `POST /api/approvals/bulk`
        """
        return _pick(self._request("POST", f"/api/approvals/bulk", query=None, body=body, multipart=False, options=options), "data.results")  # type: ignore[no-any-return]

    def cancel(self, approval_id: str, *, options: Optional[RequestOptions] = None) -> ApprovalsCancelResponse:
        """Cancels a pending approval.
        
        Only its requester or an administrator can cancel it.
        
        `DELETE /api/approvals/{approvalId}`
        """
        return self._request("DELETE", f"/api/approvals/{_seg(approval_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def create(self, body: CreateApprovalInput, *, options: Optional[RequestOptions] = None) -> Approval:
        """Requests an approval of something — a page, project, asset, workflow, row — from the given approvers.
        
        The approvers of the first step are notified.
        
        `POST /api/approvals`
        """
        return _pick(self._request("POST", f"/api/approvals", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_delegation(self, body: ApprovalsCreateDelegationBody, *, options: Optional[RequestOptions] = None) -> ApprovalDelegation:
        """Lets another member decide the caller's approvals of an organization, for a period.
        
        `POST /api/approvals/delegations`
        """
        return _pick(self._request("POST", f"/api/approvals/delegations", query=None, body=body, multipart=False, options=options), "data.delegation")  # type: ignore[no-any-return]

    def delete_delegation(self, *, id: str, options: Optional[RequestOptions] = None) -> ApprovalsDeleteDelegationResponse:
        """Ends one of the caller's approval delegations.
        
        `DELETE /api/approvals/delegations`
        """
        return self._request("DELETE", f"/api/approvals/delegations", query={"id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, approval_id: str, *, options: Optional[RequestOptions] = None) -> Approval:
        """Returns one approval with its steps and approvers.
        
        `GET /api/approvals/{approvalId}`
        """
        return _pick(self._request("GET", f"/api/approvals/{_seg(approval_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_settings(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> ApprovalsGetSettingsResponseData:
        """Returns an organization's approval settings: whether publishing needs approval and who approves.
        
        `GET /api/approvals/settings`
        """
        return _pick(self._request("GET", f"/api/approvals/settings", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def history(self, approval_id: str, *, options: Optional[RequestOptions] = None) -> List[ApprovalHistoryEntry]:
        """Lists what happened to an approval — requested, approved, rejected, cancelled — oldest first.
        
        `GET /api/approvals/{approvalId}/history`
        """
        return _pick(self._request("GET", f"/api/approvals/{_seg(approval_id)}/history", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, status: Optional[Literal["pending", "approved", "rejected", "cancelled"]] = None, entity_type: Optional[Literal["project", "page", "asset", "database", "endpoint", "workflow", "databaseRow", "documentPage", "report", "social_post", "mailThread"]] = None, filter: Optional[Literal["pending", "requested", "all"]] = None, organization_id: Optional[str] = None, workspace_id: Optional[str] = None, search: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Approval]:
        """Lists the approvals the caller may see.
        
        An approval with strict visibility is listed only to its requester and its approvers.
        
        `GET /api/approvals`
        """
        return _pick(self._request("GET", f"/api/approvals", query={"status": status, "entityType": entity_type, "filter": filter, "organizationId": organization_id, "workspaceId": workspace_id, "search": search, "page": page, "limit": limit}, body=None, multipart=False, options=options), "workflows")  # type: ignore[no-any-return]

    def list_delegations(self, *, options: Optional[RequestOptions] = None) -> List[ApprovalDelegation]:
        """Lists the approval delegations from or to the caller.
        
        `GET /api/approvals/delegations`
        """
        return _pick(self._request("GET", f"/api/approvals/delegations", query=None, body=None, multipart=False, options=options), "data.delegations")  # type: ignore[no-any-return]

    def reject(self, approval_id: str, body: ApprovalsRejectBody, *, options: Optional[RequestOptions] = None) -> Union[Approval, ApprovalsRejectResponseData2]:
        """Rejects an approval as the caller, with a reason.
        
        `POST /api/approvals/{approvalId}/reject`
        """
        return _pick(self._request("POST", f"/api/approvals/{_seg(approval_id)}/reject", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, approval_id: str, body: ApprovalsUpdateBody, *, options: Optional[RequestOptions] = None) -> Approval:
        """Changes an approval's title, description, priority or due date.
        
        The status changes only through approve, reject or cancel; sending `status` is refused.
        
        `PATCH /api/approvals/{approvalId}`
        """
        return _pick(self._request("PATCH", f"/api/approvals/{_seg(approval_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_settings(self, body: ApprovalsUpdateSettingsBody, *, options: Optional[RequestOptions] = None) -> ApprovalsUpdateSettingsResponse:
        """Changes an organization's approval settings.
        
        Organization administrators only. Name approvers by people or by roles, not both.
        
        `PUT /api/approvals/settings`
        """
        return self._request("PUT", f"/api/approvals/settings", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class AppsBuildsResource(_Resource):

    def create(self, publication_id: str, body: AppsBuildsCreateBody, *, options: Optional[RequestOptions] = None) -> AppBuild:
        """Queues a native build of a publication for one platform.
        
        Needs `project:publish_native`, the plan's native builds and a verified email; the plan's builds per month and artifact storage apply. Poll `apps.builds.list` for its status.
        
        `POST /api/apps/publications/{publicationId}/builds`
        """
        return _pick(self._request("POST", f"/api/apps/publications/{_seg(publication_id)}/builds", query=None, body=body, multipart=False, options=options), "data.build")  # type: ignore[no-any-return]

    def delete(self, build_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> AppsBuildsDeleteResponseData:
        """Cancels a queued or running build, or deletes a finished one with its file.
        
        `DELETE /api/apps/builds/{buildId}`
        """
        return _pick(self._request("DELETE", f"/api/apps/builds/{_seg(build_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def download(self, build_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a completed build's installer or package.
        
        Answers the file itself (`.dmg`, `.msi`, `.apk`, …), not JSON; the header `X-Content-Sha256` carries its hash. 400 while the build is not completed, 410 once its file expired.
        
        `GET /api/apps/builds/{buildId}/download`
        """
        return self._request("GET", f"/api/apps/builds/{_seg(build_id)}/download", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, publication_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> List[AppBuild]:
        """Lists a publication's builds, newest first.
        
        At most 50.
        
        `GET /api/apps/publications/{publicationId}/builds`
        """
        return _pick(self._request("GET", f"/api/apps/publications/{_seg(publication_id)}/builds", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.builds")  # type: ignore[no-any-return]

    def update(self, build_id: str, body: AppsBuildsUpdateBody, *, options: Optional[RequestOptions] = None) -> AppsBuildsUpdateResponse:
        """Sets a build's release notes.
        
        `PATCH /api/apps/builds/{buildId}`
        """
        return self._request("PATCH", f"/api/apps/builds/{_seg(build_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class AppsPublicationsResource(_Resource):

    def create(self, body: AppsPublicationsCreateBody, *, options: Optional[RequestOptions] = None) -> AppPublication:
        """Creates the app of a project or of a hub.
        
        Give exactly one of `projectId` (needs `project:publish_pwa`) and `hubKey` (needs `organization:manage_hub_apps`); a project or a hub has at most one publication (409). Needs a verified email; counts against the plan's `max_app_publications`.
        
        `POST /api/apps/publications`
        """
        return _pick(self._request("POST", f"/api/apps/publications", query=None, body=body, multipart=False, options=options), "data.publication")  # type: ignore[no-any-return]

    def delete(self, publication_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> AppsPublicationsDeleteResponse:
        """Deletes an app publication and its builds.
        
        `DELETE /api/apps/publications/{publicationId}`
        """
        return self._request("DELETE", f"/api/apps/publications/{_seg(publication_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, publication_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> AppPublication:
        """Returns one app publication.
        
        `GET /api/apps/publications/{publicationId}`
        """
        return _pick(self._request("GET", f"/api/apps/publications/{_seg(publication_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.publication")  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> List[AppPublication]:
        """Lists an organization's app publications, most recently changed first.
        
        At most 50.
        
        `GET /api/apps/publications`
        """
        return _pick(self._request("GET", f"/api/apps/publications", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.publications")  # type: ignore[no-any-return]

    def update(self, publication_id: str, body: AppsPublicationsUpdateBody, *, options: Optional[RequestOptions] = None) -> AppPublication:
        """Changes an app publication's name, look, version or channels.
        
        Only the fields sent change. Turning on `desktopEnabled` or `mobileEnabled` needs the plan's native builds.
        
        `PATCH /api/apps/publications/{publicationId}`
        """
        return _pick(self._request("PATCH", f"/api/apps/publications/{_seg(publication_id)}", query=None, body=body, multipart=False, options=options), "data.publication")  # type: ignore[no-any-return]


class AppsSigningCredentialsResource(_Resource):

    def create(self, body: AppsSigningCredentialsCreateBody, *, options: Optional[RequestOptions] = None) -> AppsSigningCredentialsCreateResponseDataCredential:
        """Stores signing material for native builds, encrypted.
        
        Needs `organization:manage_signing_credentials` and the plan's store submission. `blob` is the material, laid out per platform as the build runner reads it; binary files (.p12, .jks, .pfx, .mobileprovision) base64-encoded:
        
        - `apple`: `teamId`, `appStoreConnectKeyId`, `appStoreConnectIssuerId`, `apiKeyP8`, `distributionCertP12`, `distributionCertPassword`, `provisioningProfile`, `autoSubmitAfterBuild`
        - `google`: `serviceAccountJson`, `keystoreJks`, `keystorePassword`, `keyAlias`, `keyPassword`, `packageName`, `appSigningSha256`, `submitTrack`, `autoSubmitAfterBuild`
        - `macos-developer-id`: `developerIdCertP12`, `developerIdCertPassword`, `signingIdentity`, `teamId`, `appleId`, `appSpecificPassword`
        - `windows-authenticode`: `codeSigningPfx`, `codeSigningPfxPassword`, `timestampUrl`
        
        `POST /api/apps/signing-credentials`
        """
        return _pick(self._request("POST", f"/api/apps/signing-credentials", query=None, body=body, multipart=False, options=options), "data.credential")  # type: ignore[no-any-return]

    def delete(self, credential_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> AppsSigningCredentialsDeleteResponse:
        """Deletes a signing credential.
        
        Needs `organization:manage_signing_credentials`.
        
        `DELETE /api/apps/signing-credentials/{credentialId}`
        """
        return self._request("DELETE", f"/api/apps/signing-credentials/{_seg(credential_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> List[AppSigningCredential]:
        """Lists an organization's signing credentials, without their secrets.
        
        `GET /api/apps/signing-credentials`
        """
        return _pick(self._request("GET", f"/api/apps/signing-credentials", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.credentials")  # type: ignore[no-any-return]


class AppsResource(_Resource):
    """Apps — A project's or a hub's own installable app (PWA) and its native desktop and mobile builds.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.builds = AppsBuildsResource(request)
        self.publications = AppsPublicationsResource(request)
        self.signing_credentials = AppsSigningCredentialsResource(request)


class AssetFoldersResource(_Resource):
    """File folders
    """

    def create(self, body: CreateAssetFolderInput, *, options: Optional[RequestOptions] = None) -> AssetFolder:
        """Creates a file folder.
        
        `POST /api/asset-folders` — Token permission: `write:assets`.
        """
        return _pick(self._request("POST", f"/api/asset-folders", query=None, body=body, multipart=False, options=options), "folder")  # type: ignore[no-any-return]

    def delete(self, folder_id: str, *, options: Optional[RequestOptions] = None) -> AssetFoldersDeleteResponse:
        """Deletes a file folder and moves its files to the trash.
        
        Refused while the folder has subfolders, and when the caller may not delete every file in it. The folder's shares are removed.
        
        `DELETE /api/asset-folders/{folderId}` — Token permission: `write:assets`.
        """
        return self._request("DELETE", f"/api/asset-folders/{_seg(folder_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AssetFolder]:
        """Lists the file folders of an organization the caller may see.
        
        `GET /api/asset-folders` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/asset-folders", query={"organizationId": organization_id, "workspaceId": workspace_id}, body=None, multipart=False, options=options), "folders")  # type: ignore[no-any-return]

    def update(self, folder_id: str, body: UpdateAssetFolderInput, *, options: Optional[RequestOptions] = None) -> AssetFolder:
        """Renames a file folder, moves it, or changes its visibility.
        
        `PATCH /api/asset-folders/{folderId}` — Token permission: `write:assets`.
        """
        return _pick(self._request("PATCH", f"/api/asset-folders/{_seg(folder_id)}", query=None, body=body, multipart=False, options=options), "folder")  # type: ignore[no-any-return]


class AssetsVersionsResource(_Resource):

    def delete(self, asset_id: str, version_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> AssetsVersionsDeleteResponse:
        """Deletes a version of a file.
        
        `DELETE /api/assets/{assetId}/versions/{versionId}` — Token permission: `write:assets`.
        """
        return self._request("DELETE", f"/api/assets/{_seg(asset_id)}/versions/{_seg(version_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def diff(self, asset_id: str, body: AssetsVersionsDiffBody, *, options: Optional[RequestOptions] = None) -> AssetVersionDiff:
        """Compares the text of two versions of a file.
        
        `POST /api/assets/{assetId}/versions/diff` — Token permission: `write:assets`.
        """
        return _pick(self._request("POST", f"/api/assets/{_seg(asset_id)}/versions/diff", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def download(self, asset_id: str, version_id: str, *, organization_id: str, inline: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the content of a version of a file.
        
        Answers the file itself, not JSON.
        
        `GET /api/assets/{assetId}/versions/{versionId}/download` — Token permission: `read:assets`.
        """
        return self._request("GET", f"/api/assets/{_seg(asset_id)}/versions/{_seg(version_id)}/download", query={"organizationId": organization_id, "inline": inline}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, asset_id: str, version_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> AssetsVersionsGetResponseData:
        """Returns one version of a file, with its extracted text.
        
        `GET /api/assets/{assetId}/versions/{versionId}` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/assets/{_seg(asset_id)}/versions/{_seg(version_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, asset_id: str, *, organization_id: str, limit: Optional[int] = None, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[AssetVersion]:
        """Lists a file's versions, newest first, and with `q` the versions whose text matches.
        
        `GET /api/assets/{assetId}/versions` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/assets/{_seg(asset_id)}/versions", query={"organizationId": organization_id, "limit": limit, "q": q}, body=None, multipart=False, options=options), "data.versions")  # type: ignore[no-any-return]

    def restore(self, asset_id: str, version_id: str, body: AssetsVersionsRestoreBody, *, options: Optional[RequestOptions] = None) -> AssetsVersionsRestoreResponseData:
        """Makes an earlier version a file's current content, keeping the content it replaces as a version.
        
        `POST /api/assets/{assetId}/versions/{versionId}/restore` — Token permission: `write:assets`.
        """
        return _pick(self._request("POST", f"/api/assets/{_seg(asset_id)}/versions/{_seg(version_id)}/restore", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, asset_id: str, version_id: str, body: AssetsVersionsUpdateBody, *, options: Optional[RequestOptions] = None) -> AssetVersion:
        """Labels a version of a file, or marks it as a milestone.
        
        `PATCH /api/assets/{assetId}/versions/{versionId}` — Token permission: `write:assets`.
        """
        return _pick(self._request("PATCH", f"/api/assets/{_seg(asset_id)}/versions/{_seg(version_id)}", query=None, body=body, multipart=False, options=options), "data.version")  # type: ignore[no-any-return]


class AssetsResource(_Resource):
    """Files
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.versions = AssetsVersionsResource(request)

    def bulk(self, body: AssetsBulkBody, *, options: Optional[RequestOptions] = None) -> AssetsBulkResponse:
        """Moves, trashes or changes the visibility of up to 500 files and 500 folders at once.
        
        Each item is handled on its own; `breakdown` and `errors` say what did not work.
        
        `POST /api/assets/bulk` — Token permission: `write:assets`.
        """
        return self._request("POST", f"/api/assets/bulk", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create_text(self, body: AssetsCreateTextBody, *, options: Optional[RequestOptions] = None) -> Asset:
        """Creates a text file — Markdown, plain text, JSON, CSV, YAML or HTML — from its content.
        
        At most 5 MB; counts against the plan's storage. JSON must parse.
        
        `POST /api/assets/create-text` — Token permission: `write:assets`.
        """
        return _pick(self._request("POST", f"/api/assets/create-text", query=None, body=body, multipart=False, options=options), "asset")  # type: ignore[no-any-return]

    def delete(self, asset_id: str, *, options: Optional[RequestOptions] = None) -> AssetsDeleteResponse:
        """Moves a file to the trash.
        
        `DELETE /api/assets/{assetId}` — Token permission: `write:assets`.
        """
        return self._request("DELETE", f"/api/assets/{_seg(asset_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def empty_trash(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> AssetsEmptyTrashResponse:
        """Deletes for good every file in an organization's trash that the caller may delete.
        
        `DELETE /api/assets/trash` — Token permission: `write:assets`.
        """
        return self._request("DELETE", f"/api/assets/trash", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def generate_image(self, body: AssetsGenerateImageBody, *, options: Optional[RequestOptions] = None) -> Asset:
        """Generates an image with AI from a prompt and saves it to the media library.
        
        Needs `asset.ai_generate`; counts against the organization's AI budget and storage.
        
        `POST /api/assets/ai-generate-image` — Token permission: `write:assets`.
        """
        return _pick(self._request("POST", f"/api/assets/ai-generate-image", query=None, body=body, multipart=False, options=options), "asset")  # type: ignore[no-any-return]

    def get(self, asset_id: str, *, options: Optional[RequestOptions] = None) -> Asset:
        """Returns one file's details.
        
        `GET /api/assets/{assetId}` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/assets/{_seg(asset_id)}", query=None, body=None, multipart=False, options=options), "asset")  # type: ignore[no-any-return]

    def intelligence(self, *, organization_id: str, days: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> AssetsIntelligenceResponse:
        """Reports an organization's storage: totals, the biggest folders and uploaders, stale files and duplicates.
        
        Needs `asset.intelligence`.
        
        `GET /api/assets/intelligence` — Token permission: `read:assets`.
        """
        return self._request("GET", f"/api/assets/intelligence", query={"organizationId": organization_id, "days": days, "limit": limit}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, workspace_id: Optional[str] = None, file_type: Optional[Literal["image", "video", "audio", "document", "other", "all"]] = None, source: Optional[Literal["upload", "scan", "recording", "transcript", "ocr", "text", "ai_image"]] = None, folder_id: Optional[str] = None, search: Optional[str] = None, visibility: Optional[AssetVisibility] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Asset]:
        """Lists the files of an organization the caller may see, newest first.
        
        `GET /api/assets` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/assets", query={"organizationId": organization_id, "workspaceId": workspace_id, "fileType": file_type, "source": source, "folderId": folder_id, "search": search, "visibility": visibility, "page": page, "limit": limit}, body=None, multipart=False, options=options), "assets")  # type: ignore[no-any-return]

    def list_trash(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> List[AssetsListTrashResponseAssetsItem]:
        """Lists the files in an organization's trash that the caller may restore, with when each is deleted for good.
        
        `GET /api/assets/trash` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/assets/trash", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "assets")  # type: ignore[no-any-return]

    def storage_usage(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> AssetsStorageUsageResponseData:
        """Returns how much of its storage an organization uses.
        
        `GET /api/assets/storage-usage` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/assets/storage-usage", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def sync(self, *, organization_id: str, since: Optional[str] = None, cursor: Optional[str] = None, options: Optional[RequestOptions] = None) -> AssetsSyncResponse:
        """The files and folders of an organization changed since a moment, oldest change first, for keeping a copy in step.
        
        Needs desktop sync on the plan and the role's `integration:use_desktop` permission (403 `desktopSyncNotPermitted`). Only what the caller may see; the platform's own folders and the files in them are left out. 500 items a page: while `nextCursor` is set, ask again with it and the same `since`. With `since`, `deletedAssetIds` names the files moved to the trash since then (on the first page only). Keep `serverTime` as the next `since`.
        
        `GET /api/sync`
        """
        return self._request("GET", f"/api/sync", query={"organizationId": organization_id, "since": since, "cursor": cursor}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def transcribe(self, body: AssetsTranscribeBody, *, options: Optional[RequestOptions] = None) -> AssetsTranscribeResponse:
        """Transcribes an audio or video file with AI and returns the text, without saving it.
        
        Needs `asset.transcribe`; counts against the organization's AI budget. Save the text with `assets.createText`.
        
        `POST /api/assets/transcribe` — Token permission: `write:assets`.
        """
        return self._request("POST", f"/api/assets/transcribe", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def trash_action(self, body: AssetsTrashActionBody, *, options: Optional[RequestOptions] = None) -> AssetsTrashActionResponse:
        """Restores files from the trash, or deletes them for good.
        
        Files the caller may not manage are reported in `errors` and left alone.
        
        `POST /api/assets/trash` — Token permission: `write:assets`.
        """
        return self._request("POST", f"/api/assets/trash", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, asset_id: str, body: UpdateAssetInput, *, options: Optional[RequestOptions] = None) -> Asset:
        """Renames a file, moves it to another folder or workspace, or changes its tags or visibility.
        
        `PATCH /api/assets/{assetId}` — Token permission: `write:assets`.
        """
        return _pick(self._request("PATCH", f"/api/assets/{_seg(asset_id)}", query=None, body=body, multipart=False, options=options), "asset")  # type: ignore[no-any-return]

    def upload(self, body: Union[AssetsUploadBody, Dict[str, Any]], *, options: Optional[RequestOptions] = None) -> AssetsUploadResponse:
        """Uploads a file to the media library.
        
        Needs `asset.create`; counts against the plan's storage and file-size limits. With `overwriteAssetId` the file replaces that file's content as a new version, and the answer is `{ success, data }` instead of `{ asset }`.
        
        `POST /api/assets` — Token permission: `write:assets`.
        """
        return self._request("POST", f"/api/assets", query=None, body=body, multipart=True, options=options)  # type: ignore[no-any-return]

    def usage(self, asset_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the pages that show a file, so you know whether it is safe to delete.
        
        Needs `asset.intelligence`.
        
        `GET /api/assets/{assetId}/usage` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/assets/{_seg(asset_id)}/usage", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "references")  # type: ignore[no-any-return]

    def zip(self, body: AssetsZipBody, *, options: Optional[RequestOptions] = None) -> AssetsZipResponse:
        """Downloads files and folders as one ZIP archive, or with `check: true` says what it would hold.
        
        Without `check` the answer is the archive itself (`application/zip`). Only files the caller may view are included; folders are kept as paths.
        
        `POST /api/assets/zip` — Token permission: `write:assets`.
        """
        return self._request("POST", f"/api/assets/zip", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class AssetSharesResource(_Resource):
    """File shares
    """

    def create(self, asset_id: str, body: CreateAssetShareInput, *, options: Optional[RequestOptions] = None) -> AssetShare:
        """Shares a file with a member, or makes a share link for it.
        
        A link's expiry is capped at the organization's maximum, and a public link is refused when the organization does not allow them.
        
        `POST /api/assets/{assetId}/shares` — Token permission: `write:assets`.
        """
        return _pick(self._request("POST", f"/api/assets/{_seg(asset_id)}/shares", query=None, body=body, multipart=False, options=options), "share")  # type: ignore[no-any-return]

    def create_folder(self, folder_id: str, body: CreateAssetShareInput, *, options: Optional[RequestOptions] = None) -> AssetShare:
        """Shares a folder with a member, or makes a share link for it.
        
        `POST /api/asset-folders/{folderId}/shares` — Token permission: `write:assets`.
        """
        return _pick(self._request("POST", f"/api/asset-folders/{_seg(folder_id)}/shares", query=None, body=body, multipart=False, options=options), "share")  # type: ignore[no-any-return]

    def delete(self, asset_id: str, share_id: str, *, options: Optional[RequestOptions] = None) -> AssetSharesDeleteResponse:
        """Removes a file share.
        
        `DELETE /api/assets/{assetId}/shares/{shareId}` — Token permission: `write:assets`.
        """
        return self._request("DELETE", f"/api/assets/{_seg(asset_id)}/shares/{_seg(share_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_by_id(self, share_id: str, *, options: Optional[RequestOptions] = None) -> AssetSharesDeleteByIdResponse:
        """Removes any share — of a file or a folder — by its id.
        
        `DELETE /api/asset-shares/{shareId}`
        """
        return self._request("DELETE", f"/api/asset-shares/{_seg(share_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, asset_id: str, *, options: Optional[RequestOptions] = None) -> List[AssetShare]:
        """Lists a file's live shares — with members and as links.
        
        `GET /api/assets/{assetId}/shares` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/assets/{_seg(asset_id)}/shares", query=None, body=None, multipart=False, options=options), "shares")  # type: ignore[no-any-return]

    def list_folder(self, folder_id: str, *, options: Optional[RequestOptions] = None) -> List[AssetShare]:
        """Lists a folder's live shares.
        
        `GET /api/asset-folders/{folderId}/shares` — Token permission: `read:assets`.
        """
        return _pick(self._request("GET", f"/api/asset-folders/{_seg(folder_id)}/shares", query=None, body=None, multipart=False, options=options), "shares")  # type: ignore[no-any-return]

    def update(self, asset_id: str, share_id: str, body: UpdateAssetShareInput, *, options: Optional[RequestOptions] = None) -> AssetShare:
        """Changes a file share's permission, expiry or password, or turns it off.
        
        `PATCH /api/assets/{assetId}/shares/{shareId}` — Token permission: `write:assets`.
        """
        return _pick(self._request("PATCH", f"/api/assets/{_seg(asset_id)}/shares/{_seg(share_id)}", query=None, body=body, multipart=False, options=options), "share")  # type: ignore[no-any-return]

    def update_by_id(self, share_id: str, body: UpdateAssetShareInput, *, options: Optional[RequestOptions] = None) -> AssetShare:
        """Changes any share — of a file or a folder — by its id.
        
        `PATCH /api/asset-shares/{shareId}`
        """
        return _pick(self._request("PATCH", f"/api/asset-shares/{_seg(share_id)}", query=None, body=body, multipart=False, options=options), "share")  # type: ignore[no-any-return]


class AuditLogsResource(_Resource):
    """Audit log — An organization's audit trail: every sign-in, change of a member, role or setting and every write the platform records for it, for its owners and admins.
    """

    def list(self, *, organization_id: str, workspace_id: Optional[str] = None, severity: Optional[Literal["critical", "high", "medium", "low", "info"]] = None, event_type: Optional[str] = None, user_id: Optional[str] = None, since: Optional[str] = None, until: Optional[str] = None, limit: Optional[int] = None, format: Optional[Literal["json", "csv"]] = None, options: Optional[RequestOptions] = None) -> List[AuditLogEvent]:
        """Lists an organization's audit log, newest first.
        
        Needs an owner or admin of the organization (403 `adminRequired`), and the audit log on the plan (402 `featureNotOnPlan`). `format=csv` downloads the same lines as a CSV file.
        
        `GET /api/audit-logs`
        """
        return _pick(self._request("GET", f"/api/audit-logs", query={"organizationId": organization_id, "workspaceId": workspace_id, "severity": severity, "eventType": event_type, "userId": user_id, "since": since, "until": until, "limit": limit, "format": format}, body=None, multipart=False, options=options), "logs")  # type: ignore[no-any-return]


class BankingAccountsGrantsResource(_Resource):

    def list(self, account_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[BankGrant]:
        """Who holds which right on a bank account.
        
        Needs the account's `manage` right.
        
        `GET /api/banking/accounts/{accountId}/grants` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/accounts/{_seg(account_id)}/grants", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "grants")  # type: ignore[no-any-return]

    def remove(self, account_id: str, grant_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingAccountsGrantsRemoveResponse:
        """Takes a grantee's rights on a bank account away.
        
        `DELETE /api/banking/accounts/{accountId}/grants/{grantId}` — Token permission: `write:banking`.
        """
        return self._request("DELETE", f"/api/banking/accounts/{_seg(account_id)}/grants/{_seg(grant_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set(self, account_id: str, body: BankingAccountsGrantsSetBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingAccountsGrantsSetResponse:
        """Gives a person or a role rights on a bank account, or changes theirs.
        
        Needs the account's `manage` right. One of `userId` and `roleId`. `pay` may carry a limit per order.
        
        `POST /api/banking/accounts/{accountId}/grants` — Token permission: `write:banking`.
        """
        return self._request("POST", f"/api/banking/accounts/{_seg(account_id)}/grants", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class BankingAccountsImportsResource(_Resource):

    def list(self, account_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[BankImport]:
        """The statement files imported into a bank account.
        
        Needs the account's `transactions` right.
        
        `GET /api/banking/accounts/{accountId}/imports` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/accounts/{_seg(account_id)}/imports", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "imports")  # type: ignore[no-any-return]

    def upload(self, account_id: str, body: Union[BankingAccountsImportsUploadBody, Dict[str, Any]], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingAccountsImportsUploadResponse:
        """Imports a CAMT.053, MT940 or CSV statement file into a bank account.
        
        Needs the account's `manage` right. Read by its bytes, 20 MB at most; the original is kept unchangeable with its SHA-256, and the same lines are never imported twice. A CSV needs a mapping: `csvMapping` (JSON), or the one saved on the account.
        
        `POST /api/banking/accounts/{accountId}/imports` — Token permission: `write:banking`.
        """
        return self._request("POST", f"/api/banking/accounts/{_seg(account_id)}/imports", query={"organizationId": organization_id}, body=body, multipart=True, options=options)  # type: ignore[no-any-return]


class BankingAccountsLedgerResource(_Resource):

    def get(self, account_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[BankingAccountsLedgerGetResponseMappingsItem]:
        """Which account of each company's books a bank account is posted to.
        
        `GET /api/banking/accounts/{accountId}/ledger` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/accounts/{_seg(account_id)}/ledger", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "mappings")  # type: ignore[no-any-return]

    def remove(self, account_id: str, *, organization_id: Optional[str] = None, issuer_id: str, options: Optional[RequestOptions] = None) -> BankingAccountsLedgerRemoveResponse:
        """Removes a bank account's mapping to a company's books; the chart account stays.
        
        `DELETE /api/banking/accounts/{accountId}/ledger` — Token permission: `write:banking`.
        """
        return self._request("DELETE", f"/api/banking/accounts/{_seg(account_id)}/ledger", query={"organizationId": organization_id, "issuerId": issuer_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set(self, account_id: str, body: BankingAccountsLedgerSetBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingAccountsLedgerSetResponse:
        """Maps a bank account to a company's books: to an existing bank account of the chart, or to a new one made for it.
        
        Needs the account's `manage` right and `invoicing:bookkeeping`. Without `ledgerAccount` its own chart account is created (SKR03 1201 ff., SKR04 1801 ff.).
        
        `PUT /api/banking/accounts/{accountId}/ledger` — Token permission: `write:banking`.
        """
        return self._request("PUT", f"/api/banking/accounts/{_seg(account_id)}/ledger", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class BankingAccountsResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.grants = BankingAccountsGrantsResource(request)
        self.imports = BankingAccountsImportsResource(request)
        self.ledger = BankingAccountsLedgerResource(request)

    def create(self, body: BankingAccountsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankAccount:
        """Creates an account whose statements are imported as files.
        
        Needs `banking:connect`; counts against the plan's bank account limit. Visibility: the request's, else Settings → Banking's default.
        
        `POST /api/banking/accounts` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/accounts", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "account")  # type: ignore[no-any-return]

    def delete(self, account_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingAccountsDeleteResponse:
        """Deletes a bank account with nothing matched or booked.
        
        409 `bankingAccountHasBooked` otherwise — archive it instead.
        
        `DELETE /api/banking/accounts/{accountId}` — Token permission: `write:banking`.
        """
        return self._request("DELETE", f"/api/banking/accounts/{_seg(account_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, account_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankAccount:
        """One bank account as the caller may see it.
        
        `GET /api/banking/accounts/{accountId}` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/accounts/{_seg(account_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "account")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, archived: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> List[BankAccount]:
        """Lists the bank accounts the caller sees, each with the caller's rights on it.
        
        Needs `banking:read`. The balance is null without the account's `balance` right.
        
        `GET /api/banking/accounts` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/accounts", query={"organizationId": organization_id, "archived": archived}, body=None, multipart=False, options=options), "accounts")  # type: ignore[no-any-return]

    def reconciliation(self, account_id: str, *, organization_id: Optional[str] = None, period: Optional[str] = None, issuer_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingAccountsReconciliationResponse:
        """One month of a bank account against the books: the bank's opening, in, out and closing, each mapped company's ledger balance and the difference, and the lines nothing explains yet.
        
        Needs the account's `transactions` right. The books' side only for a holder of `invoicing:export` or `invoicing:bookkeeping`: otherwise `books` is empty and `booksHidden` true.
        
        `GET /api/banking/accounts/{accountId}/reconciliation` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/accounts/{_seg(account_id)}/reconciliation", query={"organizationId": organization_id, "period": period, "issuerId": issuer_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, account_id: str, body: BankingAccountsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankAccount:
        """Changes a bank account's name, type, holder, visibility, CSV mapping or low-balance warning, or archives it.
        
        Needs the account's `manage` right (its creator, a grant, or `banking:settings`).
        
        `PATCH /api/banking/accounts/{accountId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("PATCH", f"/api/banking/accounts/{_seg(account_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "account")  # type: ignore[no-any-return]


class BankingAnomaliesResource(_Resource):

    def review(self, anomaly_id: str, body: Union[BankingAnomaliesReviewBody, BankingAnomaliesReviewBody2], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankAnomaly:
        """Dismisses an anomaly of a bank line (a double debit, an unusual amount, a new payee), or restores it.
        
        Needs the `match` right on the line's account. A dismissed anomaly is not raised again for the same line and kind.
        
        `POST /api/banking/anomalies/{anomalyId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/anomalies/{_seg(anomaly_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "anomaly")  # type: ignore[no-any-return]


class BankingExpectedPlansResource(_Resource):

    def create(self, body: BankPaymentPlanInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Creates a payment plan on a database; its expected payments are generated at once.
        
        Needs `banking:match`, edit access to the database, the `match` right on every account it names, and expected payments on the plan.
        
        `POST /api/banking/expected/plans` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/expected/plans", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "plan")  # type: ignore[no-any-return]

    def delete(self, plan_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingExpectedPlansDeleteResponse:
        """Deletes a payment plan, or archives it when anything was ever paid or matched.
        
        `DELETE /api/banking/expected/plans/{planId}` — Token permission: `write:banking`.
        """
        return self._request("DELETE", f"/api/banking/expected/plans/{_seg(plan_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def generate(self, plan_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingExpectedPlansGenerateResponseResult:
        """Generates a payment plan's expected payments now rather than at the next hourly run.
        
        Needs the right to change the plan.
        
        `POST /api/banking/expected/plans/{planId}/generate` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/expected/plans/{_seg(plan_id)}/generate", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "result")  # type: ignore[no-any-return]

    def get(self, plan_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """One payment plan.
        
        `GET /api/banking/expected/plans/{planId}` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/expected/plans/{_seg(plan_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "plan")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, database_id: Optional[str] = None, counts: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the payment plans the caller may see, newest first.
        
        `GET /api/banking/expected/plans` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/expected/plans", query={"organizationId": organization_id, "databaseId": database_id, "counts": counts}, body=None, multipart=False, options=options), "plans")  # type: ignore[no-any-return]

    def update(self, plan_id: str, body: BankingExpectedPlansUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes a payment plan; the rows nothing touched yet are planned again.
        
        `PATCH /api/banking/expected/plans/{planId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("PATCH", f"/api/banking/expected/plans/{_seg(plan_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "plan")  # type: ignore[no-any-return]


class BankingExpectedResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.plans = BankingExpectedPlansResource(request)

    def list(self, *, organization_id: Optional[str] = None, filter: Optional[Literal["due", "overdue", "received", "waived", "all"]] = None, plan_id: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, q: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Expected payments: what the payment plans expect, and whether it came, with totals per currency.
        
        Needs expected payments on the plan. Only rows whose plan's account lines the caller reads and whose record they may see.
        
        `GET /api/banking/expected` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/expected", query={"organizationId": organization_id, "filter": filter, "planId": plan_id, "from": from_, "to": to, "q": q, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "items")  # type: ignore[no-any-return]

    def record(self, *, organization_id: Optional[str] = None, database_id: str, record_id: str, active: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> BankRecordPaymentAccount:
        """A database record's payment account: every expected payment of the plans the caller may see, the bank lines that paid them, and totals per currency.
        
        Needs expected payments on the plan. 404 when the caller may not see the record. `account` is null when the record's database has no payment plan the caller may see (with `active=1`, none switched on).
        
        `GET /api/banking/expected/record` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/expected/record", query={"organizationId": organization_id, "databaseId": database_id, "recordId": record_id, "active": active}, body=None, multipart=False, options=options), "account")  # type: ignore[no-any-return]

    def review(self, expected_id: str, body: Union[BankingExpectedReviewBody, BankingExpectedReviewBody2], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Waives an expected payment (a reduction, a write-off), or takes the waiver back.
        
        Needs `banking:match`, the `match` right on one of the plan's accounts and the record visible.
        
        `POST /api/banking/expected/{expectedId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/expected/{_seg(expected_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "expected")  # type: ignore[no-any-return]


class BankingMatchesResource(_Resource):

    def undo(self, match_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingMatchesUndoResponseTransaction:
        """Undoes a confirmed match: the payment it recorded is removed (its entry reversed in the books), a booking is reversed.
        
        Needs `banking:match` and the account's `match` right; a match to a document needs `invoicing:payments` and the document visible, a booking `invoicing:bookkeeping`. A payment the match only took over (a confirmed payment run's) stays.
        
        `DELETE /api/banking/matches/{matchId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("DELETE", f"/api/banking/matches/{_seg(match_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "transaction")  # type: ignore[no-any-return]


class BankingMatchingResource(_Resource):

    def count(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingMatchingCountResponse:
        """How many lines wait for a look in the accounts whose lines the caller may read.
        
        `GET /api/banking/matching/count` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/matching/count", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def queue(self, *, organization_id: Optional[str] = None, account_id: Optional[str] = None, state: Optional[Literal["suggested", "unmatched"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> BankingMatchingQueueResponse:
        """The review queue: open lines with what the engine suggested, suggestions first.
        
        Documents the caller may not see are left out.
        
        `GET /api/banking/matching/queue` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/matching/queue", query={"organizationId": organization_id, "accountId": account_id, "state": state, "limit": limit, "offset": offset}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def run(self, body: BankingMatchingRunBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Runs matching again over the open lines of one account, or of every account the caller may match.
        
        Needs `banking:match`. For after new invoices were issued or a rule was added; auto-matching follows Settings → Banking.
        
        `POST /api/banking/matching/run` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/matching/run", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "result")  # type: ignore[no-any-return]


class BankingPaymentsSettingsResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Settings → Banking → Payments: the organisation's four-eyes rule.
        
        `GET /api/banking/payments/settings` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/payments/settings", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def update(self, body: BankingPaymentsSettingsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes the four-eyes rule for payment orders.
        
        Needs `banking:settings`. Applies to orders sent to approval from then on.
        
        `PUT /api/banking/payments/settings` — Token permission: `write:banking`.
        """
        return _pick(self._request("PUT", f"/api/banking/payments/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class BankingPaymentsResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.settings = BankingPaymentsSettingsResource(request)

    def act(self, order_id: str, body: Union[BankingPaymentsActBody, BankingPaymentsActBody2, BankingPaymentsActBody3, BankingPaymentsActBody4, BankingPaymentsActBody5], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingPaymentsActResponse:
        """Submits, approves, rejects, sends or cancels a payment order.
        
        Needs `banking:pay`.
        
        - `submit`: to approval (approved at once when the rule needs none).
        - `approve` / `reject`: four eyes — never the order's creator; `pay` on the account with a limit at least the total. A rejection needs a note.
        - `send`: to the bank; answers `webFormUrl`, which a person must open to confirm with their bank. The order must equal what was approved (409 `bankingPaymentChanged`).
        - `cancel`: before it was sent, or when the bank's outcome stayed unclear.
        
        `POST /api/banking/payments/{orderId}` — Token permission: `write:banking`.
        """
        return self._request("POST", f"/api/banking/payments/{_seg(order_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create(self, body: BankingPaymentsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankPaymentOrder:
        """Creates a payment order — one transfer or several — from a connected account, and sends it to approval.
        
        Needs `banking:pay` and the account's `pay` right with a limit at least the total (403 `bankingPaymentOverLimit`), and payment orders on the plan. 422 `bankingPaymentInvalid` with `problems`. With `submit` (the default) it goes to approval at once, or is approved when the organisation's rule asks for none. Sending it to the bank needs a person (see the `send` action).
        
        `POST /api/banking/payments` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/payments", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "order")  # type: ignore[no-any-return]

    def from_purchases(self, body: BankingPaymentsFromPurchasesBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankPaymentOrder:
        """Creates a payment order paying purchase invoices: an open payment run, or ticked invoices.
        
        Needs `banking:pay` with the account's `pay` right and limit, and `invoicing:read` with `invoicing:payments`. Send `runId`, or `issuerId` with `purchaseIds`.
        
        `POST /api/banking/payments/from-purchases` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/payments/from-purchases", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "order")  # type: ignore[no-any-return]

    def get(self, order_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankPaymentOrder:
        """One payment order with its items, approvals and history.
        
        A submitted order is read back from the bank first.
        
        `GET /api/banking/payments/{orderId}` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/payments/{_seg(order_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "order")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, status: Optional[str] = None, account_id: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[BankPaymentOrder]:
        """Lists payment orders: the caller's own and those of accounts where they hold `pay` or `transactions`.
        
        Needs payment orders on the plan.
        
        `GET /api/banking/payments` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/payments", query={"organizationId": organization_id, "status": status, "accountId": account_id, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "orders")  # type: ignore[no-any-return]

    def options_(self, *, organization_id: Optional[str] = None, account_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingPaymentsOptionsResponse:
        """What the caller may pay from: the connected accounts where they hold `pay` with their limit, the four-eyes rule, and with `accountId` what that account can do at the bank.
        
        Needs payment orders on the plan. `accounts` is empty without `banking:pay`. `capabilities` (several transfers in one order, instant) is null when the bank provider does not answer. `paused`: the platform has paused calls to the bank provider.
        
        `GET /api/banking/payments/options` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/payments/options", query={"organizationId": organization_id, "accountId": account_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, order_id: str, body: BankingPaymentsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankPaymentOrder:
        """Changes a payment order that is not sent yet; a waiting or approved one goes back to approval.
        
        Needs `banking:pay`: its creator, or a `pay` holder within their limit.
        
        `PATCH /api/banking/payments/{orderId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("PATCH", f"/api/banking/payments/{_seg(order_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "order")  # type: ignore[no-any-return]


class BankingReceiptsSettingsResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Settings → Banking → Receipts: which outgoing lines ask for a receipt.
        
        `GET /api/banking/receipts/settings` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/receipts/settings", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def update(self, body: BankingReceiptsSettingsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes which outgoing lines ask for a receipt.
        
        Needs `banking:settings`.
        
        `PUT /api/banking/receipts/settings` — Token permission: `write:banking`.
        """
        return _pick(self._request("PUT", f"/api/banking/receipts/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class BankingReceiptsResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.settings = BankingReceiptsSettingsResource(request)

    def book(self, receipt_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingReceiptsBookResponse:
        """Books with the receipt: creates a purchase invoice draft from it, prefilled with the bank line.
        
        Needs the account's `match` right, and in Invoicing `invoicing:purchases` and `invoicing:create` with the books on (409 `bankingReceiptBooksOff`). `aiAvailable` tells whether reading the draft with AI is offered.
        
        `POST /api/banking/receipts/{receiptId}/book` — Token permission: `write:banking`.
        """
        return self._request("POST", f"/api/banking/receipts/{_seg(receipt_id)}/book", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def decide(self, receipt_id: str, body: BankingReceiptsDecideBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Accepts or rejects a suggested receipt.
        
        Needs `banking:match` and the `match` right on the line's account.
        
        `PATCH /api/banking/receipts/{receiptId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("PATCH", f"/api/banking/receipts/{_seg(receipt_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "receipt")  # type: ignore[no-any-return]

    def file(self, receipt_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a receipt's file: the uploaded file, or the linked document's original.
        
        Needs the account's `transactions` right; a linked document only when the caller may see it in Invoicing (404 otherwise). Inline for PDF, JPEG and PNG, an attachment otherwise.
        
        `GET /api/banking/receipts/{receiptId}/file` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/receipts/{_seg(receipt_id)}/file", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def missing(self, *, organization_id: Optional[str] = None, account_id: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> BankingReceiptsMissingResponse:
        """The outgoing lines that miss their receipt, newest first, with suggestions.
        
        Which lines ask for a receipt is Settings → Banking → Receipts.
        
        `GET /api/banking/receipts` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/receipts", query={"organizationId": organization_id, "accountId": account_id, "limit": limit, "offset": offset}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def run(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingReceiptsRunResponseResult:
        """Finds receipts: scores every line that misses one against the received documents and purchase invoices again — exact and unique is linked, the rest suggested.
        
        Needs `banking:match`.
        
        `POST /api/banking/receipts/run` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/receipts/run", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "result")  # type: ignore[no-any-return]

    def unlink(self, receipt_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingReceiptsUnlinkResponse:
        """Removes a linked receipt; an uploaded file stays stored.
        
        `DELETE /api/banking/receipts/{receiptId}` — Token permission: `write:banking`.
        """
        return self._request("DELETE", f"/api/banking/receipts/{_seg(receipt_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class BankingRulesResource(_Resource):

    def create(self, body: BankingRulesCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankRule:
        """Creates a rule: lines that meet its conditions are ignored, categorised, booked or tied to a customer or supplier.
        
        Needs `banking:match`; a rule naming an account needs the `match` right on it. A `ledger` action names a company and an account of its chart that is not money, personal or inactive.
        
        `POST /api/banking/rules` — Token permission: `write:banking`.
        """
        return _pick(self._request("POST", f"/api/banking/rules", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "rule")  # type: ignore[no-any-return]

    def delete(self, rule_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingRulesDeleteResponse:
        """Deletes a banking rule.
        
        `DELETE /api/banking/rules/{ruleId}` — Token permission: `write:banking`.
        """
        return self._request("DELETE", f"/api/banking/rules/{_seg(rule_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[BankRule]:
        """Lists the organisation's banking rules, manual and learned, by priority.
        
        `GET /api/banking/rules` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/rules", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "rules")  # type: ignore[no-any-return]

    def update(self, rule_id: str, body: BankingRulesUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankRule:
        """Changes a banking rule; changing a learned rule's conditions or action makes it a manual one.
        
        `PATCH /api/banking/rules/{ruleId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("PATCH", f"/api/banking/rules/{_seg(rule_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "rule")  # type: ignore[no-any-return]


class BankingSettingsResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankSettings:
        """Settings → Banking.
        
        `GET /api/banking/settings` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/settings", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def update(self, body: BankingSettingsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankSettings:
        """Changes Settings → Banking: auto-matching, the suggestion threshold, new accounts' visibility, consent reminders, AI on bank data.
        
        Needs `banking:settings`.
        
        `PUT /api/banking/settings` — Token permission: `write:banking`.
        """
        return _pick(self._request("PUT", f"/api/banking/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class BankingTransactionsResource(_Resource):

    def add_receipt(self, transaction_id: str, body: Union[BankingTransactionsAddReceiptBody, BankingTransactionsAddReceiptBody2], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingTransactionsAddReceiptResponse:
        """Links a received document or purchase invoice to a bank line as its receipt, or says it needs none.
        
        Needs the account's `match` right. A file can be uploaded instead as multipart form data in a `file` field (PDF, JPEG, PNG or HEIC, 20 MB at most).
        
        `POST /api/banking/transactions/{transactionId}/receipts` — Token permission: `write:banking`.
        """
        return self._request("POST", f"/api/banking/transactions/{_seg(transaction_id)}/receipts", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def annotate(self, transaction_id: str, body: BankingTransactionsAnnotateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankTransaction:
        """Sets a bank line's notes and category; the bank's own data never changes.
        
        Needs the account's `match` right.
        
        `PATCH /api/banking/transactions/{transactionId}` — Token permission: `write:banking`.
        """
        return _pick(self._request("PATCH", f"/api/banking/transactions/{_seg(transaction_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "transaction")  # type: ignore[no-any-return]

    def export(self, *, organization_id: Optional[str] = None, format: Optional[Literal["csv", "xlsx"]] = None, separator: Optional[Literal["semicolon", "comma"]] = None, account_id: Optional[str] = None, q: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, category: Optional[str] = None, direction: Optional[Literal["in", "out"]] = None, match_state: Optional[Literal["unmatched", "suggested", "matched", "ignored", "booked_manually"]] = None, status: Optional[Literal["pending", "booked"]] = None, anomaly: Optional[Literal["open", "dismissed"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the lines the list shows for the same filters as a CSV or Excel file.
        
        Needs `banking:export`. Newest first, up to a maximum; the header `X-Export-Truncated: 1` says when the filter held more.
        
        `GET /api/banking/transactions/export` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/transactions/export", query={"organizationId": organization_id, "format": format, "separator": separator, "accountId": account_id, "q": q, "from": from_, "to": to, "category": category, "direction": direction, "matchState": match_state, "status": status, "anomaly": anomaly}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, transaction_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankTransaction:
        """One bank line, with its category suggestion and its anomalies.
        
        `GET /api/banking/transactions/{transactionId}` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/transactions/{_seg(transaction_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "transaction")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, account_id: Optional[str] = None, q: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, category: Optional[str] = None, direction: Optional[Literal["in", "out"]] = None, match_state: Optional[Literal["unmatched", "suggested", "matched", "ignored", "booked_manually"]] = None, status: Optional[Literal["pending", "booked"]] = None, anomaly: Optional[Literal["open", "dismissed"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[BankTransaction]:
        """Lists one page of the lines of the accounts whose lines the caller may read, with the sums in and out.
        
        Needs `banking:read`; only accounts the caller holds the `transactions` right on (naming one without it is 403 `bankingAccountRightMissing`).
        
        `GET /api/banking/transactions` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/transactions", query={"organizationId": organization_id, "accountId": account_id, "q": q, "from": from_, "to": to, "category": category, "direction": direction, "matchState": match_state, "status": status, "anomaly": anomaly, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "items")  # type: ignore[no-any-return]

    def match_(self, transaction_id: str, body: Union[BankingTransactionsMatchBody, BankingTransactionsMatchBody2, BankingTransactionsMatchBody3, BankingTransactionsMatchBody4, BankingTransactionsMatchBody5], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingTransactionsMatchResponse:
        """Matches a bank line to invoices, purchases, expected payments or bookings — or accepts, rejects, ignores or rechecks its suggestions.
        
        Needs `banking:match` and the account's `match` right; matching documents also needs `invoicing:read` and `invoicing:payments`, bookings `invoicing:bookkeeping`.
        
        - `apply`: several targets split the line; amounts positive, together at most what is left.
        - `accept`: confirm the open suggestions as they stand.
        - `reject`: "not this" — the open suggestions go.
        - `ignore`: the line needs no match (or does again).
        - `recheck`: run the engine on this line again.
        
        `POST /api/banking/transactions/{transactionId}/matching` — Token permission: `write:banking`.
        """
        return self._request("POST", f"/api/banking/transactions/{_seg(transaction_id)}/matching", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def match_candidates(self, transaction_id: str, *, organization_id: Optional[str] = None, q: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[BankMatchCandidate]:
        """What a bank line could be matched to — open invoices for money in, purchase invoices still owed for money out, expected payments — in the line's currency, ranked for this line.
        
        Needs `banking:match` and the account's `match` right; documents also need `invoicing:read` and `invoicing:payments`, without which only expected payments are offered. Only what the caller may see.
        
        `GET /api/banking/transactions/{transactionId}/matching/candidates` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/transactions/{_seg(transaction_id)}/matching/candidates", query={"organizationId": organization_id, "q": q, "limit": limit}, body=None, multipart=False, options=options), "candidates")  # type: ignore[no-any-return]

    def matches(self, transaction_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingTransactionsMatchesResponse:
        """A bank line's matches — confirmed, suggested and undone — what is left of it, and whether the caller may match it.
        
        `hidden` counts the matches to documents the caller may not see.
        
        `GET /api/banking/transactions/{transactionId}/matching` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/transactions/{_seg(transaction_id)}/matching", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def receipt_candidates(self, transaction_id: str, *, organization_id: Optional[str] = None, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[BankReceiptCandidate]:
        """Received documents and purchase invoices that could be a bank line's receipt, best first.
        
        Needs the account's `match` right. Without `q`, the documents the receipt rules score for this line; `q` narrows by number or supplier and also finds documents outside the date window. At most 30, only those the caller may see.
        
        `GET /api/banking/transactions/{transactionId}/receipts/candidates` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/transactions/{_seg(transaction_id)}/receipts/candidates", query={"organizationId": organization_id, "q": q}, body=None, multipart=False, options=options), "candidates")  # type: ignore[no-any-return]

    def receipts(self, transaction_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingTransactionsReceiptsResponse:
        """A bank line's receipts, linked and suggested, and whether it still misses one.
        
        `GET /api/banking/transactions/{transactionId}/receipts` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/transactions/{_seg(transaction_id)}/receipts", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def suggest(self, transaction_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingTransactionsSuggestResponse:
        """Suggests a category and ledger account for a bank line, from the counterpart's history and then the platform AI.
        
        Needs `banking:match` and the account's `match` right. The suggestion is kept beside the line and applied by a person, never booked by itself. The AI half needs AI on bank data on the plan and allowed in Settings → Banking. 10 a minute.
        
        `POST /api/banking/transactions/{transactionId}/suggest` — Token permission: `write:banking`.
        """
        return self._request("POST", f"/api/banking/transactions/{_seg(transaction_id)}/suggest", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class BankingResource(_Resource):
    """Banking — The organisation's bank accounts and their lines: statement imports, matching to invoices and purchases, rules, receipts, expected payments, payment orders, the liquidity forecast. Every operation works in one organisation (`organizationId`) and needs the role's `banking:*` permissions held at organisation level, plus the right on each account (a grant, its visibility). Connecting a bank goes through finAPI's web form in the dashboard.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.accounts = BankingAccountsResource(request)
        self.anomalies = BankingAnomaliesResource(request)
        self.expected = BankingExpectedResource(request)
        self.matches = BankingMatchesResource(request)
        self.matching = BankingMatchingResource(request)
        self.payments = BankingPaymentsResource(request)
        self.receipts = BankingReceiptsResource(request)
        self.rules = BankingRulesResource(request)
        self.settings = BankingSettingsResource(request)
        self.transactions = BankingTransactionsResource(request)

    def forecast(self, *, organization_id: Optional[str] = None, days: Optional[int] = None, options: Optional[RequestOptions] = None) -> BankingForecastResponse:
        """The liquidity forecast: today's balances moved by open invoices, recurring invoices, open purchases and recurring payments — a row per day.
        
        Only accounts the caller holds the `balance` right on; `available: false` when that is none.
        
        `GET /api/banking/forecast` — Token permission: `read:banking`.
        """
        return self._request("GET", f"/api/banking/forecast", query={"organizationId": organization_id, "days": days}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def import_preview(self, body: Union[BankingImportPreviewBody, Dict[str, Any]], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BankingImportPreviewResponse:
        """Tells what a statement file is before importing it: its format and, for a CSV, its header, a few rows and a recognised bank's mapping.
        
        Nothing is stored.
        
        `POST /api/banking/import-preview` — Token permission: `write:banking`.
        """
        return self._request("POST", f"/api/banking/import-preview", query={"organizationId": organization_id}, body=body, multipart=True, options=options)  # type: ignore[no-any-return]

    def reports(self, *, organization_id: Optional[str] = None, dataset: Literal["balances", "balanceHistory", "inOutByMonth", "byCategory", "topCounterparts", "forecast"], period: Optional[Literal["3m", "6m", "12m"]] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The Banking hub's numbers as rows: balances, balance history, in and out by month, by category, top counterparts, the forecast.
        
        `GET /api/banking/reports` — Token permission: `read:banking`.
        """
        return _pick(self._request("GET", f"/api/banking/reports", query={"organizationId": organization_id, "dataset": dataset, "period": period}, body=None, multipart=False, options=options), "rows")  # type: ignore[no-any-return]


class BillingResource(_Resource):
    """Billing — An organization's own plan with the platform: its status, billing address, payment history and the invoices the platform issued to it. Changing or paying for a plan happens in the dashboard, where the payment provider's form can ask the person to confirm.
    """

    def document_pdf(self, document_id: str, *, inline: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the PDF of a document the platform issued to the caller, as archived.
        
        An organization's document also needs `invoices:download` there. 404 for anything else. The header `X-Content-SHA256` carries the stored hash; every download is written to the audit log.
        
        `GET /api/billing/documents/{documentId}/pdf`
        """
        return self._request("GET", f"/api/billing/documents/{_seg(document_id)}/pdf", query={"inline": inline}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def document_xml(self, document_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the e-invoice XML of a document the platform issued to the caller, as archived.
        
        Same access as the PDF. 404 also when the document was not issued as an e-invoice; 502 `invoicingEinvoiceXmlMissing` when the archive cannot be read.
        
        `GET /api/billing/documents/{documentId}/xml`
        """
        return self._request("GET", f"/api/billing/documents/{_seg(document_id)}/xml", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def explain_document(self, document_id: str, *, options: Optional[RequestOptions] = None) -> BillingExplainDocumentResponse:
        """Explains a document the platform issued to the caller in plain language, with the platform AI.
        
        Counts against the buyer organization's AI tokens (a personal purchase: the caller's first organization). 503 `aiNotConfigured` without platform AI, 403 `aiOptedOut` when the person opted out of AI, 429 over the quota. Cached per document and language for 24 hours.
        
        `POST /api/billing/documents/{documentId}/explain`
        """
        return self._request("POST", f"/api/billing/documents/{_seg(document_id)}/explain", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_address(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> BillingAddress:
        """Returns an organization's billing address and VAT number.
        
        Needs `billing:read` and membership of the organization.
        
        `GET /api/billing/address`
        """
        return self._request("GET", f"/api/billing/address", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_status(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> BillingStatus:
        """Returns the status of an organization's plan.
        
        Needs `billing:read` and membership of the organization. A paid plan is preferred over a free one when both are assigned.
        
        `GET /api/billing/status`
        """
        return self._request("GET", f"/api/billing/status", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_documents(self, *, organization_id: Optional[str] = None, type_: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> BillingListDocumentsResponseData:
        """Lists the invoices, credit notes and other documents the platform issued to the caller or the caller's organizations.
        
        An organization's documents are listed where the caller holds `invoices:read` at organization level; personal purchases always. Drafts are never listed.
        
        `GET /api/billing/documents`
        """
        return _pick(self._request("GET", f"/api/billing/documents", query={"organizationId": organization_id, "type": type_, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_history(self, *, organization_id: str, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[BillingEvent]:
        """Lists an organization's billing events, newest first.
        
        Needs `billing:read` and membership of the organization.
        
        `GET /api/billing/history`
        """
        return _pick(self._request("GET", f"/api/billing/history", query={"organizationId": organization_id, "limit": limit}, body=None, multipart=False, options=options), "events")  # type: ignore[no-any-return]

    def list_marketplace_invoices(self, *, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[MarketplaceInvoice]:
        """Lists the invoices marketplace sellers issued to the caller or the caller's organizations.
        
        An organization's invoices are listed where the caller holds `invoices:read` at organization level. 403 `featureDisabledByAdmin` while the marketplace is switched off.
        
        `GET /api/billing/documents/marketplace`
        """
        return _pick(self._request("GET", f"/api/billing/documents/marketplace", query={"limit": limit, "offset": offset}, body=None, multipart=False, options=options), "data.rows")  # type: ignore[no-any-return]

    def marketplace_invoice_pdf(self, invoice_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the PDF of a marketplace seller's invoice to the caller or the caller's organization.
        
        An organization's invoice also needs `invoices:download` there; 404 otherwise. Every download is written to the audit log.
        
        `GET /api/billing/documents/marketplace/{invoiceId}/pdf`
        """
        return self._request("GET", f"/api/billing/documents/marketplace/{_seg(invoice_id)}/pdf", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_address(self, body: UpdateBillingAddressInput, *, options: Optional[RequestOptions] = None) -> BillingUpdateAddressResponse:
        """Saves an organization's billing address and VAT number.
        
        Needs `billing:manage` in that organization. A field left out keeps its value; an empty string clears it. An EU VAT number is checked (400 when malformed), and the details are passed on to the payment provider when the organization is already a customer there (`providerSync`).
        
        `PATCH /api/billing/address`
        """
        return self._request("PATCH", f"/api/billing/address", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def usage(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> BillingUsageResponse:
        """Returns an organization's plan with its limits and what is used of each, AI and video usage this month, and whether the caller may change the plan.
        
        Needs membership of the organization. `limits` and `usage` are keyed alike (`max_projects`, `max_storage_mb` …); a limit of `-1` means no limit. Mailboxes, mail storage, calendars, booking pages and organizations are the caller's own, against the best plan among their organizations; the organization's shared mailboxes are `sharedMail`.
        
        `GET /api/usage`
        """
        return self._request("GET", f"/api/usage", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class BuilderBlocksVersionsResource(_Resource):

    def create(self, block_id: str, body: BuilderBlocksVersionsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> float:
        """Publishes a new version of a block's schema, defaults and template, which becomes the current one.
        
        Needs `component:manage_org_blocks` held in the organisation acted on.
        
        `POST /api/builder-blocks/{blockId}/versions`
        """
        return _pick(self._request("POST", f"/api/builder-blocks/{_seg(block_id)}/versions", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "data.version")  # type: ignore[no-any-return]

    def list(self, block_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[BuilderBlockVersion]:
        """Lists every version of a block, the newest first.
        
        Needs `component:manage_org_blocks` held in the organisation acted on.
        
        `GET /api/builder-blocks/{blockId}/versions`
        """
        return _pick(self._request("GET", f"/api/builder-blocks/{_seg(block_id)}/versions", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.versions")  # type: ignore[no-any-return]


class BuilderBlocksResource(_Resource):
    """Builder blocks — An organisation's own blocks for the website builder — each with versions of its props schema, default props and styles and an HTML template — beside the platform's blocks, which are read-only. The organisation acted on is the one the request names, else the one the token is bound to; the caller must belong to it.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.versions = BuilderBlocksVersionsResource(request)

    def catalog(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[BuilderBlockCatalogEntry]:
        """Lists every block the editor offers the caller — the platform's and the organisation's own — with its current schema, defaults and whether the plan includes it.
        
        Hidden blocks are left out; a block the plan does not include is listed with `policy.accessible: false`. Answers an `ETag`; with a matching `If-None-Match` it answers 304.
        
        `GET /api/builder-blocks/catalog`
        """
        return _pick(self._request("GET", f"/api/builder-blocks/catalog", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.blocks")  # type: ignore[no-any-return]

    def create(self, body: BuilderBlocksCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> str:
        """Creates a block of the organisation, with its first version.
        
        Needs `component:manage_org_blocks` held in the organisation acted on. The block starts as `beta`. 409 when the organisation already has a block with that slug.
        
        `POST /api/builder-blocks`
        """
        return _pick(self._request("POST", f"/api/builder-blocks", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "data.id")  # type: ignore[no-any-return]

    def delete(self, block_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BuilderBlocksDeleteResponseData:
        """Moves a block of the organisation to the trash.
        
        Needs `component:manage_org_blocks` held in the organisation acted on. It can be restored from the trash until it is deleted for good.
        
        `DELETE /api/builder-blocks/{blockId}`
        """
        return _pick(self._request("DELETE", f"/api/builder-blocks/{_seg(block_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, search: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> BuilderBlocksListResponseData:
        """Lists one page of the organisation's own blocks, the most recently changed first.
        
        Needs `component:manage_org_blocks` held in the organisation acted on. Blocks in the trash are left out.
        
        `GET /api/builder-blocks`
        """
        return _pick(self._request("GET", f"/api/builder-blocks", query={"organizationId": organization_id, "search": search, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def offer_in_marketplace(self, block_id: str, body: BuilderBlocksOfferInMarketplaceBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BuilderBlocksOfferInMarketplaceResponseData:
        """Prepares a product in the Products hub that offers the block in the marketplace, or finds the one already there.
        
        Needs the marketplace switched on, `component:manage_org_blocks`, `products:create` in the block's organisation, and selling in the marketplace on its plan. Nothing is listed yet: the product is finished and submitted in the Products hub, and a purchase delivers the block's current version.
        
        `POST /api/builder-blocks/{blockId}/publish`
        """
        return _pick(self._request("POST", f"/api/builder-blocks/{_seg(block_id)}/publish", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, block_id: str, body: BuilderBlocksUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BuilderBlocksUpdateResponseData:
        """Changes a block's name, description, category, icon, tags, notes or whether it is offered.
        
        Needs `component:manage_org_blocks` held in the organisation acted on. Only the fields sent change; the schema and template change with a new version (builderBlocks.versions.create).
        
        `PATCH /api/builder-blocks/{blockId}`
        """
        return _pick(self._request("PATCH", f"/api/builder-blocks/{_seg(block_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def usage(self, block_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> BuilderBlocksUsageResponseData:
        """Tells how often a block of the organisation is used, and on which pages.
        
        Needs `component:manage_org_blocks` held in the organisation acted on. `pages` names at most 25.
        
        `GET /api/builder-blocks/{blockId}/usage`
        """
        return _pick(self._request("GET", f"/api/builder-blocks/{_seg(block_id)}/usage", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class CalendarResource(_Resource):
    """Calendar — Calendars and their events, sharing, ICS subscriptions and CalDAV sync; booking pages with their bookings and waiting lists; Google and Microsoft accounts; meeting polls; the scheduling helpers (conflicts, holidays, AI). Everything needs Calendar on the caller's plan (booking pages: booking pages on the plan).
    """

    def add_attendee(self, event_id: str, body: CalendarAddAttendeeBody, *, options: Optional[RequestOptions] = None) -> CalendarEventAttendee:
        """Adds a guest to an event and invites them by mail.
        
        Events of calendars the caller owns. Answers 201.
        
        `POST /api/calendar/events/{eventId}/attendees`
        """
        return _pick(self._request("POST", f"/api/calendar/events/{_seg(event_id)}/attendees", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def ai_command(self, body: CalendarAiCommandBody, *, options: Optional[RequestOptions] = None) -> Union[CalendarAiCommandResponseData, CalendarAiCommandResponseData2]:
        """Reads an event out of a sentence (`parse_event`), or suggests free meeting times (`suggest_slots`).
        
        parse_event needs AI scheduling on the plan and counts against the organisation's AI allowance. suggest_slots needs no AI: it ranks 3–5 free times within the caller's working hours and own events.
        
        `POST /api/calendar/ai`
        """
        return _pick(self._request("POST", f"/api/calendar/ai", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def cancel_booking(self, id: str, body: CalendarCancelBookingBody, *, options: Optional[RequestOptions] = None) -> Booking:
        """Cancels a booking: as its host, or as the guest with the booking's cancel token.
        
        The guest is told by mail and the slot is freed. 400 when already cancelled.
        
        `POST /api/calendar/bookings/{id}/cancel`
        """
        return _pick(self._request("POST", f"/api/calendar/bookings/{_seg(id)}/cancel", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def check_conflicts(self, body: CalendarCheckConflictsBody, *, options: Optional[RequestOptions] = None) -> List[CalendarCheckConflictsResponseDataConflictsItem]:
        """Lists the caller's events that overlap a proposed time, recurring ones and travel buffers included.
        
        Across the calendars the caller owns; at most 25.
        
        `POST /api/calendar/conflicts`
        """
        return _pick(self._request("POST", f"/api/calendar/conflicts", query=None, body=body, multipart=False, options=options), "data.conflicts")  # type: ignore[no-any-return]

    def confirm_booking(self, id: str, *, options: Optional[RequestOptions] = None) -> Booking:
        """Confirms a pending booking of a page the caller owns.
        
        A booking held back as suspected spam is released at the same time.
        
        `POST /api/calendar/bookings/{id}/confirm`
        """
        return _pick(self._request("POST", f"/api/calendar/bookings/{_seg(id)}/confirm", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_booking_page(self, body: CalendarCreateBookingPageBody, *, options: Optional[RequestOptions] = None) -> BookingPage:
        """Creates a booking page on one of the caller's calendars.
        
        Counts against the plan's booking page limit. The slug is the page's public address and must be free.
        
        `POST /api/calendar/booking-pages`
        """
        return _pick(self._request("POST", f"/api/calendar/booking-pages", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_calendar(self, body: CalendarCreateCalendarBody, *, options: Optional[RequestOptions] = None) -> Calendar:
        """Creates a calendar.
        
        Counts against the plan's calendar limit. A workspace or organisation calendar takes `workspaceId` / `organizationId`, else the `X-Workspace-Id` / `X-Organization-Id` header.
        
        `POST /api/calendar/calendars`
        """
        return _pick(self._request("POST", f"/api/calendar/calendars", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_event(self, calendar_id: str, body: CalendarCreateEventBody, *, options: Optional[RequestOptions] = None) -> CalendarEvent:
        """Creates an event in a calendar; its guests are invited by mail.
        
        Needs edit access to the calendar. `createConference` adds a Google Meet or Teams link when the calendar mirrors such an account.
        
        `POST /api/calendar/calendars/{calendarId}/events`
        """
        return _pick(self._request("POST", f"/api/calendar/calendars/{_seg(calendar_id)}/events", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_event_conference(self, event_id: str, *, options: Optional[RequestOptions] = None) -> CalendarCreateEventConferenceResponseData:
        """Creates a Google Meet or Teams link for an event of a calendar linked to Google or Microsoft.
        
        Events of calendars the caller owns. 409 when the calendar is not linked, 422 when the account cannot make online meetings. Google may still be making it (`status: pending`); the next sync brings it.
        
        `POST /api/calendar/events/{eventId}/conference`
        """
        return _pick(self._request("POST", f"/api/calendar/events/{_seg(event_id)}/conference", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_proposal(self, body: CalendarCreateProposalBody, *, options: Optional[RequestOptions] = None) -> CalendarCreateProposalResponseData:
        """Creates a meeting poll: 2–8 candidate times the guests vote on without an account.
        
        The guests vote at /schedule/<token>; finalize it to make the winning time an event.
        
        `POST /api/calendar/proposals`
        """
        return _pick(self._request("POST", f"/api/calendar/proposals", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_share(self, calendar_id: str, body: CalendarCreateShareBody, *, options: Optional[RequestOptions] = None) -> CalendarShare:
        """Shares a calendar with a person by e-mail address.
        
        The calendar's owner only. Needs `calendar:share`. An address with no account yet is kept and links when they sign up. 409 when already shared. With an organisation-bound token, only members of that organisation are linked.
        
        `POST /api/calendar/calendars/{calendarId}/shares`
        """
        return _pick(self._request("POST", f"/api/calendar/calendars/{_seg(calendar_id)}/shares", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def decide_spam_booking(self, id: str, body: CalendarDecideSpamBookingBody, *, options: Optional[RequestOptions] = None) -> Booking:
        """Decides on a booking held back as suspected spam: let it through, or discard it without mailing anybody.
        
        The booking page's owner; only a pending booking marked as suspected.
        
        `POST /api/calendar/bookings/{id}/spam`
        """
        return _pick(self._request("POST", f"/api/calendar/bookings/{_seg(id)}/spam", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_booking(self, id: str, *, options: Optional[RequestOptions] = None) -> CalendarDeleteBookingResponse:
        """Cancels a booking as its host; the guest is told by mail.
        
        Never deleted: it stays as cancelled. One cancelled before answers `alreadyCancelled`.
        
        `DELETE /api/calendar/bookings/{id}`
        """
        return self._request("DELETE", f"/api/calendar/bookings/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_booking_page(self, id: str, *, options: Optional[RequestOptions] = None) -> CalendarDeleteBookingPageResponse:
        """Moves one of the caller's booking pages to the trash.
        
        `DELETE /api/calendar/booking-pages/{id}`
        """
        return self._request("DELETE", f"/api/calendar/booking-pages/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_calendar(self, calendar_id: str, *, force: Optional[bool] = None, options: Optional[RequestOptions] = None) -> CalendarDeleteCalendarResponse:
        """Moves a calendar to the trash, or deletes it for good with `force`.
        
        The calendar's owner only.
        
        `DELETE /api/calendar/calendars/{calendarId}`
        """
        return self._request("DELETE", f"/api/calendar/calendars/{_seg(calendar_id)}", query={"force": force}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_event(self, event_id: str, *, options: Optional[RequestOptions] = None) -> CalendarDeleteEventResponse:
        """Moves an event of a calendar the caller owns to the trash.
        
        `DELETE /api/calendar/events/{eventId}`
        """
        return self._request("DELETE", f"/api/calendar/events/{_seg(event_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_share(self, calendar_id: str, share_id: str, *, options: Optional[RequestOptions] = None) -> CalendarDeleteShareResponse:
        """Stops sharing a calendar with a person.
        
        The calendar's owner only. Needs `calendar:share`.
        
        `DELETE /api/calendar/calendars/{calendarId}/shares/{shareId}`
        """
        return self._request("DELETE", f"/api/calendar/calendars/{_seg(calendar_id)}/shares/{_seg(share_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def disable_caldav_sync(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> CalendarDisableCaldavSyncResponse:
        """Turns off CalDAV sync for a calendar and removes its CalDAV copy.
        
        The calendar's owner only. Needs `calendar:caldav_enable`. The events here stay.
        
        `DELETE /api/calendar/calendars/{calendarId}/caldav-sync`
        """
        return self._request("DELETE", f"/api/calendar/calendars/{_seg(calendar_id)}/caldav-sync", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def disconnect_integration(self, id: str, *, options: Optional[RequestOptions] = None) -> CalendarDisconnectIntegrationResponse:
        """Disconnects a Google or Microsoft account; its mirrored calendars go to the trash.
        
        `DELETE /api/calendar/integrations/{id}`
        """
        return self._request("DELETE", f"/api/calendar/integrations/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def enable_caldav_sync(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> CalendarEnableCaldavSyncResponseData:
        """Turns on CalDAV sync for a calendar and copies its events there.
        
        The calendar's owner only. Needs `calendar:caldav_enable`. More than 50 events are copied in the background (`backfillQueued`).
        
        `POST /api/calendar/calendars/{calendarId}/caldav-sync`
        """
        return _pick(self._request("POST", f"/api/calendar/calendars/{_seg(calendar_id)}/caldav-sync", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def event_briefing(self, event_id: str, *, options: Optional[RequestOptions] = None) -> CalendarEventBriefingResponseData:
        """Writes an AI briefing for a meeting: who is coming, recent mail with them, earlier meetings.
        
        Needs view access to the event's content. Needs AI scheduling on the plan and counts against the organisation's AI allowance.
        
        `POST /api/calendar/events/{eventId}/briefing`
        """
        return _pick(self._request("POST", f"/api/calendar/events/{_seg(event_id)}/briefing", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def event_meeting_need(self, event_id: str, *, options: Optional[RequestOptions] = None) -> CalendarEventMeetingNeedResponseData:
        """Asks the AI whether an event needs to be a meeting, with a reply to send instead when it does not.
        
        Needs view access to the event's content. Needs AI scheduling on the plan and counts against the organisation's AI allowance.
        
        `POST /api/calendar/events/{eventId}/meeting-need`
        """
        return _pick(self._request("POST", f"/api/calendar/events/{_seg(event_id)}/meeting-need", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def event_outcome(self, event_id: str, body: Union[CalendarEventOutcomeBody, CalendarEventOutcomeBody2], *, options: Optional[RequestOptions] = None) -> Union[CalendarEventOutcomeResponseData, CalendarEventOutcomeResponseData2]:
        """Drafts a meeting's outcome with AI (`generate`), or saves one (`save`).
        
        generate: view access; needs AI scheduling on the plan and counts against the organisation's AI allowance. Nothing is stored. save: edit access.
        
        `POST /api/calendar/events/{eventId}/outcome`
        """
        return _pick(self._request("POST", f"/api/calendar/events/{_seg(event_id)}/outcome", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def event_recurrence(self, event_id: str, body: CalendarEventRecurrenceBody, *, options: Optional[RequestOptions] = None) -> Union[CalendarEventRecurrenceResponseData, CalendarEventRecurrenceResponseData2]:
        """Keeps a recurring event going (`renew`) or ends its series today (`kill`).
        
        Needs edit access. Ending keeps the past occurrences. 400 for an event that does not repeat.
        
        `POST /api/calendar/events/{eventId}/recurrence`
        """
        return _pick(self._request("POST", f"/api/calendar/events/{_seg(event_id)}/recurrence", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def finalize_proposal(self, token: str, body: CalendarFinalizeProposalBody, *, force: Optional[bool] = None, options: Optional[RequestOptions] = None) -> CalendarFinalizeProposalResponseData:
        """Makes one time of a meeting poll a calendar event and closes the poll.
        
        The poll's organiser only; needs edit access to the calendar. 409 when the time collides with an event there, unless `force=true`.
        
        `POST /api/calendar/proposals/{token}/finalize`
        """
        return _pick(self._request("POST", f"/api/calendar/proposals/{_seg(token)}/finalize", query={"force": force}, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_booking(self, id: str, *, options: Optional[RequestOptions] = None) -> CalendarGetBookingResponseData:
        """One booking of a page the caller hosts, with its page.
        
        `GET /api/calendar/bookings/{id}`
        """
        return _pick(self._request("GET", f"/api/calendar/bookings/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_booking_page(self, id: str, *, options: Optional[RequestOptions] = None) -> BookingPage:
        """One of the caller's booking pages.
        
        `GET /api/calendar/booking-pages/{id}`
        """
        return _pick(self._request("GET", f"/api/calendar/booking-pages/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_caldav_sync(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> CalendarGetCaldavSyncResponseData:
        """Whether a calendar syncs over CalDAV, and the server address and login to add it to Apple Calendar, Outlook or DAVx5.
        
        Anybody who can view the calendar (a public one: its owner or a `manage` share). Needs `calendar:caldav_enable`. `connection` is set while sync is on.
        
        `GET /api/calendar/calendars/{calendarId}/caldav-sync`
        """
        return _pick(self._request("GET", f"/api/calendar/calendars/{_seg(calendar_id)}/caldav-sync", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_calendar(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> Calendar:
        """One calendar the caller owns or that is shared with them.
        
        `GET /api/calendar/calendars/{calendarId}`
        """
        return _pick(self._request("GET", f"/api/calendar/calendars/{_seg(calendar_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_calendar_feed_token(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> CalendarGetCalendarFeedTokenResponseData:
        """A calendar's ICS subscription URL, for Google, Apple or Outlook calendars.
        
        The calendar's owner only. The URL carries a secret: whoever has it reads the calendar.
        
        `GET /api/calendar/calendars/{calendarId}/feed`
        """
        return _pick(self._request("GET", f"/api/calendar/calendars/{_seg(calendar_id)}/feed", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_event(self, event_id: str, *, options: Optional[RequestOptions] = None) -> CalendarEvent:
        """One event of a calendar the caller owns.
        
        `GET /api/calendar/events/{eventId}`
        """
        return _pick(self._request("GET", f"/api/calendar/events/{_seg(event_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_event_ics(self, event_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Downloads an event as an .ics file.
        
        Events of calendars the caller owns.
        
        `GET /api/calendar/events/{eventId}/ics`
        """
        return self._request("GET", f"/api/calendar/events/{_seg(event_id)}/ics", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_event_outcome(self, event_id: str, *, options: Optional[RequestOptions] = None) -> CalendarGetEventOutcomeResponseData:
        """A meeting's saved outcome summary.
        
        Needs view access to the event's content.
        
        `GET /api/calendar/events/{eventId}/outcome`
        """
        return _pick(self._request("GET", f"/api/calendar/events/{_seg(event_id)}/outcome", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_settings(self, *, options: Optional[RequestOptions] = None) -> CalendarSettings:
        """The caller's calendar preferences, defaults filled in.
        
        `GET /api/calendar/settings`
        """
        return _pick(self._request("GET", f"/api/calendar/settings", query=None, body=None, multipart=False, options=options), "data.settings")  # type: ignore[no-any-return]

    def holidays(self, *, year: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[CalendarHolidaysResponseDataHolidaysItem]:
        """The public holidays of the caller's holiday country and region for a year.
        
        Empty while no country is set in the calendar settings.
        
        `GET /api/calendar/holidays`
        """
        return _pick(self._request("GET", f"/api/calendar/holidays", query={"year": year}, body=None, multipart=False, options=options), "data.holidays")  # type: ignore[no-any-return]

    def list_attendees(self, event_id: str, *, options: Optional[RequestOptions] = None) -> List[CalendarEventAttendee]:
        """Lists an event's guests with their answers.
        
        Events of calendars the caller owns.
        
        `GET /api/calendar/events/{eventId}/attendees`
        """
        return _pick(self._request("GET", f"/api/calendar/events/{_seg(event_id)}/attendees", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_booking_pages(self, *, options: Optional[RequestOptions] = None) -> List[BookingPage]:
        """Lists the caller's booking pages.
        
        `GET /api/calendar/booking-pages`
        """
        return _pick(self._request("GET", f"/api/calendar/booking-pages", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_bookings(self, *, status: Optional[Literal["pending", "confirmed", "cancelled"]] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> CalendarListBookingsResponseData:
        """Lists one page of the bookings of the pages the caller hosts, latest start first.
        
        `GET /api/calendar/bookings`
        """
        return _pick(self._request("GET", f"/api/calendar/bookings", query={"status": status, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_calendars(self, *, options: Optional[RequestOptions] = None) -> List[CalendarListCalendarsResponseDataItem]:
        """Lists the calendars the caller can see: their own, those shared with them, and their organisations' and workspaces'.
        
        The headers `X-Organization-Id` / `X-Workspace-Id` narrow the organisation and workspace calendars to one. A shared calendar carries `_sharePermission`; `feedToken` is the owner's only.
        
        `GET /api/calendar/calendars`
        """
        return _pick(self._request("GET", f"/api/calendar/calendars", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_events(self, calendar_id: str, *, start: Optional[str] = None, end: Optional[str] = None, from_: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[CalendarEvent]:
        """Lists a calendar's events in a window, recurring ones expanded into their occurrences.
        
        With `start` and `end`: the events touching that window, each occurrence of a recurring event on its own (at most 1,000 rows). Without: the events around `from` (default now) unexpanded, at most 2,000. A private event on a calendar the caller may only view comes back as a busy block (`masked`).
        
        `GET /api/calendar/calendars/{calendarId}/events`
        """
        return _pick(self._request("GET", f"/api/calendar/calendars/{_seg(calendar_id)}/events", query={"start": start, "end": end, "from": from_}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_integration_calendars(self, id: str, *, options: Optional[RequestOptions] = None) -> CalendarListIntegrationCalendarsResponseData:
        """Lists a connected account's calendars and which of them are mirrored here.
        
        Asks the provider (502 when it does not answer). 400 when the account is no longer connected.
        
        `GET /api/calendar/integrations/{id}/calendars`
        """
        return _pick(self._request("GET", f"/api/calendar/integrations/{_seg(id)}/calendars", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_integrations(self, *, options: Optional[RequestOptions] = None) -> List[CalendarIntegration]:
        """Lists the caller's connected Google and Microsoft accounts.
        
        Connecting one happens in a browser; the tokens are never answered.
        
        `GET /api/calendar/integrations`
        """
        return _pick(self._request("GET", f"/api/calendar/integrations", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_proposals(self, *, options: Optional[RequestOptions] = None) -> List[CalendarListProposalsResponseDataPollsItem]:
        """Lists the caller's meeting polls, newest first, with their vote counts.
        
        The newest 100.
        
        `GET /api/calendar/proposals`
        """
        return _pick(self._request("GET", f"/api/calendar/proposals", query=None, body=None, multipart=False, options=options), "data.polls")  # type: ignore[no-any-return]

    def list_shares(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> List[CalendarShare]:
        """Lists whom a calendar is shared with.
        
        The calendar's owner only. Needs `calendar:share`. A person is named only when they share an organisation with the owner.
        
        `GET /api/calendar/calendars/{calendarId}/shares`
        """
        return _pick(self._request("GET", f"/api/calendar/calendars/{_seg(calendar_id)}/shares", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_waitlist(self, *, page_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[BookingWaitlistEntry]:
        """Lists the waiting lists of the caller's booking pages, in line order.
        
        `GET /api/calendar/booking-waitlist`
        """
        return _pick(self._request("GET", f"/api/calendar/booking-waitlist", query={"pageId": page_id}, body=None, multipart=False, options=options), "data.entries")  # type: ignore[no-any-return]

    def pull_caldav_sync(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> CalendarPullCaldavSyncResponseData:
        """Brings in now what changed in a calendar's CalDAV copy.
        
        The calendar's owner only. Needs `calendar:caldav_enable`; 409 when sync is off. `skipped` when nothing changed.
        
        `POST /api/calendar/calendars/{calendarId}/caldav-sync/refresh`
        """
        return _pick(self._request("POST", f"/api/calendar/calendars/{_seg(calendar_id)}/caldav-sync/refresh", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def refresh(self, *, options: Optional[RequestOptions] = None) -> CalendarRefreshResponseData:
        """Brings in now what changed in the caller's CalDAV calendars and connected accounts.
        
        At most once every 30 seconds; a call inside that answers `skipped: true`.
        
        `POST /api/calendar/refresh`
        """
        return _pick(self._request("POST", f"/api/calendar/refresh", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_attendee(self, event_id: str, *, email: str, options: Optional[RequestOptions] = None) -> CalendarRemoveAttendeeResponse:
        """Removes a guest from an event and tells them it is off.
        
        Events of calendars the caller owns.
        
        `DELETE /api/calendar/events/{eventId}/attendees`
        """
        return self._request("DELETE", f"/api/calendar/events/{_seg(event_id)}/attendees", query={"email": email}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def remove_waitlist_entry(self, entry_id: str, *, options: Optional[RequestOptions] = None) -> CalendarRemoveWaitlistEntryResponse:
        """Takes somebody off a booking page's waiting list; a slot held for them goes to the next in line.
        
        `DELETE /api/calendar/booking-waitlist/{entryId}`
        """
        return self._request("DELETE", f"/api/calendar/booking-waitlist/{_seg(entry_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def reschedule_booking(self, id: str, body: CalendarRescheduleBookingBody, *, options: Optional[RequestOptions] = None) -> CalendarRescheduleBookingResponseData:
        """Moves a booking to another time: as the host of its page, or as the guest with the reschedule token.
        
        The new time must be bookable on the page (409 otherwise); a guest also within its notice and advance limits. A new reschedule token is made.
        
        `POST /api/calendar/bookings/{id}/reschedule`
        """
        return _pick(self._request("POST", f"/api/calendar/bookings/{_seg(id)}/reschedule", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def revoke_calendar_feed(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> CalendarRevokeCalendarFeedResponse:
        """Switches a calendar's ICS subscription off until it is rotated.
        
        The calendar's owner only.
        
        `DELETE /api/calendar/calendars/{calendarId}/feed`
        """
        return self._request("DELETE", f"/api/calendar/calendars/{_seg(calendar_id)}/feed", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def rotate_calendar_feed(self, calendar_id: str, *, options: Optional[RequestOptions] = None) -> CalendarRotateCalendarFeedResponseData:
        """Makes a new ICS subscription URL; every old one stops working.
        
        The calendar's owner only. Also switches a revoked feed back on.
        
        `POST /api/calendar/calendars/{calendarId}/feed`
        """
        return _pick(self._request("POST", f"/api/calendar/calendars/{_seg(calendar_id)}/feed", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def search(self, *, q: str, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[CalendarSearchResponseDataResultsItem]:
        """Searches the events of the caller's own and shared calendars by title, description, place or guest.
        
        From 90 days back to a year ahead, newest first. Private events of calendars the caller may only view never match. 30 a minute; fewer than 2 characters answer nothing.
        
        `GET /api/calendar/search`
        """
        return _pick(self._request("GET", f"/api/calendar/search", query={"q": q, "limit": limit}, body=None, multipart=False, options=options), "data.results")  # type: ignore[no-any-return]

    def set_integration_calendars(self, id: str, body: CalendarSetIntegrationCalendarsBody, *, options: Optional[RequestOptions] = None) -> CalendarSetIntegrationCalendarsResponseData:
        """Chooses which of a connected account's calendars are mirrored here, then syncs.
        
        Each chosen one gets a calendar of its own; one no longer chosen goes to the trash here, its events stay at the provider.
        
        `PUT /api/calendar/integrations/{id}/calendars`
        """
        return _pick(self._request("PUT", f"/api/calendar/integrations/{_seg(id)}/calendars", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def sync_integration(self, id: str, *, options: Optional[RequestOptions] = None) -> CalendarSyncCounts:
        """Syncs a connected account now, both ways.
        
        `POST /api/calendar/integrations/{id}/sync`
        """
        return _pick(self._request("POST", f"/api/calendar/integrations/{_seg(id)}/sync", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def travel_estimate(self, body: CalendarTravelEstimateBody, *, options: Optional[RequestOptions] = None) -> CalendarTravelEstimateResponseData:
        """Estimates the travel time in minutes between two places.
        
        Needs the travel buffer feature. `minutes` is null when the platform has no maps provider. 30 a minute.
        
        `POST /api/calendar/travel-estimate`
        """
        return _pick(self._request("POST", f"/api/calendar/travel-estimate", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_booking_page(self, id: str, body: CalendarUpdateBookingPageBody, *, options: Optional[RequestOptions] = None) -> BookingPage:
        """Changes one of the caller's booking pages.
        
        Only the fields sent change.
        
        `PUT /api/calendar/booking-pages/{id}`
        """
        return _pick(self._request("PUT", f"/api/calendar/booking-pages/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_calendar(self, calendar_id: str, body: CalendarUpdateCalendarBody, *, options: Optional[RequestOptions] = None) -> Calendar:
        """Changes a calendar's name, description, colour, zone, visibility or settings.
        
        The calendar's owner only. Only the fields sent change.
        
        `PUT /api/calendar/calendars/{calendarId}`
        """
        return _pick(self._request("PUT", f"/api/calendar/calendars/{_seg(calendar_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_event(self, event_id: str, body: CalendarUpdateEventBody, *, options: Optional[RequestOptions] = None) -> CalendarEvent:
        """Changes an event of a calendar the caller owns; guests are told what changed.
        
        Only the fields sent change.
        
        `PUT /api/calendar/events/{eventId}`
        """
        return _pick(self._request("PUT", f"/api/calendar/events/{_seg(event_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_settings(self, body: CalendarUpdateSettingsBody, *, options: Optional[RequestOptions] = None) -> CalendarSettings:
        """Changes the caller's calendar preferences.
        
        Only the fields sent change; an unknown field is refused.
        
        `PUT /api/calendar/settings`
        """
        return _pick(self._request("PUT", f"/api/calendar/settings", query=None, body=body, multipart=False, options=options), "data.settings")  # type: ignore[no-any-return]

    def update_share(self, calendar_id: str, share_id: str, body: CalendarUpdateShareBody, *, options: Optional[RequestOptions] = None) -> CalendarShare:
        """Changes what a person a calendar is shared with may do.
        
        The calendar's owner only. Needs `calendar:share`.
        
        `PATCH /api/calendar/calendars/{calendarId}/shares/{shareId}`
        """
        return _pick(self._request("PATCH", f"/api/calendar/calendars/{_seg(calendar_id)}/shares/{_seg(share_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class CodeAssetsResource(_Resource):

    def get_text(self, asset_id: str, *, options: Optional[RequestOptions] = None) -> CodeAssetsGetTextResponse:
        """Returns the text of a file in the Assets hub, as the code editor opens it.
        
        For a text file up to 2 MB the caller can see. Otherwise 415 with `reason` (`excluded`, `not_text`, `too_large`), or 502 `unreadable`.
        
        `GET /api/code/assets/{assetId}`
        """
        return self._request("GET", f"/api/code/assets/{_seg(asset_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def save_text(self, asset_id: str, body: CodeAssetsSaveTextBody, *, options: Optional[RequestOptions] = None) -> CodeAssetsSaveTextResponse:
        """Replaces the text of a file in the Assets hub, keeping the previous content as a version.
        
        The asset keeps its id and URL, so what links to it shows the new text. Needs the right to manage the asset; at most 2 MB (413).
        
        `PUT /api/code/assets/{assetId}`
        """
        return self._request("PUT", f"/api/code/assets/{_seg(asset_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CodeDataResource(_Resource):

    def bind(self, project_id: str, body: CodeDataBindBody, *, options: Optional[RequestOptions] = None) -> CodeDataBindResponseBinding:
        """Lets a code project's code reach a database under an alias.
        
        Needs `code:update` and, on the database, read access (`access: read`) or edit access (`write`); the database must be the project's organization's. A refusal answers with `problem`: `not_found`, `forbidden`, `other_tenant`, `too_many`, `alias_taken` or the alias's shape.
        
        `POST /api/code/projects/{projectId}/data`
        """
        return _pick(self._request("POST", f"/api/code/projects/{_seg(project_id)}/data", query=None, body=body, multipart=False, options=options), "binding")  # type: ignore[no-any-return]

    def list(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[CodeDataBinding]:
        """Lists the databases a code project's code may reach, and those the caller could add.
        
        `GET /api/code/projects/{projectId}/data`
        """
        return _pick(self._request("GET", f"/api/code/projects/{_seg(project_id)}/data", query=None, body=None, multipart=False, options=options), "bindings")  # type: ignore[no-any-return]

    def unbind(self, project_id: str, *, binding_id: str, options: Optional[RequestOptions] = None) -> CodeDataUnbindResponse:
        """Stops a code project's code from reaching a database.
        
        Needs `code:update`.
        
        `DELETE /api/code/projects/{projectId}/data`
        """
        return self._request("DELETE", f"/api/code/projects/{_seg(project_id)}/data", query={"bindingId": binding_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, project_id: str, body: CodeDataUpdateBody, *, options: Optional[RequestOptions] = None) -> CodeDataUpdateResponseBinding:
        """Changes whether a code project may only read or also write a bound database.
        
        Needs `code:update`; `write` needs edit access to the database.
        
        `PATCH /api/code/projects/{projectId}/data`
        """
        return _pick(self._request("PATCH", f"/api/code/projects/{_seg(project_id)}/data", query=None, body=body, multipart=False, options=options), "binding")  # type: ignore[no-any-return]


class CodeDeploymentsResource(_Resource):

    def delete(self, project_id: str, *, environment: Optional[Literal["production", "staging"]] = None, options: Optional[RequestOptions] = None) -> CodeDeploymentsDeleteResponse:
        """Takes a published site down and frees its name.
        
        Needs `code:update`. `alreadyGone: true` when nothing was published.
        
        `DELETE /api/code/projects/{projectId}/deployments`
        """
        return self._request("DELETE", f"/api/code/projects/{_seg(project_id)}/deployments", query={"environment": environment}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[CodeDeploymentsListResponseDeploymentsItem]:
        """Lists a code project's published sites, with their containers and this month's compute use.
        
        `GET /api/code/projects/{projectId}/deployments`
        """
        return _pick(self._request("GET", f"/api/code/projects/{_seg(project_id)}/deployments", query=None, body=None, multipart=False, options=options), "deployments")  # type: ignore[no-any-return]

    def logs(self, project_id: str, *, environment: Optional[Literal["production", "staging"]] = None, options: Optional[RequestOptions] = None) -> CodeDeploymentsLogsResponse:
        """Returns the last 200 lines a published site's container wrote.
        
        `live: false` is what was captured when the container stopped (`reason`: `stopped` or `unreachable`). 404 with `reason: not_published` when the environment is not published.
        
        `GET /api/code/projects/{projectId}/deployments/logs`
        """
        return self._request("GET", f"/api/code/projects/{_seg(project_id)}/deployments/logs", query={"environment": environment}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def publish(self, project_id: str, body: CodeDeploymentsPublishBody, *, options: Optional[RequestOptions] = None) -> CodeDeployment:
        """Publishes a code project as a site, or publishes it again.
        
        Needs `code:update`. Builds the current files in a container of their own and runs the project's start script; the answer comes when it is up. The first publish of an environment takes `slug`; the plan's environments and deployments apply. A refusal answers with `reason`: `no_domain` or `not_enabled` (403), `slug` with `problem` (`too_short`, `too_long`, `shape`, `taken`), `no_start_script` (400), `limit` (403).
        
        `POST /api/code/projects/{projectId}/deployments`
        """
        return _pick(self._request("POST", f"/api/code/projects/{_seg(project_id)}/deployments", query=None, body=body, multipart=False, options=options), "deployment")  # type: ignore[no-any-return]

    def remove_domain(self, project_id: str, *, environment: Optional[Literal["production", "staging"]] = None, options: Optional[RequestOptions] = None) -> CodeDeploymentsRemoveDomainResponse:
        """Removes a published site's custom domain.
        
        Needs `code:update`.
        
        `DELETE /api/code/projects/{projectId}/deployments/domain`
        """
        return self._request("DELETE", f"/api/code/projects/{_seg(project_id)}/deployments/domain", query={"environment": environment}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set_domain(self, project_id: str, body: CodeDeploymentsSetDomainBody, *, environment: Optional[Literal["production", "staging"]] = None, options: Optional[RequestOptions] = None) -> CodeDeploymentsSetDomainResponse:
        """Claims a custom domain for a published site.
        
        Needs `code:update`, custom domains on the plan and a published environment (409 otherwise). The domain is pending until `code.deployments.verifyDomain` finds the TXT `record` the answer names.
        
        `PUT /api/code/projects/{projectId}/deployments/domain`
        """
        return self._request("PUT", f"/api/code/projects/{_seg(project_id)}/deployments/domain", query={"environment": environment}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, project_id: str, body: CodeDeploymentsUpdateBody, *, options: Optional[RequestOptions] = None) -> CodeDeploymentsUpdateResponseDeployment:
        """Turns a required sign-in on or off for a published site, without publishing again.
        
        Needs `code:update`. Visitors sign in as the workspace's site users, so turning it on needs a project with a workspace (400 `problem: no_workspace`).
        
        `PATCH /api/code/projects/{projectId}/deployments`
        """
        return _pick(self._request("PATCH", f"/api/code/projects/{_seg(project_id)}/deployments", query=None, body=body, multipart=False, options=options), "deployment")  # type: ignore[no-any-return]

    def verify_domain(self, project_id: str, *, environment: Optional[Literal["production", "staging"]] = None, options: Optional[RequestOptions] = None) -> CodeDeploymentsVerifyDomainResponse:
        """Checks a site's custom domain for its TXT record and marks it verified when it is there.
        
        Needs `code:update`.
        
        `POST /api/code/projects/{projectId}/deployments/domain`
        """
        return self._request("POST", f"/api/code/projects/{_seg(project_id)}/deployments/domain", query={"environment": environment}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class CodeEnvResource(_Resource):

    def delete(self, project_id: str, *, key: str, options: Optional[RequestOptions] = None) -> CodeEnvDeleteResponse:
        """Removes an environment variable of a code project.
        
        Needs `code:update`. Applies on the container's next start.
        
        `DELETE /api/code/projects/{projectId}/env`
        """
        return self._request("DELETE", f"/api/code/projects/{_seg(project_id)}/env", query={"key": key}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[CodeEnvVariable]:
        """Lists a code project's environment variables, without their values.
        
        `GET /api/code/projects/{projectId}/env`
        """
        return _pick(self._request("GET", f"/api/code/projects/{_seg(project_id)}/env", query=None, body=None, multipart=False, options=options), "variables")  # type: ignore[no-any-return]

    def set(self, project_id: str, body: CodeEnvSetBody, *, options: Optional[RequestOptions] = None) -> CodeEnvSetResponse:
        """Sets an environment variable of a code project.
        
        Needs `code:update`. Stored encrypted; the value never comes back. A running container keeps the environment it started with — the change applies on its next start. A refusal answers 400 with `problem`: `shape`, `too_long`, `reserved`, `value_too_long` or `too_many`.
        
        `PUT /api/code/projects/{projectId}/env`
        """
        return self._request("PUT", f"/api/code/projects/{_seg(project_id)}/env", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CodeFilesResource(_Resource):

    def create(self, project_id: str, body: CodeFilesCreateBody, *, options: Optional[RequestOptions] = None) -> CodeFile:
        """Creates a file in a code project.
        
        Needs `code:update`. Text up to 1 MB; a non-text file is uploaded to the Assets hub and added here by `assetId`. 409 when the path exists; the project's file count and storage limits apply.
        
        `POST /api/code/projects/{projectId}/files`
        """
        return _pick(self._request("POST", f"/api/code/projects/{_seg(project_id)}/files", query=None, body=body, multipart=False, options=options), "file")  # type: ignore[no-any-return]

    def delete(self, project_id: str, *, path: str, recursive: Optional[bool] = None, options: Optional[RequestOptions] = None) -> CodeFilesDeleteResponse:
        """Deletes a file, or a folder with everything in it.
        
        Needs `code:update`.
        
        `DELETE /api/code/projects/{projectId}/files`
        """
        return self._request("DELETE", f"/api/code/projects/{_seg(project_id)}/files", query={"path": path, "recursive": recursive}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, project_id: str, *, path: str, options: Optional[RequestOptions] = None) -> CodeFile:
        """Returns one file of a code project, with its content.
        
        While the project's container runs, the content is the container's; `stale: true` means the container did not answer in time and the last saved copy was served.
        
        `GET /api/code/projects/{projectId}/files`
        """
        return _pick(self._request("GET", f"/api/code/projects/{_seg(project_id)}/files", query={"path": path}, body=None, multipart=False, options=options), "file")  # type: ignore[no-any-return]

    def update(self, project_id: str, body: CodeFilesUpdateBody, *, options: Optional[RequestOptions] = None) -> CodeFilesUpdateResponse:
        """Saves a file's content, or renames or moves a file or a folder.
        
        Needs `code:update`. With `newPath` the file — or the folder and everything in it — moves there and the answer carries `moved`; otherwise `content` is saved and the answer carries the `file`, or `unchanged: true` when nothing changed.
        
        `PATCH /api/code/projects/{projectId}/files`
        """
        return self._request("PATCH", f"/api/code/projects/{_seg(project_id)}/files", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CodeGitCredentialsResource(_Resource):

    def create(self, body: CodeGitCredentialsCreateBody, *, options: Optional[RequestOptions] = None) -> CodeGitCredential:
        """Stores a git host access token, after the host accepted it.
        
        Needs `code:update`; a credential shared with an organization (`scope: organization`) also needs `organization:update`. The token is stored encrypted and never comes back.
        
        `POST /api/code/git/credentials`
        """
        return _pick(self._request("POST", f"/api/code/git/credentials", query=None, body=body, multipart=False, options=options), "credential")  # type: ignore[no-any-return]

    def delete(self, *, id: str, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> CodeGitCredentialsDeleteResponse:
        """Deletes a git credential or a signed-in GitHub account.
        
        `DELETE /api/code/git/credentials`
        """
        return self._request("DELETE", f"/api/code/git/credentials", query={"id": id, "workspaceId": workspace_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[CodeGitCredential]:
        """Lists the git credentials the caller may use, without their tokens.
        
        The caller's own tokens and their organizations' shared ones; with `workspaceId`, also the GitHub accounts signed in to in that workspace.
        
        `GET /api/code/git/credentials`
        """
        return _pick(self._request("GET", f"/api/code/git/credentials", query={"organizationId": organization_id, "workspaceId": workspace_id}, body=None, multipart=False, options=options), "credentials")  # type: ignore[no-any-return]


class CodeGitResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.credentials = CodeGitCredentialsResource(request)

    def connect(self, project_id: str, body: CodeGitConnectBody, *, options: Optional[RequestOptions] = None) -> CodeGitConnectResponse:
        """Connects a code project to a repository, or disconnects it.
        
        Needs `code:update`. Without `remoteUrl` the project is disconnected. Give a credential the caller may use (`code.git.credentials.list`): `credentialId` for a token, `connectionId` for a signed-in GitHub account.
        
        `PUT /api/code/projects/{projectId}/git`
        """
        return self._request("PUT", f"/api/code/projects/{_seg(project_id)}/git", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def history(self, project_id: str, *, sha: Optional[str] = None, path: Optional[str] = None, branches: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> CodeGitHistoryResponse:
        """Lists the commits of a code project's branch, its branches, one commit's changes, or one file as last synced.
        
        One of: nothing — the branch's latest 30 commits (`commits`); `branches=1` — the repository's branches; `sha` — that commit's `message` and `files` with their diffs; `path` — that file's `content` at the commit the project last synced to (null when there is none).
        
        `GET /api/code/projects/{projectId}/git/history`
        """
        return self._request("GET", f"/api/code/projects/{_seg(project_id)}/git/history", query={"sha": sha, "path": path, "branches": branches}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def repos(self, *, credential_id: Optional[str] = None, connection_id: Optional[str] = None, workspace_id: Optional[str] = None, repo: Optional[str] = None, options: Optional[RequestOptions] = None) -> CodeGitReposResponse:
        """Lists the repositories a git credential can push to, or one repository's branches.
        
        Give `credentialId` or `connectionId` (with its `workspaceId`). With `repo`, the answer is that repository's `branches` instead of `repos`.
        
        `GET /api/code/git/repos`
        """
        return self._request("GET", f"/api/code/git/repos", query={"credentialId": credential_id, "connectionId": connection_id, "workspaceId": workspace_id, "repo": repo}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def status(self, project_id: str, *, options: Optional[RequestOptions] = None) -> CodeGitStatusResponse:
        """Returns a code project's repository connection and what differs from it.
        
        Needs Git sync on the account. `connected: false` with a `reason` when there is no repository or no usable credential.
        
        `GET /api/code/projects/{projectId}/git`
        """
        return self._request("GET", f"/api/code/projects/{_seg(project_id)}/git", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def sync(self, project_id: str, body: CodeGitSyncBody, *, options: Optional[RequestOptions] = None) -> CodeGitSyncResponse:
        """Pulls from, pushes to, or switches the branch of a code project's repository.
        
        Needs `code:update`. `pull` refuses to overwrite local changes unless `force`; `push` makes one commit of what changed and refuses when the branch moved since the last sync; `switch-branch` refuses with local changes (409) unless `force`, which discards them.
        
        `POST /api/code/projects/{projectId}/git`
        """
        return self._request("POST", f"/api/code/projects/{_seg(project_id)}/git", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CodeProjectsResource(_Resource):

    def create(self, body: CodeProjectsCreateBody, *, options: Optional[RequestOptions] = None) -> CodeProject:
        """Creates a code project, from a template or with a starter file.
        
        Needs `code:create` and the Coding hub on the plan; counts against the organization's `max_code_projects`. Without `template` the project starts with the language's starter file, unless `empty` is true.
        
        `POST /api/code/projects`
        """
        return _pick(self._request("POST", f"/api/code/projects", query=None, body=body, multipart=False, options=options), "project")  # type: ignore[no-any-return]

    def delete(self, project_id: str, *, options: Optional[RequestOptions] = None) -> CodeProjectsDeleteResponse:
        """Moves a code project to the trash.
        
        Needs `code:delete`, and only the owner may. What runs stops and its sites go offline; the files wait in the trash until it is deleted for good.
        
        `DELETE /api/code/projects/{projectId}`
        """
        return self._request("DELETE", f"/api/code/projects/{_seg(project_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def download(self, project_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a code project's files as a ZIP file.
        
        Answers the file itself (`application/zip`), not JSON. Uploaded files live in the Assets hub and are only listed, in `UPLOADS.txt`.
        
        `GET /api/code/projects/{projectId}/download`
        """
        return self._request("GET", f"/api/code/projects/{_seg(project_id)}/download", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, project_id: str, *, options: Optional[RequestOptions] = None) -> CodeProjectsGetResponse:
        """Returns a code project with its file tree, without the files' contents.
        
        Read a file's content with `code.files.get`.
        
        `GET /api/code/projects/{projectId}`
        """
        return self._request("GET", f"/api/code/projects/{_seg(project_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: Optional[str] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[CodeProjectsListResponseProjectsItem]:
        """Lists the caller's code projects, and the shared ones of a workspace or organization.
        
        Always the caller's own. With `workspaceId`, also that workspace's projects shared with it; with `organizationId`, also the organization's projects shared with it — each only where the caller belongs. Most recently opened first; projects in the trash are left out.
        
        `GET /api/code/projects`
        """
        return _pick(self._request("GET", f"/api/code/projects", query={"workspaceId": workspace_id, "organizationId": organization_id}, body=None, multipart=False, options=options), "projects")  # type: ignore[no-any-return]

    def update(self, project_id: str, body: CodeProjectsUpdateBody, *, options: Optional[RequestOptions] = None) -> CodeProject:
        """Renames, describes, archives or re-scopes a code project.
        
        Needs `code:update`. Only the owner may change `visibility`; people who lose write access are disconnected from live editing at once.
        
        `PATCH /api/code/projects/{projectId}`
        """
        return _pick(self._request("PATCH", f"/api/code/projects/{_seg(project_id)}", query=None, body=body, multipart=False, options=options), "project")  # type: ignore[no-any-return]


class CodeResource(_Resource):
    """Coding hub — Code projects: their files, environment variables, git sync, the databases their code may reach, and the sites they are published as.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.assets = CodeAssetsResource(request)
        self.data = CodeDataResource(request)
        self.deployments = CodeDeploymentsResource(request)
        self.env = CodeEnvResource(request)
        self.files = CodeFilesResource(request)
        self.git = CodeGitResource(request)
        self.projects = CodeProjectsResource(request)

    def storage(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> CodeStorageResponse:
        """Returns how much code storage each project the caller can open uses.
        
        Uploaded files count in the Assets hub, not here.
        
        `GET /api/code/storage`
        """
        return self._request("GET", f"/api/code/storage", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class CommunityResource(_Resource):
    """Community — Community hubs — forums with members, posts, replies, polls, AMAs, tags, invitations, join requests, reputation and moderation. A hub is named by its slug. Creating and changing things needs Community on the caller's plan; what a caller may do in a hub follows their role there (owner, moderator, member).
    """

    def accept_answer(self, slug: str, post_id: str, body: CommunityAcceptAnswerBody, *, options: Optional[RequestOptions] = None) -> CommunityAcceptAnswerResponseData:
        """Marks a reply as a question's accepted answer.
        
        The question's author or a moderator. Its author earns reputation.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/accept-answer`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/accept-answer", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def accept_invite(self, token: str, *, options: Optional[RequestOptions] = None) -> CommunityAcceptInviteResponseData:
        """Joins a hub with an invitation.
        
        409 when already a member, 404 when the invitation is expired or used up.
        
        `POST /api/community/invites/{token}`
        """
        return _pick(self._request("POST", f"/api/community/invites/{_seg(token)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def ai_summarize(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityAiSummarizeResponseData:
        """An AI summary of a post's discussion.
        
        Null with `reason: not_enough_replies` for a short one. Cached until ten more replies arrive. Not for a person who opted out of AI.
        
        `GET /api/community/hubs/{slug}/posts/{postId}/summary`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/summary", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def ama_recap(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityAmaRecapResponseData:
        """Writes the recap post of an AMA.
        
        The AMA's host or a moderator; needs the AMA feature.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/recap`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/recap", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def approve_post(self, slug: str, post_id: str, body: CommunityApprovePostBody, *, options: Optional[RequestOptions] = None) -> CommunityApprovePostResponseData:
        """Publishes a post waiting for review, or rejects it.
        
        The hub's owner and moderators only.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/approve`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/approve", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def approve_reply(self, slug: str, reply_id: str, body: CommunityApproveReplyBody, *, options: Optional[RequestOptions] = None) -> CommunityApproveReplyResponseData:
        """Publishes a reply waiting for review, or rejects it.
        
        The hub's owner and moderators only.
        
        `POST /api/community/hubs/{slug}/replies/{replyId}/approve`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/replies/{_seg(reply_id)}/approve", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def become_member(self, slug: str, body: CommunityBecomeMemberBody, *, options: Optional[RequestOptions] = None) -> Union[CommunityBecomeMemberResponseData, CommunityBecomeMemberResponseData2]:
        """Joins a hub and answers the membership, or the join request when it needs approval.
        
        Like POST …/join, with the row in the answer. 409 when already a member or already asked.
        
        `POST /api/community/hubs/{slug}/members`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/members", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def bookmark_post(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityBookmarkPostResponse:
        """Saves a post to the caller's bookmarks.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/bookmark`
        """
        return self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/bookmark", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def clear_accepted_answer(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityClearAcceptedAnswerResponse:
        """Takes back a question's accepted answer.
        
        The question's author or a moderator.
        
        `DELETE /api/community/hubs/{slug}/posts/{postId}/accept-answer`
        """
        return self._request("DELETE", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/accept-answer", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def create_hub(self, body: CommunityCreateHubBody, *, options: Optional[RequestOptions] = None) -> CommunityHub:
        """Creates a hub with the caller as its owner; the slug is made from the name.
        
        Needs `community:create_hub`. An organisation's hub counts against its plan's hub limit. Five an hour.
        
        `POST /api/community/hubs`
        """
        return _pick(self._request("POST", f"/api/community/hubs", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_invite(self, slug: str, body: CommunityCreateInviteBody, *, options: Optional[RequestOptions] = None) -> CommunityInvite:
        """Creates an invitation link to a hub, mailed when an address is given.
        
        The hub's owner and moderators only. Only the owner invites moderators. 40 an hour.
        
        `POST /api/community/hubs/{slug}/invites`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/invites", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_post(self, slug: str, body: CommunityCreatePostBody, *, options: Optional[RequestOptions] = None) -> CommunityPost:
        """Posts in a hub.
        
        Active members only. With post approval or AI moderation on, it may wait for a moderator (`status: pending`). An AMA needs a moderator, the AMA feature and its start and end. Rate-limited.
        
        `POST /api/community/hubs/{slug}/posts`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_reply(self, slug: str, post_id: str, body: CommunityCreateReplyBody, *, options: Optional[RequestOptions] = None) -> CommunityCreateReplyResponseData:
        """Replies to a post, or to a reply on it.
        
        Active members; a locked post only takes moderators' replies. Two levels deep at most. With moderation on it may wait for review (`pending`). The author and those mentioned are told.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/replies`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/replies", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_tag(self, slug: str, body: CommunityCreateTagBody, *, options: Optional[RequestOptions] = None) -> CommunityTag:
        """Adds a tag to a hub.
        
        The hub's owner and moderators only. 409 when a tag of that name exists.
        
        `POST /api/community/hubs/{slug}/tags`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/tags", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_draft(self, slug: str, *, options: Optional[RequestOptions] = None) -> CommunityDeleteDraftResponse:
        """Discards the caller's unfinished post in a hub.
        
        `DELETE /api/community/hubs/{slug}/drafts`
        """
        return self._request("DELETE", f"/api/community/hubs/{_seg(slug)}/drafts", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_hub(self, slug: str, *, options: Optional[RequestOptions] = None) -> CommunityDeleteHubResponse:
        """Deletes a hub with everything in it, for good.
        
        Its owner only.
        
        `DELETE /api/community/hubs/{slug}`
        """
        return self._request("DELETE", f"/api/community/hubs/{_seg(slug)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_post(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityDeletePostResponse:
        """Deletes a post.
        
        Its author or a moderator.
        
        `DELETE /api/community/hubs/{slug}/posts/{postId}`
        """
        return self._request("DELETE", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_reply(self, slug: str, post_id: str, reply_id: str, *, options: Optional[RequestOptions] = None) -> CommunityDeleteReplyResponse:
        """Deletes a reply.
        
        Its author or a moderator.
        
        `DELETE /api/community/hubs/{slug}/posts/{postId}/replies/{replyId}`
        """
        return self._request("DELETE", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/replies/{_seg(reply_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def feed(self, *, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[CommunityFeedResponseDataPostsItem]:
        """The newest posts of the hubs the caller is an active member of.
        
        `GET /api/community/feed`
        """
        return _pick(self._request("GET", f"/api/community/feed", query={"limit": limit}, body=None, multipart=False, options=options), "data.posts")  # type: ignore[no-any-return]

    def get_draft(self, slug: str, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """The caller's unfinished post in a hub, or null.
        
        One draft per person and hub; active members only.
        
        `GET /api/community/hubs/{slug}/drafts`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/drafts", query=None, body=None, multipart=False, options=options), "data.draft")  # type: ignore[no-any-return]

    def get_hub(self, slug: str, *, options: Optional[RequestOptions] = None) -> CommunityGetHubResponseData:
        """One hub, with the caller's role and status in it.
        
        A hub that is not public or unlisted only for its members (and, for an organisation or workspace hub, that organisation's or workspace's members).
        
        `GET /api/community/hubs/{slug}`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_invite(self, token: str, *, options: Optional[RequestOptions] = None) -> CommunityGetInviteResponseData:
        """What an invitation leads to: the hub, who invited, the role and until when.
        
        `GET /api/community/invites/{token}`
        """
        return _pick(self._request("GET", f"/api/community/invites/{_seg(token)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_member_badges(self, slug: str, member_id: str, *, options: Optional[RequestOptions] = None) -> CommunityGetMemberBadgesResponseData:
        """A member's badges and reputation in a hub.
        
        Needs community gamification switched on. A hub that is not public or unlisted only for its active members.
        
        `GET /api/community/hubs/{slug}/members/{memberId}/badges`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/members/{_seg(member_id)}/badges", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_member_profile(self, slug: str, member_id: str, *, options: Optional[RequestOptions] = None) -> CommunityGetMemberProfileResponseData:
        """A member's profile in a hub: who they are, their role, badges and latest posts and replies.
        
        E-mail and the extended profile only where the member allows it (always for themselves and moderators).
        
        `GET /api/community/hubs/{slug}/members/{memberId}/profile`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/members/{_seg(member_id)}/profile", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_post(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityGetPostResponseData:
        """One post with its author, hub, reaction counts and what the caller did on it.
        
        Counts one view per person a day.
        
        `GET /api/community/hubs/{slug}/posts/{postId}`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def join(self, slug: str, *, options: Optional[RequestOptions] = None) -> CommunityJoinResponseData:
        """Joins a hub, or asks to when it needs approval.
        
        A private or invitation-only hub is joined through an invitation (403).
        
        `POST /api/community/hubs/{slug}/join`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/join", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def leaderboard(self, slug: str, *, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[CommunityLeaderboardResponseDataLeaderboardItem]:
        """A hub's members with the most reputation, with their top badges.
        
        Needs community gamification switched on. A hub that is not public or unlisted only for its active members.
        
        `GET /api/community/hubs/{slug}/leaderboard`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/leaderboard", query={"limit": limit}, body=None, multipart=False, options=options), "data.leaderboard")  # type: ignore[no-any-return]

    def leave(self, slug: str, *, options: Optional[RequestOptions] = None) -> CommunityLeaveResponse:
        """Leaves a hub.
        
        Its owner cannot leave: transfer it or delete it first.
        
        `DELETE /api/community/hubs/{slug}/join`
        """
        return self._request("DELETE", f"/api/community/hubs/{_seg(slug)}/join", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_bookmarks(self, *, options: Optional[RequestOptions] = None) -> List[CommunityListBookmarksResponseDataBookmarksItem]:
        """Lists the caller's bookmarked posts across hubs, newest first.
        
        At most 100.
        
        `GET /api/community/bookmarks`
        """
        return _pick(self._request("GET", f"/api/community/bookmarks", query=None, body=None, multipart=False, options=options), "data.bookmarks")  # type: ignore[no-any-return]

    def list_hubs(self, *, page: Optional[int] = None, category: Optional[CommunityCategory] = None, visibility: Optional[CommunityHubVisibility] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> CommunityListHubsResponseData:
        """Lists one page of the hubs the caller can see, biggest first: public ones and those they belong to.
        
        20 a page. Archived hubs are left out.
        
        `GET /api/community/hubs`
        """
        return _pick(self._request("GET", f"/api/community/hubs", query={"page": page, "category": category, "visibility": visibility, "organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_invites(self, slug: str, *, options: Optional[RequestOptions] = None) -> List[CommunityInvite]:
        """Lists a hub's invitations.
        
        The hub's owner and moderators only.
        
        `GET /api/community/hubs/{slug}/invites`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/invites", query=None, body=None, multipart=False, options=options), "data.invites")  # type: ignore[no-any-return]

    def list_join_requests(self, slug: str, *, options: Optional[RequestOptions] = None) -> List[CommunityListJoinRequestsResponseDataRequestsItem]:
        """Lists a hub's open join requests, newest first.
        
        The hub's owner and moderators only.
        
        `GET /api/community/hubs/{slug}/join-requests`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/join-requests", query=None, body=None, multipart=False, options=options), "data.requests")  # type: ignore[no-any-return]

    def list_members(self, slug: str, *, page: Optional[int] = None, status: Optional[Literal["active", "banned", "pending", "all"]] = None, options: Optional[RequestOptions] = None) -> CommunityListMembersResponseData:
        """Lists one page of a hub's members, newest first, with their post counts and badges.
        
        20 a page. Moderators may list other statuses and see e-mail addresses; everybody else sees active members.
        
        `GET /api/community/hubs/{slug}/members`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/members", query={"page": page, "status": status}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_posts(self, slug: str, *, page: Optional[int] = None, sort: Optional[Literal["createdAt", "upvoteCount", "replyCount"]] = None, type_: Optional[CommunityPostType] = None, tag: Optional[str] = None, status: Optional[Literal["pending"]] = None, options: Optional[RequestOptions] = None) -> CommunityListPostsResponseData:
        """Lists one page of a hub's posts, pinned first.
        
        20 a page. Poll options come with their counts and the caller's own vote (`userVotedIndex`, -1 for none). `status=pending` lists the review queue, for moderators.
        
        `GET /api/community/hubs/{slug}/posts`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/posts", query={"page": page, "sort": sort, "type": type_, "tag": tag, "status": status}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_replies(self, slug: str, post_id: str, *, page: Optional[int] = None, options: Optional[RequestOptions] = None) -> CommunityListRepliesResponseData:
        """Lists one page of a post's replies, the accepted answer first, each with the replies under it.
        
        20 top-level replies a page. A deleted reply that was answered stays as a placeholder.
        
        `GET /api/community/hubs/{slug}/posts/{postId}/replies`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/replies", query={"page": page}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_reputation_events(self, slug: str, member_id: str, *, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[CommunityListReputationEventsResponseDataEventsItem]:
        """How a member's reputation in a hub came about, newest first.
        
        Needs community gamification switched on. The member themselves or a moderator.
        
        `GET /api/community/hubs/{slug}/members/{memberId}/reputation-events`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/members/{_seg(member_id)}/reputation-events", query={"limit": limit}, body=None, multipart=False, options=options), "data.events")  # type: ignore[no-any-return]

    def list_tags(self, slug: str, *, options: Optional[RequestOptions] = None) -> List[CommunityTag]:
        """Lists a hub's tags.
        
        `GET /api/community/hubs/{slug}/tags`
        """
        return _pick(self._request("GET", f"/api/community/hubs/{_seg(slug)}/tags", query=None, body=None, multipart=False, options=options), "data.tags")  # type: ignore[no-any-return]

    def lock_post(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityLockPostResponseData:
        """Locks a post against new replies, or unlocks it.
        
        The hub's owner and moderators only. Each call flips it.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/lock`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/lock", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def moderation(self, *, hub_id: Optional[str] = None, tab: Optional[Literal["queue", "reports", "activity"]] = None, page: Optional[int] = None, page_size: Optional[int] = None, options: Optional[RequestOptions] = None) -> CommunityModerationResponseData:
        """The caller's moderation work across the hubs they moderate: the review queue, open reports and recent activity.
        
        The tab named in `tab` comes back as the page asked for; the other two as a preview of five.
        
        `GET /api/community/moderation`
        """
        return _pick(self._request("GET", f"/api/community/moderation", query={"hubId": hub_id, "tab": tab, "page": page, "pageSize": page_size}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def pin_post(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityPinPostResponseData:
        """Pins a post to the top of its hub, or unpins it.
        
        The hub's owner and moderators only. Each call flips it.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/pin`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/pin", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def react_post(self, slug: str, post_id: str, body: CommunityReactPostBody, *, options: Optional[RequestOptions] = None) -> CommunityReactPostResponseData:
        """Adds an emoji reaction to a post, or takes it back.
        
        Active members only. Each call with the same emoji flips it.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/react`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/react", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def react_reply(self, slug: str, post_id: str, reply_id: str, body: CommunityReactReplyBody, *, options: Optional[RequestOptions] = None) -> CommunityReactReplyResponseData:
        """Adds an emoji reaction to a reply, or takes it back.
        
        Members only. Each call with the same emoji flips it.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/replies/{replyId}/react`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/replies/{_seg(reply_id)}/react", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_member(self, slug: str, member_id: str, *, options: Optional[RequestOptions] = None) -> CommunityRemoveMemberResponse:
        """Removes a member from a hub.
        
        A moderator, or the member themselves. The owner cannot be removed by anybody else.
        
        `DELETE /api/community/hubs/{slug}/members/{memberId}`
        """
        return self._request("DELETE", f"/api/community/hubs/{_seg(slug)}/members/{_seg(member_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def report(self, body: CommunityReportBody, *, options: Optional[RequestOptions] = None) -> CommunityReportResponseData:
        """Reports a post or reply to the hub's moderators.
        
        Members of the hub; not one's own content. Reporting the same thing again answers the open report (`duplicate: true`). 30 an hour.
        
        `POST /api/community/reports`
        """
        return _pick(self._request("POST", f"/api/community/reports", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def resolve_join_request(self, slug: str, request_id: str, body: CommunityResolveJoinRequestBody, *, options: Optional[RequestOptions] = None) -> CommunityResolveJoinRequestResponseData:
        """Lets somebody into a hub or turns them away; they are told either way.
        
        The hub's owner and moderators only. 409 when already decided.
        
        `PUT /api/community/hubs/{slug}/join-requests/{requestId}`
        """
        return _pick(self._request("PUT", f"/api/community/hubs/{_seg(slug)}/join-requests/{_seg(request_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def resolve_report(self, id: str, body: CommunityResolveReportBody, *, options: Optional[RequestOptions] = None) -> CommunityResolveReportResponseData:
        """Settles a report: dismiss it, remove the content, or ban its author from the hub.
        
        The hub's moderators. 409 when already settled.
        
        `PATCH /api/community/moderation/reports/{id}`
        """
        return _pick(self._request("PATCH", f"/api/community/moderation/reports/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def save_draft(self, slug: str, body: CommunitySaveDraftBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Saves the caller's unfinished post in a hub, replacing the one before.
        
        `PUT /api/community/hubs/{slug}/drafts`
        """
        return _pick(self._request("PUT", f"/api/community/hubs/{_seg(slug)}/drafts", query=None, body=body, multipart=False, options=options), "data.draft")  # type: ignore[no-any-return]

    def search(self, *, q: str, hub: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[CommunitySearchResponseDataPostsItem]:
        """Searches the posts of public hubs and of the hubs the caller belongs to, newest first.
        
        At most 30. An unlisted hub is searched only when named in `hub`. Fewer than 2 characters answer nothing.
        
        `GET /api/community/search`
        """
        return _pick(self._request("GET", f"/api/community/search", query={"q": q, "hub": hub}, body=None, multipart=False, options=options), "data.posts")  # type: ignore[no-any-return]

    def transfer_hub(self, slug: str, body: CommunityTransferHubBody, *, options: Optional[RequestOptions] = None) -> CommunityTransferHubResponse:
        """Hands a hub to another of its active members; the old owner becomes a moderator.
        
        Its owner only.
        
        `POST /api/community/hubs/{slug}/transfer`
        """
        return self._request("POST", f"/api/community/hubs/{_seg(slug)}/transfer", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def unbookmark_post(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityUnbookmarkPostResponse:
        """Removes a post from the caller's bookmarks.
        
        `DELETE /api/community/hubs/{slug}/posts/{postId}/bookmark`
        """
        return self._request("DELETE", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/bookmark", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_hub(self, slug: str, body: CommunityUpdateHubBody, *, options: Optional[RequestOptions] = None) -> CommunityHub:
        """Changes a hub: its texts, look, visibility, joining, moderation settings, slug or archive state.
        
        The hub's owner and moderators only. Only the fields sent change; `settings` is merged into what is stored. A new slug must be free (409).
        
        `PUT /api/community/hubs/{slug}`
        """
        return _pick(self._request("PUT", f"/api/community/hubs/{_seg(slug)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_member(self, slug: str, member_id: str, body: CommunityUpdateMemberBody, *, options: Optional[RequestOptions] = None) -> CommunityMember:
        """Changes a member's role, bans or unbans them, or mutes them for a while.
        
        The hub's owner and moderators only. Only the owner can touch the owner or make somebody owner.
        
        `PUT /api/community/hubs/{slug}/members/{memberId}`
        """
        return _pick(self._request("PUT", f"/api/community/hubs/{_seg(slug)}/members/{_seg(member_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_post(self, slug: str, post_id: str, body: CommunityUpdatePostBody, *, options: Optional[RequestOptions] = None) -> CommunityPost:
        """Edits a post.
        
        Its author within 30 minutes of posting, or a moderator at any time.
        
        `PUT /api/community/hubs/{slug}/posts/{postId}`
        """
        return _pick(self._request("PUT", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_reply(self, slug: str, post_id: str, reply_id: str, body: CommunityUpdateReplyBody, *, options: Optional[RequestOptions] = None) -> CommunityReply:
        """Edits a reply.
        
        Its author only.
        
        `PUT /api/community/hubs/{slug}/posts/{postId}/replies/{replyId}`
        """
        return _pick(self._request("PUT", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/replies/{_seg(reply_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def upvote_post(self, slug: str, post_id: str, *, options: Optional[RequestOptions] = None) -> CommunityUpvotePostResponseData:
        """Upvotes a post, or takes the upvote back.
        
        Active members only. Each call flips it.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/upvote`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/upvote", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def upvote_reply(self, slug: str, post_id: str, reply_id: str, *, options: Optional[RequestOptions] = None) -> CommunityUpvoteReplyResponseData:
        """Upvotes a reply, or takes the upvote back.
        
        Active members only. Each call flips it.
        
        `POST /api/community/hubs/{slug}/posts/{postId}/replies/{replyId}/upvote`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/replies/{_seg(reply_id)}/upvote", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def vote_poll(self, slug: str, post_id: str, body: CommunityVotePollBody, *, options: Optional[RequestOptions] = None) -> CommunityVotePollResponseData:
        """Votes in a poll; voting for the same option again takes the vote back.
        
        Members; in a public, open hub voting joins it. Someone banned from the hub is refused (403).
        
        `POST /api/community/hubs/{slug}/posts/{postId}/vote`
        """
        return _pick(self._request("POST", f"/api/community/hubs/{_seg(slug)}/posts/{_seg(post_id)}/vote", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ConnectionsResource(_Resource):
    """Connections — Credentials for the services workflows talk to.
    """

    def create(self, body: CreateConnectionInput, *, options: Optional[RequestOptions] = None) -> Connection:
        """Stores credentials for an integration as a connection.
        
        `POST /api/connections`
        """
        return self._request("POST", f"/api/connections", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> ConnectionsDeleteResponse:
        """Deletes a connection; workflows using it stop working (see `connections.dependents`).
        
        `DELETE /api/connections/{connectionId}`
        """
        return self._request("DELETE", f"/api/connections/{_seg(connection_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def dependents(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> List[ConnectionsDependentsResponseItem]:
        """Lists the workflows that use a connection.
        
        `GET /api/connections/{connectionId}/dependents`
        """
        return self._request("GET", f"/api/connections/{_seg(connection_id)}/dependents", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> Connection:
        """Returns one connection, with secrets masked.
        
        `GET /api/connections/{connectionId}`
        """
        return self._request("GET", f"/api/connections/{_seg(connection_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_o_auth_url(self, connection_id: str, *, package_id: str, options: Optional[RequestOptions] = None) -> str:
        """Returns the address where a person authorizes an OAuth connection with the provider.
        
        `GET /api/connections/{connectionId}/oauth-url`
        """
        return _pick(self._request("GET", f"/api/connections/{_seg(connection_id)}/oauth-url", query={"packageId": package_id}, body=None, multipart=False, options=options), "url")  # type: ignore[no-any-return]

    def list(self, *, workspace_id: Optional[str] = None, package_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Connection]:
        """Lists a workspace's connections, with secrets masked.
        
        The caller's personal connections are included; other people's are not.
        
        `GET /api/connections`
        """
        return self._request("GET", f"/api/connections", query={"workspaceId": workspace_id, "packageId": package_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_requirements(self, *, options: Optional[RequestOptions] = None) -> List[ConnectionsListRequirementsResponseItem]:
        """Lists what each integration needs to connect: credential types and fields.
        
        `GET /api/connections/requirements`
        """
        return self._request("GET", f"/api/connections/requirements", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def refresh(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> ConnectionsRefreshResponse:
        """Refreshes an OAuth connection's access token when it is about to expire.
        
        `POST /api/connections/{connectionId}/refresh`
        """
        return self._request("POST", f"/api/connections/{_seg(connection_id)}/refresh", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def test(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> ConnectionsTestResponse:
        """Checks that a connection's credentials work.
        
        `POST /api/connections/{connectionId}/test`
        """
        return self._request("POST", f"/api/connections/{_seg(connection_id)}/test", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, connection_id: str, body: UpdateConnectionInput, *, options: Optional[RequestOptions] = None) -> Connection:
        """Renames a connection or changes its credentials.
        
        `PATCH /api/connections/{connectionId}`
        """
        return self._request("PATCH", f"/api/connections/{_seg(connection_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CountriesResource(_Resource):
    """Countries
    """

    def list(self, *, options: Optional[RequestOptions] = None) -> List[Country]:
        """Lists the countries the platform offers, with each one's regional defaults and tax regime.
        
        Answers without a token. Only enabled countries, in the administrator's order; cached for five minutes.
        
        `GET /api/countries` — No token needed.
        """
        return self._request("GET", f"/api/countries", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class CreatorsResource(_Resource):
    """Creator profiles — A person's creator profile — what they chose to show, their marketplace listings, the hubs and templates they share with the caller, and their community reputation. Not anonymous: every call needs a signed-in person or a token; never an address, a phone number or an organisation membership.
    """

    def faces(self, handle: str, *, options: Optional[RequestOptions] = None) -> CreatorFaces:
        """Lists where else a person shows up that the caller can see: their shop, shared hubs, templates and reports.
        
        A profile is seen by its owner; by anybody signed in when public; by people of the same organisation when shared with the organisation. Otherwise 404, as if there were none.
        
        `GET /api/public/creator/{handle}/faces`
        """
        return _pick(self._request("GET", f"/api/public/creator/{_seg(handle)}/faces", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, handle: str, *, options: Optional[RequestOptions] = None) -> CreatorProfile:
        """Returns a person's creator profile by handle.
        
        A profile is seen by its owner; by anybody signed in when public; by people of the same organisation when shared with the organisation. Otherwise 404, as if there were none.
        
        `GET /api/public/creator/{handle}`
        """
        return self._request("GET", f"/api/public/creator/{_seg(handle)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def regenerate_about(self, handle: str, *, options: Optional[RequestOptions] = None) -> CreatorsRegenerateAboutResponseData:
        """Writes the short introduction on the caller's own profile again with the platform's AI, from their listings, badges and bio.
        
        The profile's owner only, and only with an organisation (403 `no_organization` without one). Needs the AI introduction on their organisation's plan and its AI allowance (402 when used up); 4 an hour. 400 `creatorAboutNotEnoughSignal` with no listing, badge or bio to write from. The text is shown again (if it was hidden) and marked as written by AI.
        
        `POST /api/public/creator/{handle}/about`
        """
        return _pick(self._request("POST", f"/api/public/creator/{_seg(handle)}/about", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def reputation(self, handle: str, *, options: Optional[RequestOptions] = None) -> CreatorReputation:
        """Returns a person's reputation per community hub and their latest reputation events, in the hubs the caller also belongs to.
        
        A profile is seen by its owner; by anybody signed in when public; by people of the same organisation when shared with the organisation. Otherwise 404, as if there were none. The profile's owner sees every hub of theirs.
        
        `GET /api/public/creator/{handle}/reputation-events`
        """
        return _pick(self._request("GET", f"/api/public/creator/{_seg(handle)}/reputation-events", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_about_hidden(self, handle: str, body: CreatorsSetAboutHiddenBody, *, options: Optional[RequestOptions] = None) -> CreatorsSetAboutHiddenResponse:
        """Hides the AI-written introduction on the caller's own profile, or shows it again.
        
        The profile's owner only.
        
        `PATCH /api/public/creator/{handle}/about`
        """
        return self._request("PATCH", f"/api/public/creator/{_seg(handle)}/about", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmActionsResource(_Resource):

    def booking_link(self, space_id: str, record_id: str, body: CrmActionsBookingLinkBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Shares a booking link with the person: prefilled in the composer, as a link to copy, or as a mail draft in the caller's mailbox.
        
        Needs edit level. Never sends mail by itself. The record's timeline notes it.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/actions/booking-link` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/actions/booking-link", query=None, body=body, multipart=False, options=options), "result")  # type: ignore[no-any-return]

    def document(self, space_id: str, record_id: str, body: CrmActionsDocumentBody, *, options: Optional[RequestOptions] = None) -> CrmActionsDocumentResponseDocument:
        """Creates a document from a template with the record's values filled in, private to the caller.
        
        Needs edit level and `document:create`; counts against the plan's document limit.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/actions/document` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/actions/document", query=None, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def get(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """What a record's actions may offer now: the person they reach, the booking pages to share, the templates a document may start from, whether signing is possible.
        
        Needs edit level on the record (403 otherwise).
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/actions` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/actions", query=None, body=None, multipart=False, options=options), "actions")  # type: ignore[no-any-return]

    def request_signature(self, space_id: str, record_id: str, body: CrmActionsRequestSignatureBody, *, options: Optional[RequestOptions] = None) -> str:
        """Sends a document for signing — to the record's person, or the signers named.
        
        Needs edit level and e-signature on the plan. The document is rendered as a PDF and sent through the e-signature hub; the record's timeline notes it.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/actions/signature` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/actions/signature", query=None, body=body, multipart=False, options=options), "requestId")  # type: ignore[no-any-return]

    def signature_options(self, space_id: str, record_id: str, *, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> CrmActionsSignatureOptionsResponse:
        """The documents the caller may send for signing to the record's person.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/actions/signature` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/actions/signature", query={"q": q}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmActivitiesResource(_Resource):

    def delete(self, space_id: str, record_id: str, activity_id: str, *, options: Optional[RequestOptions] = None) -> CrmActivitiesDeleteResponse:
        """Removes an activity; entries the system recorded cannot be removed.
        
        `DELETE /api/crm/spaces/{spaceId}/records/{recordId}/activities/{activityId}` — Token permission: `write:crm`.
        """
        return self._request("DELETE", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/activities/{_seg(activity_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def log(self, space_id: str, record_id: str, body: CrmLogActivityInput, *, options: Optional[RequestOptions] = None) -> CrmActivitiesLogResponse:
        """Log an activity — a call, meeting, email, note or one of the space's own types — with the answers to its question flow.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/activities` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/activities", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def log_call(self, space_id: str, record_id: str, body: CrmLogCallInput, *, options: Optional[RequestOptions] = None) -> CrmActivitiesLogCallResponse:
        """Log a call — direction, outcome, duration, a note, the call flow's answers, and optionally a follow-up task.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/calls` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/calls", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def timeline(self, space_id: str, record_id: str, *, kind: Optional[Literal["change", "activity"]] = None, cursor: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[CrmTimelineEntry]:
        """One page of a record's timeline, newest first.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/timeline` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/timeline", query={"kind": kind, "cursor": cursor, "limit": limit}, body=None, multipart=False, options=options), "entries")  # type: ignore[no-any-return]

    def update(self, space_id: str, record_id: str, activity_id: str, body: CrmActivitiesUpdateBody, *, options: Optional[RequestOptions] = None) -> CrmActivitiesUpdateResponse:
        """Change an activity (its author, or a manager of the space).
        
        `PATCH /api/crm/spaces/{spaceId}/records/{recordId}/activities/{activityId}` — Token permission: `write:crm`.
        """
        return self._request("PATCH", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/activities/{_seg(activity_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmBriefResource(_Resource):

    def get(self, space_id: str, record_id: str, body: CrmBriefGetBody, *, options: Optional[RequestOptions] = None) -> CrmBriefing:
        """"Brief me": a short briefing before a call or meeting — who, last contact, open deals and tasks, what to mention, risks — written by the platform's AI.
        
        Nothing is stored. Written only from what the caller may see; the AI allowance applies (429).
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/brief` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/brief", query=None, body=body, multipart=False, options=options), "briefing")  # type: ignore[no-any-return]

    def save_note(self, space_id: str, record_id: str, body: CrmBriefSaveNoteBody, *, options: Optional[RequestOptions] = None) -> CrmTimelineEntry:
        """Saves a briefing as a note on the record, marked AI-assisted.
        
        Needs edit level on the space.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/brief/note` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/brief/note", query=None, body=body, multipart=False, options=options), "entry")  # type: ignore[no-any-return]


class CrmCaptureRulesResource(_Resource):

    def create(self, body: CrmCaptureRulesCreateBody, *, options: Optional[RequestOptions] = None) -> CrmCaptureRule:
        """Creates an automatic-contact rule: what arrives from a source (a form, a waitlist…) becomes people — and optionally companies, deals and tasks — in the CRM.
        
        Needs `crm:manage` in the workspace, edit level on every space it writes to, the source readable by the caller, and automatic contacts on the plan (counts against its rule limit). The rule runs as the caller.
        
        `POST /api/crm/capture-rules` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/capture-rules", query=None, body=body, multipart=False, options=options), "rule")  # type: ignore[no-any-return]

    def delete(self, rule_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Deletes an automatic-contact rule.
        
        `DELETE /api/crm/capture-rules/{ruleId}` — Token permission: `write:crm`.
        """
        return self._request("DELETE", f"/api/crm/capture-rules/{_seg(rule_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> CrmCaptureRulesListResponse:
        """The workspace's automatic-contact rules, each with its source, the spaces it writes to, its last run and its counts.
        
        `GET /api/crm/capture-rules` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/capture-rules", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def sources(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> CrmCaptureChoices:
        """What a rule may point at — sources, their items, the spaces.
        
        `GET /api/crm/capture-rules/sources` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/capture-rules/sources", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options), "choices")  # type: ignore[no-any-return]

    def update(self, rule_id: str, body: CrmCaptureRulesUpdateBody, *, options: Optional[RequestOptions] = None) -> CrmCaptureRule:
        """Change a rule — `{ enabled: false }` alone switches it off.
        
        `PATCH /api/crm/capture-rules/{ruleId}` — Token permission: `write:crm`.
        """
        return _pick(self._request("PATCH", f"/api/crm/capture-rules/{_seg(rule_id)}", query=None, body=body, multipart=False, options=options), "rule")  # type: ignore[no-any-return]


class CrmConsentsResource(_Resource):

    def for_space(self, space_id: str, *, options: Optional[RequestOptions] = None) -> CrmConsentsForSpaceResponse:
        """Consent status per record and channel, and the counts.
        
        `GET /api/crm/spaces/{spaceId}/consents` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/consents", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> CrmConsentsGetResponse:
        """A person's consent ledger.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/consents` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/consents", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def grant(self, space_id: str, record_id: str, body: Union[CrmConsentsGrantBody, CrmConsentsGrantBody2], *, options: Optional[RequestOptions] = None) -> str:
        """Records a consent the person gave (`action: grant`), or that they withdrew one (`action: revoke`).
        
        Needs edit level on the space. A consent recorded here is marked manual, with the caller as the actor.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/consents` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/consents", query=None, body=body, multipart=False, options=options), "consentId")  # type: ignore[no-any-return]

    def reconsent(self, space_id: str, record_id: str, body: CrmConsentsReconsentBody, *, options: Optional[RequestOptions] = None) -> CrmConsentsReconsentResponse:
        """Asks the person to confirm their consent by double opt-in: a mail with a one-time link in their language.
        
        Needs edit level. E-mail channels only; refused for a person whose latest decision is a withdrawal they made themselves. 30 an hour.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/consents/reconsent` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/consents/reconsent", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmDealRoomResource(_Resource):

    def add_step(self, space_id: str, deal_id: str, body: CrmDealRoomStepInput, *, options: Optional[RequestOptions] = None) -> CrmDealRoomStep:
        """Add a step to the mutual action plan.
        
        `POST /api/crm/spaces/{spaceId}/records/{dealId}/deal-room/steps` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/deal-room/steps", query=None, body=body, multipart=False, options=options), "step")  # type: ignore[no-any-return]

    def delete_step(self, space_id: str, deal_id: str, step_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Remove a step.
        
        `DELETE /api/crm/spaces/{spaceId}/records/{dealId}/deal-room/steps/{stepId}` — Token permission: `write:crm`.
        """
        return self._request("DELETE", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/deal-room/steps/{_seg(step_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, space_id: str, deal_id: str, *, options: Optional[RequestOptions] = None) -> CrmDealRoomState:
        """The room: plan, shared items, thread.
        
        `GET /api/crm/spaces/{spaceId}/records/{dealId}/deal-room` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/deal-room", query=None, body=None, multipart=False, options=options), "room")  # type: ignore[no-any-return]

    def message(self, space_id: str, deal_id: str, body: Union[CrmDealRoomMessageBody, CrmDealRoomMessageBody2], *, options: Optional[RequestOptions] = None) -> CrmDealRoomMessage:
        """Writes a message to the customer, or a comment on a step, in the deal room; plain text.
        
        `POST /api/crm/spaces/{spaceId}/records/{dealId}/deal-room/messages` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/deal-room/messages", query=None, body=body, multipart=False, options=options), "message")  # type: ignore[no-any-return]

    def options_(self, space_id: str, deal_id: str, *, kind: CrmDealRoomItemKind, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[CrmDealRoomOption]:
        """What could be shared, of one kind.
        
        `GET /api/crm/spaces/{spaceId}/records/{dealId}/deal-room/options` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/deal-room/options", query={"kind": kind, "q": q}, body=None, multipart=False, options=options), "options")  # type: ignore[no-any-return]

    def share(self, space_id: str, deal_id: str, body: CrmDealRoomShareBody, *, options: Optional[RequestOptions] = None) -> CrmDealRoomItem:
        """Share a document, file, signature request, booking page or match into the room.
        
        `POST /api/crm/spaces/{spaceId}/records/{dealId}/deal-room/items` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/deal-room/items", query=None, body=body, multipart=False, options=options), "item")  # type: ignore[no-any-return]

    def unshare(self, space_id: str, deal_id: str, item_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Take a shared item back out.
        
        `DELETE /api/crm/spaces/{spaceId}/records/{dealId}/deal-room/items/{itemId}` — Token permission: `write:crm`.
        """
        return self._request("DELETE", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/deal-room/items/{_seg(item_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_step(self, space_id: str, deal_id: str, step_id: str, body: CrmDealRoomStepPatch, *, options: Optional[RequestOptions] = None) -> CrmDealRoomStep:
        """Change, tick off or reorder a step.
        
        `PATCH /api/crm/spaces/{spaceId}/records/{dealId}/deal-room/steps/{stepId}` — Token permission: `write:crm`.
        """
        return _pick(self._request("PATCH", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/deal-room/steps/{_seg(step_id)}", query=None, body=body, multipart=False, options=options), "step")  # type: ignore[no-any-return]


class CrmDuplicatesResource(_Resource):

    def check(self, space_id: str, body: Union[CrmDuplicatesCheckBody, CrmDuplicatesCheckBody2], *, options: Optional[RequestOptions] = None) -> List[CrmDuplicateCandidate]:
        """Records the given cells may be the same as — at most five.
        
        `POST /api/crm/spaces/{spaceId}/duplicates/check` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/duplicates/check", query=None, body=body, multipart=False, options=options), "candidates")  # type: ignore[no-any-return]

    def list(self, space_id: str, *, options: Optional[RequestOptions] = None) -> CrmDuplicatesListResponse:
        """Groups of records that look like the same person or company.
        
        `GET /api/crm/spaces/{spaceId}/duplicates` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/duplicates", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def merge(self, space_id: str, body: CrmMergeRequest, *, options: Optional[RequestOptions] = None) -> CrmDuplicatesMergeResponse:
        """Merges records into one; the others are deleted.
        
        Needs manage level on the space.
        
        `POST /api/crm/spaces/{spaceId}/merge` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/merge", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def preview_merge(self, space_id: str, body: CrmMergeRequest, *, options: Optional[RequestOptions] = None) -> CrmMergePreview:
        """What merging would do; nothing is written.
        
        `POST /api/crm/spaces/{spaceId}/merge/preview` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/merge/preview", query=None, body=body, multipart=False, options=options), "preview")  # type: ignore[no-any-return]


class CrmEnrichmentResource(_Resource):

    def bulk(self, space_id: str, body: CrmEnrichmentBulkBody, *, options: Optional[RequestOptions] = None) -> CrmEnrichmentBulkResponse:
        """Enriches the selected records: a run each, for those with a website or company address.
        
        Needs edit level and company enrichment on the plan. The month's allowance is checked for all before any is queued (403 limit).
        
        `POST /api/crm/spaces/{spaceId}/enrichment/bulk` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/enrichment/bulk", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def configure(self, space_id: str, body: CrmEnrichmentConfigureBody, *, options: Optional[RequestOptions] = None) -> CrmEnrichmentConfigureResponse:
        """Replaces a space's company-enrichment settings.
        
        Needs manage level and `crm:manage`. Each mapped column must exist, fit its field and be mapped once (400 `crmEnrichmentInvalid` with `problems`). Automatic enrichment and refreshing need it on the plan.
        
        `PUT /api/crm/spaces/{spaceId}/enrichment` — Token permission: `write:crm`.
        """
        return self._request("PUT", f"/api/crm/spaces/{_seg(space_id)}/enrichment", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def decide(self, space_id: str, record_id: str, body: CrmEnrichmentDecideBody, *, options: Optional[RequestOptions] = None) -> CrmEnrichmentDecideResponse:
        """Accepts or rejects enrichment proposals; accepted values are written to the record.
        
        Needs edit level. A cell changed since the proposal answers 409 `recordFieldChanged` unless it is in `force`. `acceptEmpty` accepts every open proposal whose cell is empty now.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/enrichment/decide` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/enrichment/decide", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> CrmEnrichmentGetResponse:
        """A record's company enrichment: its last run, its open proposals with what each cell holds now, and the month's allowance.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/enrichment` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/enrichment", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def run(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Queues an enrichment run for a record: its company's public details become proposals.
        
        Needs edit level. One run per record at a time (409 `crmEnrichmentRunning`); the month's allowance applies (403 limit).
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/enrichment` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/enrichment", query=None, body=None, multipart=False, options=options), "run")  # type: ignore[no-any-return]

    def settings(self, space_id: str, *, options: Optional[RequestOptions] = None) -> CrmEnrichmentSettingsResponse:
        """A space's company-enrichment settings, the mapping its columns suggest, and the organisation's allowance this month.
        
        Needs company enrichment on the plan.
        
        `GET /api/crm/spaces/{spaceId}/enrichment` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/enrichment", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmGroupsResource(_Resource):

    def delete(self, group_id: str, *, options: Optional[RequestOptions] = None) -> CrmGroupsDeleteResponse:
        """Deletes a group with every space in it, their records, activities and reminders.
        
        Needs `crm:manage`, `database:delete` and delete level on every space of the group: all or nothing, checked before the first goes.
        
        `DELETE /api/crm/groups/{groupId}` — Token permission: `write:crm`.
        """
        return self._request("DELETE", f"/api/crm/groups/{_seg(group_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def rename(self, group_id: str, body: CrmGroupsRenameBody, *, options: Optional[RequestOptions] = None) -> CrmGroupsRenameResponse:
        """Renames a group of spaces, on every space in it.
        
        Needs `crm:manage` and manage level on every space of the group — renamed everywhere or nowhere (403 `crmGroupNotEditable`).
        
        `PATCH /api/crm/groups/{groupId}` — Token permission: `write:crm`.
        """
        return self._request("PATCH", f"/api/crm/groups/{_seg(group_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmJourneyResource(_Resource):

    def get(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """A record's visitor journeys: the consented visitors of the organisation's sites linked to it, their touches and events.
        
        Needs `journeys:read` and visitor journeys on the plan.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/journey` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/journey", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def summarise(self, space_id: str, record_id: str, body: CrmJourneySummariseBody, *, options: Optional[RequestOptions] = None) -> CrmJourneySummariseResponse:
        """Summarises with the platform's AI how this person found and used the organisation's sites; nothing is stored.
        
        Needs `journeys:read`; the AI allowance applies (429). The AI reads touches, pages and timestamps only — never an e-mail or a name.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/journey/summary` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/journey/summary", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmMatchesResource(_Resource):

    def for_record(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> CrmMatchesForRecordResponse:
        """The records matching this one, ranked, with reasons.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/matches` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/matches", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def for_space(self, space_id: str, *, options: Optional[RequestOptions] = None) -> CrmMatchesForSpaceResponse:
        """The space's best open matches.
        
        `GET /api/crm/spaces/{spaceId}/matches` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/matches", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def propose(self, space_id: str, record_id: str, body: CrmMatchesProposeBody, *, options: Optional[RequestOptions] = None) -> CrmMatchesProposeResponse:
        """Logs a match as proposed: a "Match proposed" activity on each record the caller may change, and a link in the proposed column.
        
        Needs edit level on at least one of the two spaces.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/matches/propose` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/matches/propose", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmMatchingResource(_Resource):

    def get(self, space_id: str, *, brief: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> CrmMatchingGetResponse:
        """A space's matching definitions (properties and search profiles), those of other spaces looking at it, and what no longer fits.
        
        `GET /api/crm/spaces/{spaceId}/matching` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/matching", query={"brief": brief}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def put(self, space_id: str, body: CrmMatchingPutBody, *, options: Optional[RequestOptions] = None) -> CrmMatchingPutResponse:
        """Replaces a space's matching definitions.
        
        Needs manage level and `crm:manage`. Each definition names another space of the workspace the caller can open and fits both spaces' columns (400 `crmMatchingInvalid` with `problems`).
        
        `PUT /api/crm/spaces/{spaceId}/matching` — Token permission: `write:crm`.
        """
        return self._request("PUT", f"/api/crm/spaces/{_seg(space_id)}/matching", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmMeetingsResource(_Resource):

    def apply(self, event_id: str, body: CrmMeetingsApplyBody, *, options: Optional[RequestOptions] = None) -> CrmMeetingsApplyResponse:
        """Writes a meeting's outcome to the CRM: a Meeting activity per person, a task per next step — each once per event.
        
        An item applied before is skipped and reported `alreadyApplied`.
        
        `POST /api/crm/meetings/{eventId}` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/meetings/{_seg(event_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def proposal(self, event_id: str, *, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """What a calendar meeting's outcome would write to the CRM: the attendees' records, their open deals, the next steps as tasks.
        
        Writes nothing. Only records the caller may see.
        
        `GET /api/crm/meetings/{eventId}` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/meetings/{_seg(event_id)}", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options), "proposal")  # type: ignore[no-any-return]


class CrmOfflineConversionsResource(_Resource):

    def get(self, space_id: str, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """A deals space's offline-conversion settings — which stage reports which conversion to which ad network — and its last deliveries.
        
        `GET /api/crm/spaces/{spaceId}/offline-conversions` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/offline-conversions", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def put(self, space_id: str, body: CrmOfflineConversionsPutBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Replaces a deals space's offline-conversion settings.
        
        Needs manage level, `crm:manage` and offline conversions on the plan. 400 `crmOfflineInvalid` with `problems`.
        
        `PUT /api/crm/spaces/{spaceId}/offline-conversions` — Token permission: `write:crm`.
        """
        return _pick(self._request("PUT", f"/api/crm/spaces/{_seg(space_id)}/offline-conversions", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class CrmPipelineResource(_Resource):

    def add(self, space_id: str, body: CrmPipelineAddBody, *, options: Optional[RequestOptions] = None) -> CrmPipelineAddResponse:
        """Adds another pipeline beside a deals space: a new deals space in the same group, its stages copied from this one or the template's.
        
        Needs `crm:manage` and `database:create`; counts against the plan's CRM space limit.
        
        `POST /api/crm/spaces/{spaceId}/pipeline` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/pipeline", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, space_id: str, body: CrmPipelineUpdateBody, *, options: Optional[RequestOptions] = None) -> CrmPipelineUpdateResponse:
        """Changes a deals space's pipeline as one list: add, rename, recolour, reorder and remove stages, mark them won or lost.
        
        Needs edit level on the table. Cells and views holding a renamed stage follow; a removed stage's deals move by `moves` (or lose their stage). 400 `crmPipelineInvalid` with `problems`.
        
        `PATCH /api/crm/spaces/{spaceId}/pipeline` — Token permission: `write:crm`.
        """
        return self._request("PATCH", f"/api/crm/spaces/{_seg(space_id)}/pipeline", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmPlaybooksResource(_Resource):

    def get(self, space_id: str, *, options: Optional[RequestOptions] = None) -> CrmPlaybooksGetResponse:
        """The space's playbooks and what the editor offers.
        
        `GET /api/crm/spaces/{spaceId}/playbooks` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/playbooks", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def put(self, space_id: str, body: CrmPlaybooksPutBody, *, options: Optional[RequestOptions] = None) -> CrmPlaybooksPutResponse:
        """Replaces the space's playbooks.
        
        400 `crmPlaybooksInvalid` with `problems`.
        
        `PUT /api/crm/spaces/{spaceId}/playbooks` — Token permission: `write:crm`.
        """
        return self._request("PUT", f"/api/crm/spaces/{_seg(space_id)}/playbooks", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def retry(self, space_id: str, deal_id: str, run_id: str, *, options: Optional[RequestOptions] = None) -> List[CrmPlaybookRun]:
        """Run a run's skipped or failed steps again, as the caller.
        
        `POST /api/crm/spaces/{spaceId}/records/{dealId}/playbooks/{runId}/retry` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/playbooks/{_seg(run_id)}/retry", query=None, body=None, multipart=False, options=options), "runs")  # type: ignore[no-any-return]

    def runs(self, space_id: str, deal_id: str, *, options: Optional[RequestOptions] = None) -> CrmPlaybooksRunsResponse:
        """A deal's playbook runs.
        
        `GET /api/crm/spaces/{spaceId}/records/{dealId}/playbooks` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(deal_id)}/playbooks", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmPortalResource(_Resource):

    def invitations(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> CrmPortalInvitationsResponse:
        """The person's invitations, newest first.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/portal-invitations` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/portal-invitations", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def invite(self, space_id: str, record_id: str, body: CrmPortalInviteBody, *, options: Optional[RequestOptions] = None) -> CrmPortalInviteResult:
        """Invite the person: a single-use sign-in link by mail.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/portal-invite` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/portal-invite", query=None, body=body, multipart=False, options=options), "result")  # type: ignore[no-any-return]

    def invite_options(self, space_id: str, record_id: str, *, project_id: Optional[str] = None, language: Optional[str] = None, options: Optional[RequestOptions] = None) -> CrmPortalInviteOptions:
        """What an invitation would offer — address, websites, the mail as sent.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/portal-invite` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/portal-invite", query={"projectId": project_id, "language": language}, body=None, multipart=False, options=options), "invite")  # type: ignore[no-any-return]

    def record(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Whether a record is shown in the customer portal and with which fields, and how many website accounts see it.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/portal` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/portal", query=None, body=None, multipart=False, options=options), "portal")  # type: ignore[no-any-return]

    def resend(self, invitation_id: str, *, options: Optional[RequestOptions] = None) -> CrmPortalInviteResult:
        """Send a new invitation in place of this one.
        
        `POST /api/crm/portal/invitations/{invitationId}/resend` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/portal/invitations/{_seg(invitation_id)}/resend", query=None, body=None, multipart=False, options=options), "result")  # type: ignore[no-any-return]

    def set_site_page(self, project_id: str, body: CrmPortalSetSitePageBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Chooses a website's customer portal page — a live page holding a customer portal block — or clears the choice.
        
        Needs `crm:manage` and `project:update`. 400 `crmPortalPageNotPortal`.
        
        `PUT /api/crm/portal/sites/{projectId}` — Token permission: `write:crm`.
        """
        return _pick(self._request("PUT", f"/api/crm/portal/sites/{_seg(project_id)}", query=None, body=body, multipart=False, options=options), "site")  # type: ignore[no-any-return]

    def site_invitations(self, project_id: str, *, options: Optional[RequestOptions] = None) -> CrmPortalSiteInvitationsResponse:
        """A website's invitations.
        
        `GET /api/crm/portal/sites/{projectId}/invitations` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/portal/sites/{_seg(project_id)}/invitations", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def sites(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> CrmPortalSitesResponse:
        """The workspace's websites with their customer portal pages, the chosen one, and what stands in the way.
        
        `GET /api/crm/portal/sites` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/portal/sites", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def spaces(self, *, project_id: str, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The CRM spaces a customer portal block on a website may show, each with the fields it shares.
        
        `GET /api/crm/portal/spaces` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/portal/spaces", query={"projectId": project_id}, body=None, multipart=False, options=options), "spaces")  # type: ignore[no-any-return]

    def withdraw(self, invitation_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Withdraw an open invitation.
        
        `POST /api/crm/portal/invitations/{invitationId}/withdraw` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/portal/invitations/{_seg(invitation_id)}/withdraw", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmRecordsResource(_Resource):

    def create(self, space_id: str, body: Union[CrmRecordsCreateBody, CrmRecordsCreateBody2], *, options: Optional[RequestOptions] = None) -> CrmRecordsCreateResponse:
        """Creates a record (cells by column id), or several at once with `records`.
        
        Counts against the plan's CRM record limit. Relations and person cells are checked; a database with approvers files the new record for approval.
        
        `POST /api/databases/{spaceId}/records`
        """
        return self._request("POST", f"/api/databases/{_seg(space_id)}/records", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> CrmRecordsDeleteResponse:
        """Moves a record to the trash.
        
        409 `recordPendingApproval` while a change waits for approval.
        
        `DELETE /api/databases/{spaceId}/records/{recordId}`
        """
        return self._request("DELETE", f"/api/databases/{_seg(space_id)}/records/{_seg(record_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> CrmRecord:
        """One record.
        
        `GET /api/databases/{spaceId}/records/{recordId}`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(space_id)}/records/{_seg(record_id)}", query=None, body=None, multipart=False, options=options), "record")  # type: ignore[no-any-return]

    def list(self, space_id: str, *, limit: Optional[int] = None, offset: Optional[int] = None, sort_by: Optional[str] = None, sort_direction: Optional[Literal["asc", "desc"]] = None, filters: Optional[str] = None, options: Optional[RequestOptions] = None) -> CrmRecordsListResponse:
        """One page of a space's records, with filters, sort and offset paging.
        
        Only the records the caller may see (row security).
        
        `GET /api/databases/{spaceId}/records`
        """
        return self._request("GET", f"/api/databases/{_seg(space_id)}/records", query={"limit": limit, "offset": offset, "sortBy": sort_by, "sortDirection": sort_direction, "filters": filters}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, space_id: str, record_id: str, body: CrmRecordsUpdateBody, *, options: Optional[RequestOptions] = None) -> CrmRecord:
        """Changes the cells of a record.
        
        With `merge: true` only the cells in `data` change; without it `data` is the whole row and a cell left out is removed. With `base` (each changed cell as the edit began), a cell somebody changed since is refused (409 `recordFieldChanged`) instead of overwritten. 409 `recordPendingApproval` while an earlier change waits for approval.
        
        `PATCH /api/databases/{spaceId}/records/{recordId}`
        """
        return _pick(self._request("PATCH", f"/api/databases/{_seg(space_id)}/records/{_seg(record_id)}", query=None, body=body, multipart=False, options=options), "record")  # type: ignore[no-any-return]


class CrmSalesResource(_Resource):

    def deal_signals(self, space_id: str, *, options: Optional[RequestOptions] = None) -> CrmSalesDealSignalsResponse:
        """Stalled deals and their next steps.
        
        `GET /api/crm/spaces/{spaceId}/deal-signals` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/deal-signals", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def flow_funnel(self, *, space_id: Optional[str] = None, workspace_id: Optional[str] = None, period: Optional[Literal["30d", "90d", "month", "lastMonth", "quarter", "year"]] = None, activity_type: Optional[str] = None, options: Optional[RequestOptions] = None) -> CrmFlowFunnelReport:
        """The question flow funnel of an activity type: how the answers of logged calls and meetings went.
        
        For one space or a workspace's spaces; one of `spaceId` and `workspaceId` is required.
        
        `GET /api/crm/sales/flows` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/sales/flows", query={"spaceId": space_id, "workspaceId": workspace_id, "period": period, "activityType": activity_type}, body=None, multipart=False, options=options), "report")  # type: ignore[no-any-return]

    def report(self, *, space_id: Optional[str] = None, workspace_id: Optional[str] = None, period: Optional[Literal["30d", "90d", "month", "lastMonth", "quarter", "year"]] = None, options: Optional[RequestOptions] = None) -> CrmSalesReport:
        """The sales report: pipeline, win rate, sales cycle, forecast, activities, lost reasons, stalled deals.
        
        For one deals space (`spaceId`) or every deals space of a workspace the caller may open (`workspaceId`); one of the two is required. Only the deals the caller may see; periods on the caller's clock. 60 a minute.
        
        `GET /api/crm/sales` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/sales", query={"spaceId": space_id, "workspaceId": workspace_id, "period": period}, body=None, multipart=False, options=options), "report")  # type: ignore[no-any-return]


class CrmSpacesResource(_Resource):

    def convert(self, body: CrmSpacesConvertBody, *, options: Optional[RequestOptions] = None) -> CrmSpaceSummary:
        """Turns an existing table into a CRM space; its rows, columns, views, shares and relations stay as they are.
        
        Needs manage level on the table and `crm:manage`. The table and its rows move to the CRM's own plan limits (403 limit). 400 `crmConfigInvalid` with `problems`; 409 `crmAlreadySpace`.
        
        `POST /api/crm/spaces/convert` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/convert", query=None, body=body, multipart=False, options=options), "space")  # type: ignore[no-any-return]

    def convertible(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> CrmSpacesConvertibleResponse:
        """The plain tables of a workspace the caller could turn into a CRM space.
        
        Needs `crm:manage` in the workspace. Names, icons, row counts and columns only.
        
        `GET /api/crm/spaces/convert` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/convert", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def create(self, body: CrmSpacesCreateBody, *, options: Optional[RequestOptions] = None) -> CrmSpaceSummary:
        """Creates a custom space with one Name column and the default activity types.
        
        Needs `crm:manage` and `database:create` in the workspace; counts against the plan's CRM space limit.
        
        `POST /api/crm/spaces` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces", query=None, body=body, multipart=False, options=options), "space")  # type: ignore[no-any-return]

    def design(self, body: CrmSpacesDesignBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Designs CRM spaces from a description with the platform's AI — answered as a proposal, never created here.
        
        Needs `crm:manage`, `database:create` and CRM AI on the plan; the AI allowance applies (429). Create the (edited) proposal with `crm.spaces.setup` and `design`.
        
        `POST /api/crm/design` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/design", query=None, body=body, multipart=False, options=options), "proposal")  # type: ignore[no-any-return]

    def get(self, space_id: str, *, options: Optional[RequestOptions] = None) -> CrmSpaceSummary:
        """One space, its config and what the caller may do with it.
        
        The table itself — columns, views, records — is the Databases API.
        
        `GET /api/crm/spaces/{spaceId}` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}", query=None, body=None, multipart=False, options=options), "space")  # type: ignore[no-any-return]

    def list(self, *, workspace_id: str, space_type: Optional[Literal["people", "companies", "deals", "tasks", "custom"]] = None, options: Optional[RequestOptions] = None) -> List[CrmSpaceSummary]:
        """The workspace's CRM spaces the caller can open, each with its config, record count and what no longer fits.
        
        Needs `crm:read` in the workspace.
        
        `GET /api/crm/spaces` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces", query={"workspaceId": workspace_id, "spaceType": space_type}, body=None, multipart=False, options=options), "spaces")  # type: ignore[no-any-return]

    def set_group(self, space_id: str, body: Union[CrmSpacesSetGroupBody, CrmSpacesSetGroupBody2], *, options: Optional[RequestOptions] = None) -> CrmSpacesSetGroupResponse:
        """Moves a space into a group, out of any group, or into a new group of its own.
        
        Needs manage level on the table and `crm:manage`.
        
        `PUT /api/crm/spaces/{spaceId}/group` — Token permission: `write:crm`.
        """
        return self._request("PUT", f"/api/crm/spaces/{_seg(space_id)}/group", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def setup(self, body: CrmSetupInput, *, options: Optional[RequestOptions] = None) -> CrmSpacesSetupResponse:
        """Creates spaces from a template of the gallery ("sales", "realEstate", …), or the classic People / Companies / Deals / Tasks set.
        
        A template's spaces form one new group with their relations both ways; a template that wants Tasks reuses the workspace's Tasks space by default. The classic set refuses a type that exists already (409 `crmSpaceTypeExists`) unless `force`.
        
        `POST /api/crm/setup` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/setup", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def summary(self, space_id: str, *, options: Optional[RequestOptions] = None) -> CrmSpacesSummaryResponse:
        """What a space's overview card shows: the pipeline per stage with count and amount, open / won / lost, open and done tasks, the records changed last.
        
        Counted only from the rows the caller may see, up to a read cap (`truncated`).
        
        `GET /api/crm/spaces/{spaceId}/summary` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/summary", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_config(self, space_id: str, body: CrmSpacesUpdateConfigBody, *, options: Optional[RequestOptions] = None) -> CrmSpaceSummary:
        """Changes a space's CRM config: roles, pipeline settings, activity types, connected hubs, portal, website.
        
        Needs manage level on the table and `crm:manage`. A key left out stays; null clears a role. Checked against the columns as they are now: 400 `crmConfigInvalid` with `problems`. Switching on the portal, deal room or website needs it on the plan. Built-in activity types can be renamed or hidden, never removed.
        
        `PATCH /api/crm/spaces/{spaceId}` — Token permission: `write:crm`.
        """
        return _pick(self._request("PATCH", f"/api/crm/spaces/{_seg(space_id)}", query=None, body=body, multipart=False, options=options), "space")  # type: ignore[no-any-return]


class CrmTasksResource(_Resource):

    def set_done(self, space_id: str, record_id: str, body: CrmTasksSetDoneBody, *, options: Optional[RequestOptions] = None) -> CrmTasksSetDoneResponse:
        """Ticks a CRM task done (the space's first done value), or opens it again.
        
        Needs edit level on the space.
        
        `POST /api/crm/spaces/{spaceId}/records/{recordId}/done` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/done", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class CrmWebsiteResource(_Resource):

    def create_pages(self, space_id: str, body: CrmWebsiteCreatePagesBody, *, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Creates listing pages for a space on a website: a list page and a detail page per language, as drafts.
        
        Needs manage level, `crm:manage` and `page:create`. Nothing goes live: each page is published from the builder. 409 `crmWebsiteOff`, `crmWebsitePagesExist`, `pathTaken`.
        
        `POST /api/crm/spaces/{spaceId}/website/pages` — Token permission: `write:crm`.
        """
        return _pick(self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/website/pages", query=None, body=body, multipart=False, options=options), "pages")  # type: ignore[no-any-return]

    def get(self, space_id: str, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """A space on websites: whether it is on, how many records are public, the public columns and the listing pages.
        
        `GET /api/crm/spaces/{spaceId}/website` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/website", query=None, body=None, multipart=False, options=options), "website")  # type: ignore[no-any-return]

    def preview(self, space_id: str, body: CrmWebsitePreviewBody, *, options: Optional[RequestOptions] = None) -> CrmWebsitePreviewResponse:
        """What visitors would see under a website configuration not saved yet: how many records would be public, and three of them.
        
        Needs manage level and `crm:manage`. Writes nothing.
        
        `POST /api/crm/spaces/{spaceId}/website/preview` — Token permission: `write:crm`.
        """
        return self._request("POST", f"/api/crm/spaces/{_seg(space_id)}/website/preview", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def record(self, space_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Whether a record is public on the website now, with its live addresses and public columns.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/website` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/website", query=None, body=None, multipart=False, options=options), "website")  # type: ignore[no-any-return]


class CrmResource(_Resource):
    """CRM
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.actions = CrmActionsResource(request)
        self.activities = CrmActivitiesResource(request)
        self.brief = CrmBriefResource(request)
        self.capture_rules = CrmCaptureRulesResource(request)
        self.consents = CrmConsentsResource(request)
        self.deal_room = CrmDealRoomResource(request)
        self.duplicates = CrmDuplicatesResource(request)
        self.enrichment = CrmEnrichmentResource(request)
        self.groups = CrmGroupsResource(request)
        self.journey = CrmJourneyResource(request)
        self.matches = CrmMatchesResource(request)
        self.matching = CrmMatchingResource(request)
        self.meetings = CrmMeetingsResource(request)
        self.offline_conversions = CrmOfflineConversionsResource(request)
        self.pipeline = CrmPipelineResource(request)
        self.playbooks = CrmPlaybooksResource(request)
        self.portal = CrmPortalResource(request)
        self.records = CrmRecordsResource(request)
        self.sales = CrmSalesResource(request)
        self.spaces = CrmSpacesResource(request)
        self.tasks = CrmTasksResource(request)
        self.website = CrmWebsiteResource(request)

    def connected(self, space_id: str, record_id: str, *, sources: Optional[str] = None, cursor: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> CrmConnectedResponse:
        """What the other hubs know about this person — mail, form submissions, bookings, meetings, signatures — newest first.
        
        Read live for the caller: per hub its own rules apply, and nothing they may not see there is shown or counted. `failedSources` names a hub that could not be read.
        
        `GET /api/crm/spaces/{spaceId}/records/{recordId}/connected` — Token permission: `read:crm`.
        """
        return self._request("GET", f"/api/crm/spaces/{_seg(space_id)}/records/{_seg(record_id)}/connected", query={"sources": sources, "cursor": cursor, "limit": limit}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def mailboxes(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The caller's mailboxes of the workspace's organisation, each with whether it shows in the CRM.
        
        Only a mailbox's owner switches it, in the Mail API.
        
        `GET /api/crm/mailboxes` — Token permission: `read:crm`.
        """
        return _pick(self._request("GET", f"/api/crm/mailboxes", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options), "mailboxes")  # type: ignore[no-any-return]


class CurrenciesResource(_Resource):
    """Currencies
    """

    def list(self, *, options: Optional[RequestOptions] = None) -> List[Currency]:
        """Lists the currencies the platform offers, with how each one is written.
        
        Answers without a token. Only enabled currencies, in the administrator's order; cached for five minutes.
        
        `GET /api/currencies` — No token needed.
        """
        return self._request("GET", f"/api/currencies", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def rates(self, *, options: Optional[RequestOptions] = None) -> CurrencyRates:
        """Returns the latest stored exchange rates against one base currency.
        
        The base is the currency most rates are stored against. Before the first fetch the answer is `{ base: null, rates: {}, fetchedAt: null }`.
        
        `GET /api/currency-rates`
        """
        return self._request("GET", f"/api/currency-rates", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class DashboardsResource(_Resource):
    """Dashboards — An organisation's custom dashboards and their widgets. A dashboard is private to its creator, or visible to a workspace or the whole organisation; only its creator changes or deletes it.
    """

    def add_widget(self, dashboard_id: str, body: DashboardsAddWidgetBody, *, options: Optional[RequestOptions] = None) -> DashboardWidget:
        """Adds a widget to a dashboard.
        
        `POST /api/dashboards/{dashboardId}/widgets`
        """
        return _pick(self._request("POST", f"/api/dashboards/{_seg(dashboard_id)}/widgets", query=None, body=body, multipart=False, options=options), "widget")  # type: ignore[no-any-return]

    def create(self, body: DashboardsCreateBody, *, options: Optional[RequestOptions] = None) -> Dashboard:
        """Creates a dashboard.
        
        Needs `dashboard:create` and membership of the organisation (and access to the workspace, if given).
        
        `POST /api/dashboards`
        """
        return _pick(self._request("POST", f"/api/dashboards", query=None, body=body, multipart=False, options=options), "dashboard")  # type: ignore[no-any-return]

    def delete(self, id: str, *, options: Optional[RequestOptions] = None) -> DashboardsDeleteResponse:
        """Deletes a dashboard with its widgets.
        
        Needs `dashboard:delete`; only the dashboard's creator may.
        
        `DELETE /api/dashboards/{id}`
        """
        return self._request("DELETE", f"/api/dashboards/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_widget(self, dashboard_id: str, widget_id: str, *, options: Optional[RequestOptions] = None) -> DashboardsDeleteWidgetResponse:
        """Removes a widget from a dashboard.
        
        `DELETE /api/dashboards/{dashboardId}/widgets/{widgetId}`
        """
        return self._request("DELETE", f"/api/dashboards/{_seg(dashboard_id)}/widgets/{_seg(widget_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, id: str, *, options: Optional[RequestOptions] = None) -> DashboardsGetResponseDashboard:
        """Returns one dashboard with its widgets.
        
        Needs `dashboard:read`.
        
        `GET /api/dashboards/{id}`
        """
        return _pick(self._request("GET", f"/api/dashboards/{_seg(id)}", query=None, body=None, multipart=False, options=options), "dashboard")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, workspace_id: Optional[str] = None, scope: Optional[Literal["org", "platform"]] = None, options: Optional[RequestOptions] = None) -> List[Dashboard]:
        """Lists the dashboards of an organisation the caller can see.
        
        Needs `dashboard:read`. Without `organizationId` the list is empty. Workspace dashboards are listed only with their `workspaceId`.
        
        `GET /api/dashboards`
        """
        return _pick(self._request("GET", f"/api/dashboards", query={"organizationId": organization_id, "workspaceId": workspace_id, "scope": scope}, body=None, multipart=False, options=options), "dashboards")  # type: ignore[no-any-return]

    def list_widgets(self, dashboard_id: str, *, options: Optional[RequestOptions] = None) -> List[DashboardWidget]:
        """Lists a dashboard's widgets, top to bottom.
        
        `GET /api/dashboards/{dashboardId}/widgets`
        """
        return _pick(self._request("GET", f"/api/dashboards/{_seg(dashboard_id)}/widgets", query=None, body=None, multipart=False, options=options), "widgets")  # type: ignore[no-any-return]

    def update(self, id: str, body: DashboardsUpdateBody, *, options: Optional[RequestOptions] = None) -> Dashboard:
        """Changes a dashboard's name, description, visibility, order or default flag.
        
        Needs `dashboard:update`; only the dashboard's creator may.
        
        `PATCH /api/dashboards/{id}`
        """
        return _pick(self._request("PATCH", f"/api/dashboards/{_seg(id)}", query=None, body=body, multipart=False, options=options), "dashboard")  # type: ignore[no-any-return]

    def update_widget(self, dashboard_id: str, widget_id: str, body: DashboardsUpdateWidgetBody, *, options: Optional[RequestOptions] = None) -> DashboardWidget:
        """Changes a widget's title, type, configuration or place on the grid.
        
        `PATCH /api/dashboards/{dashboardId}/widgets/{widgetId}`
        """
        return _pick(self._request("PATCH", f"/api/dashboards/{_seg(dashboard_id)}/widgets/{_seg(widget_id)}", query=None, body=body, multipart=False, options=options), "widget")  # type: ignore[no-any-return]


class DataExportsResource(_Resource):

    def download(self, *, id: str, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the file of a finished background export.
        
        Needs `data:export`. Answers the file itself, not JSON. Only the person who started it; 404 until it is completed, 410 once it expired.
        
        `GET /api/data/export/download`
        """
        return self._request("GET", f"/api/data/export/download", query={"id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Union[DataExportsListResponse, DataExportJob]:
        """Lists the caller's last ten background exports, or returns one of them.
        
        Needs `data:export`. With `id` the answer is that export alone (an object, not a list); another person's export answers 404.
        
        `GET /api/data/export/jobs`
        """
        return self._request("GET", f"/api/data/export/jobs", query={"id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def start(self, body: DataExportsStartBody, *, options: Optional[RequestOptions] = None) -> DataExportsStartResponse:
        """Starts a background export of the caller's data.
        
        Needs `data:export`. One at a time per person: while one runs the answer is 409 with that one's `jobId`. Poll `data.exports.list` with the id, then download it with `data.exports.download`.
        
        `POST /api/data/export/jobs`
        """
        return self._request("POST", f"/api/data/export/jobs", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class DataResource(_Resource):
    """Data export — Everything of the caller's organizations they may see, as one JSON, Excel or CSV file.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.exports = DataExportsResource(request)

    def export(self, *, categories: Optional[str] = None, format: Optional[Literal["json", "xlsx", "csv"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Exports the caller's data at once, as a file.
        
        Needs `data:export`. Answers the file itself (JSON, .xlsx or CSV), not JSON in an envelope. For a large export, start a background one with `data.exports.start`.
        
        `GET /api/data/export`
        """
        return self._request("GET", f"/api/data/export", query={"categories": categories, "format": format}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class DatabasesColumnsResource(_Resource):

    def delete(self, database_id: str, column_id: str, *, options: Optional[RequestOptions] = None) -> DatabasesColumnsDeleteResponse:
        """Removes a column and its values from a table.
        
        `DELETE /api/databases/{databaseId}/columns/{columnId}`
        """
        return self._request("DELETE", f"/api/databases/{_seg(database_id)}/columns/{_seg(column_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def disable_calendar_feed(self, database_id: str, column_id: str, *, options: Optional[RequestOptions] = None) -> DatabasesColumnsDisableCalendarFeedResponse:
        """Stops a column's calendar feed; its URL stops working.
        
        `DELETE /api/databases/{databaseId}/columns/{columnId}/calendar-feed`
        """
        return self._request("DELETE", f"/api/databases/{_seg(database_id)}/columns/{_seg(column_id)}/calendar-feed", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def enable_calendar_feed(self, database_id: str, column_id: str, body: DatabasesColumnsEnableCalendarFeedBody, *, options: Optional[RequestOptions] = None) -> DatabasesColumnsEnableCalendarFeedResponse:
        """Publishes a date column as a calendar feed and returns its subscription URL.
        
        `POST /api/databases/{databaseId}/columns/{columnId}/calendar-feed`
        """
        return self._request("POST", f"/api/databases/{_seg(database_id)}/columns/{_seg(column_id)}/calendar-feed", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, database_id: str, column_id: str, *, options: Optional[RequestOptions] = None) -> DatabaseColumn:
        """Returns one column of a table.
        
        `GET /api/databases/{databaseId}/columns/{columnId}`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}/columns/{_seg(column_id)}", query=None, body=None, multipart=False, options=options), "column")  # type: ignore[no-any-return]

    def update(self, database_id: str, column_id: str, body: DatabasesColumnsUpdateBody, *, options: Optional[RequestOptions] = None) -> DatabaseColumn:
        """Changes one column of a table — its name, type or options.
        
        `clearData: true` empties the column in every record — for a type change whose old values mean nothing in the new type. Pointing a relation at another table always empties it.
        
        `PUT /api/databases/{databaseId}/columns/{columnId}`
        """
        return _pick(self._request("PUT", f"/api/databases/{_seg(database_id)}/columns/{_seg(column_id)}", query=None, body=body, multipart=False, options=options), "column")  # type: ignore[no-any-return]


class DatabasesRecordsResource(_Resource):

    def activity(self, database_id: str, record_id: str, *, cursor: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[DatabasesRecordsActivityResponseEntriesItem]:
        """Lists a record's history and logged activity, newest first.
        
        `GET /api/databases/{databaseId}/records/{recordId}/activity`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}/records/{_seg(record_id)}/activity", query={"cursor": cursor, "limit": limit}, body=None, multipart=False, options=options), "entries")  # type: ignore[no-any-return]

    def ai_formula(self, database_id: str, record_id: str, body: DatabasesRecordsAiFormulaBody, *, options: Optional[RequestOptions] = None) -> Any:
        """Computes an AI formula cell — `AI()`, `AI_CLASSIFY()`, `AI_SUMMARIZE()`, `AI_EXTRACT()` — for one record.
        
        Counts against the organization's AI budget.
        
        `POST /api/databases/{databaseId}/records/{recordId}/ai-formula`
        """
        return _pick(self._request("POST", f"/api/databases/{_seg(database_id)}/records/{_seg(record_id)}/ai-formula", query=None, body=body, multipart=False, options=options), "value")  # type: ignore[no-any-return]

    def bulk(self, database_id: str, body: DatabasesRecordsBulkBody, *, options: Optional[RequestOptions] = None) -> DatabasesRecordsBulkResponse:
        """Deletes or duplicates up to 500 records at once.
        
        `POST /api/databases/{databaseId}/records/bulk`
        """
        return self._request("POST", f"/api/databases/{_seg(database_id)}/records/bulk", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create(self, database_id: str, body: CreateRecordInput, *, options: Optional[RequestOptions] = None) -> DatabasesRecordsCreateResponse:
        """Adds one record, or several with `records`.
        
        Counts against the plan's record limit. Linked records must exist and be readable by the caller.
        
        `POST /api/databases/{databaseId}/records`
        """
        return self._request("POST", f"/api/databases/{_seg(database_id)}/records", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete(self, database_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> DatabasesRecordsDeleteResponse:
        """Moves a record to the trash.
        
        `DELETE /api/databases/{databaseId}/records/{recordId}`
        """
        return self._request("DELETE", f"/api/databases/{_seg(database_id)}/records/{_seg(record_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, database_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> DatabaseRecord:
        """Returns one record.
        
        `GET /api/databases/{databaseId}/records/{recordId}`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}/records/{_seg(record_id)}", query=None, body=None, multipart=False, options=options), "record")  # type: ignore[no-any-return]

    def links(self, database_id: str, record_id: str, *, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the records of other tables that link to a record and the caller may see.
        
        `GET /api/databases/{databaseId}/records/{recordId}/links`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}/records/{_seg(record_id)}/links", query=None, body=None, multipart=False, options=options), "links")  # type: ignore[no-any-return]

    def list(self, database_id: str, *, limit: Optional[int] = None, offset: Optional[int] = None, sort_by: Optional[str] = None, sort_direction: Optional[Literal["asc", "desc"]] = None, filters: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[DatabaseRecord]:
        """Lists a table's records, filtered and sorted.
        
        `GET /api/databases/{databaseId}/records`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}/records", query={"limit": limit, "offset": offset, "sortBy": sort_by, "sortDirection": sort_direction, "filters": filters}, body=None, multipart=False, options=options), "records")  # type: ignore[no-any-return]

    def update(self, database_id: str, record_id: str, body: UpdateRecordInput, *, options: Optional[RequestOptions] = None) -> DatabaseRecord:
        """Changes a record's cells.
        
        `PATCH /api/databases/{databaseId}/records/{recordId}`
        """
        return _pick(self._request("PATCH", f"/api/databases/{_seg(database_id)}/records/{_seg(record_id)}", query=None, body=body, multipart=False, options=options), "record")  # type: ignore[no-any-return]


class DatabasesSharesResource(_Resource):

    def list(self, database_id: str, *, include: Optional[Literal["candidates"]] = None, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[DatabasesSharesListResponseSharesItem]:
        """Lists who a table is shared with, and at what level.
        
        `GET /api/databases/{databaseId}/shares`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}/shares", query={"include": include, "q": q}, body=None, multipart=False, options=options), "shares")  # type: ignore[no-any-return]

    def remove(self, database_id: str, user_id: str, *, options: Optional[RequestOptions] = None) -> DatabasesSharesRemoveResponse:
        """Stops sharing a table with a person.
        
        `DELETE /api/databases/{databaseId}/shares/{userId}`
        """
        return self._request("DELETE", f"/api/databases/{_seg(database_id)}/shares/{_seg(user_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set(self, database_id: str, body: DatabasesSharesSetBody, *, options: Optional[RequestOptions] = None) -> DatabasesSharesSetResponseShare:
        """Shares a table with a person, or changes their level.
        
        `PUT /api/databases/{databaseId}/shares`
        """
        return _pick(self._request("PUT", f"/api/databases/{_seg(database_id)}/shares", query=None, body=body, multipart=False, options=options), "share")  # type: ignore[no-any-return]


class DatabasesResource(_Resource):
    """Databases
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.columns = DatabasesColumnsResource(request)
        self.records = DatabasesRecordsResource(request)
        self.shares = DatabasesSharesResource(request)

    def activity(self, database_id: str, *, cursor: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[DatabasesActivityResponseEntriesItem]:
        """Lists what happened in a table — records and columns added, changed, deleted — newest first.
        
        `GET /api/databases/{databaseId}/activity`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}/activity", query={"cursor": cursor, "limit": limit}, body=None, multipart=False, options=options), "entries")  # type: ignore[no-any-return]

    def create(self, body: DatabasesCreateBody, *, options: Optional[RequestOptions] = None) -> Database:
        """Creates a table, optionally with its columns.
        
        Needs `database.create`.
        
        `POST /api/databases`
        """
        return _pick(self._request("POST", f"/api/databases", query=None, body=body, multipart=False, options=options), "database")  # type: ignore[no-any-return]

    def delete(self, database_id: str, *, options: Optional[RequestOptions] = None) -> DatabasesDeleteResponse:
        """Moves a table and its records to the trash.
        
        `DELETE /api/databases/{databaseId}`
        """
        return self._request("DELETE", f"/api/databases/{_seg(database_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, database_id: str, *, include: Optional[Literal["schemaAccess"]] = None, options: Optional[RequestOptions] = None) -> Database:
        """Returns a table with its columns and views, and what the caller may do with it.
        
        `GET /api/databases/{databaseId}`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}", query={"include": include}, body=None, multipart=False, options=options), "database")  # type: ignore[no-any-return]

    def import_(self, database_id: str, body: Union[DatabasesImportBody, Dict[str, Any]], *, options: Optional[RequestOptions] = None) -> DatabasesImportResponse:
        """Imports a CSV file into a table, or with `dryRun` says what an import would do.
        
        Needs edit access. `options` maps each file column to an existing column, a new one, or nothing, and says how numbers, dates, invalid values and duplicates are handled. The plan's record limit applies to the whole file. An .xlsx is refused — save it as CSV.
        
        `POST /api/databases/{databaseId}/import`
        """
        return self._request("POST", f"/api/databases/{_seg(database_id)}/import", query=None, body=body, multipart=True, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, workspace_id: Optional[str] = None, visibility: Optional[Literal["private", "organization", "workspace"]] = None, search: Optional[str] = None, folder: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Database]:
        """Lists the tables of an organization or workspace the caller can open.
        
        `GET /api/databases`
        """
        return _pick(self._request("GET", f"/api/databases", query={"organizationId": organization_id, "workspaceId": workspace_id, "visibility": visibility, "search": search, "folder": folder, "page": page, "limit": limit}, body=None, multipart=False, options=options), "databases")  # type: ignore[no-any-return]

    def people(self, database_id: str, *, options: Optional[RequestOptions] = None) -> List[DatabasesPeopleResponsePeopleItem]:
        """Lists the people a table's person cells can name, and those they already name.
        
        `GET /api/databases/{databaseId}/people`
        """
        return _pick(self._request("GET", f"/api/databases/{_seg(database_id)}/people", query=None, body=None, multipart=False, options=options), "people")  # type: ignore[no-any-return]

    def update(self, database_id: str, body: DatabasesUpdateBody, *, options: Optional[RequestOptions] = None) -> Database:
        """Changes a table's name, look, visibility, columns, views or settings.
        
        `columns`, when sent, is the whole column list. A relation column whose pair in the linked table changes too is reported in `inverse`.
        
        `PATCH /api/databases/{databaseId}`
        """
        return _pick(self._request("PATCH", f"/api/databases/{_seg(database_id)}", query=None, body=body, multipart=False, options=options), "database")  # type: ignore[no-any-return]


class DocumentsCommentsResource(_Resource):

    def create(self, document_id: str, page_id: str, body: DocumentsCommentsCreateBody, *, options: Optional[RequestOptions] = None) -> DocumentComment:
        """Comments on a page, or answers a comment.
        
        Needs `document:resolve` and comment access, and comments allowed on the document. The people named and the thread's participants who can open the page are notified. Threads nest five levels at most.
        
        `POST /api/documents/{documentId}/pages/{pageId}/comments`
        """
        return _pick(self._request("POST", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}/comments", query=None, body=body, multipart=False, options=options), "comment")  # type: ignore[no-any-return]

    def delete(self, document_id: str, page_id: str, comment_id: str, *, options: Optional[RequestOptions] = None) -> DocumentsCommentsDeleteResponse:
        """Deletes a comment (its author only).
        
        `DELETE /api/documents/{documentId}/pages/{pageId}/comments/{commentId}`
        """
        return self._request("DELETE", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}/comments/{_seg(comment_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, document_id: str, page_id: str, *, options: Optional[RequestOptions] = None) -> List[DocumentComment]:
        """Lists the comments on a page, threaded by `parentId`, with their reactions.
        
        `GET /api/documents/{documentId}/pages/{pageId}/comments`
        """
        return _pick(self._request("GET", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}/comments", query=None, body=None, multipart=False, options=options), "comments")  # type: ignore[no-any-return]

    def react(self, document_id: str, page_id: str, comment_id: str, body: DocumentsCommentsReactBody, *, options: Optional[RequestOptions] = None) -> bool:
        """Adds the caller's reaction to a comment, or takes it away again.
        
        `PUT /api/documents/{documentId}/pages/{pageId}/comments/{commentId}/react`
        """
        return _pick(self._request("PUT", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}/comments/{_seg(comment_id)}/react", query=None, body=body, multipart=False, options=options), "reacted")  # type: ignore[no-any-return]

    def update(self, document_id: str, page_id: str, comment_id: str, body: DocumentsCommentsUpdateBody, *, options: Optional[RequestOptions] = None) -> DocumentComment:
        """Edits a comment's text (its author only), or resolves and reopens its thread.
        
        `PATCH /api/documents/{documentId}/pages/{pageId}/comments/{commentId}`
        """
        return _pick(self._request("PATCH", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}/comments/{_seg(comment_id)}", query=None, body=body, multipart=False, options=options), "comment")  # type: ignore[no-any-return]


class DocumentsMailMergeResource(_Resource):

    def clear(self, document_id: str, *, options: Optional[RequestOptions] = None) -> DocumentsMailMergeClearResponse:
        """Clears a document's mail merge source; the fields stay in the text.
        
        `DELETE /api/documents/{documentId}/mail-merge`
        """
        return self._request("DELETE", f"/api/documents/{_seg(document_id)}/mail-merge", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, document_id: str, *, row: Optional[int] = None, options: Optional[RequestOptions] = None) -> DocumentsMailMergeGetResponse:
        """A document's mail merge: its source database and columns, the views to choose from, how many rows it covers, and optionally one row's values.
        
        The rows are always read as the caller. `source` is null when none is set; `refused` says why a set source cannot be read by the caller. `blocked` is the reason an export would refuse the merge.
        
        `GET /api/documents/{documentId}/mail-merge`
        """
        return self._request("GET", f"/api/documents/{_seg(document_id)}/mail-merge", query={"row": row}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, document_id: str, body: DocumentsMailMergeUpdateBody, *, options: Optional[RequestOptions] = None) -> DocumentsMailMergeUpdateResponse:
        """Sets or changes a document's mail merge source, view and sort.
        
        Needs `document:update` and edit access. A partial update: `databaseId` is needed only for the first source, and a different one starts over. Only a database of the document's organisation the caller may read, a usable view of it, a column of it.
        
        `PUT /api/documents/{documentId}/mail-merge`
        """
        return self._request("PUT", f"/api/documents/{_seg(document_id)}/mail-merge", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class DocumentsPagesResource(_Resource):

    def backlinks(self, document_id: str, page_id: str, *, options: Optional[RequestOptions] = None) -> List[DocumentsPagesBacklinksResponseBacklinksItem]:
        """The pages of the document that link to this page.
        
        `GET /api/documents/{documentId}/backlinks/{pageId}`
        """
        return _pick(self._request("GET", f"/api/documents/{_seg(document_id)}/backlinks/{_seg(page_id)}", query=None, body=None, multipart=False, options=options), "backlinks")  # type: ignore[no-any-return]

    def create(self, document_id: str, body: DocumentsPagesCreateBody, *, options: Optional[RequestOptions] = None) -> DocumentPage:
        """Adds an empty page to a document, at the end of its parent's children.
        
        Needs `document:update` and edit access; counts against the plan's page limit. Pages nest six levels deep at most (409 `depth`). A sensitivity other than `none` needs sensitive blocks on the plan, else the page is plain.
        
        `POST /api/documents/{documentId}/pages`
        """
        return _pick(self._request("POST", f"/api/documents/{_seg(document_id)}/pages", query=None, body=body, multipart=False, options=options), "page")  # type: ignore[no-any-return]

    def delete(self, document_id: str, page_id: str, *, options: Optional[RequestOptions] = None) -> DocumentsPagesDeleteResponse:
        """Deletes a page and its subpages.
        
        Refused (403 `pageHasRestrictedSubpages`) when a subpage is one the caller may not edit.
        
        `DELETE /api/documents/{documentId}/pages/{pageId}`
        """
        return self._request("DELETE", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, document_id: str, page_id: str, *, options: Optional[RequestOptions] = None) -> DocumentPage:
        """One page with its content.
        
        `GET /api/documents/{documentId}/pages/{pageId}`
        """
        return _pick(self._request("GET", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}", query=None, body=None, multipart=False, options=options), "page")  # type: ignore[no-any-return]

    def list(self, document_id: str, *, options: Optional[RequestOptions] = None) -> List[DocumentPage]:
        """Lists the pages of a document the caller may read, in tree order, without their content.
        
        `GET /api/documents/{documentId}/pages`
        """
        return _pick(self._request("GET", f"/api/documents/{_seg(document_id)}/pages", query=None, body=None, multipart=False, options=options), "pages")  # type: ignore[no-any-return]

    def update(self, document_id: str, page_id: str, body: DocumentsPagesUpdateBody, *, options: Optional[RequestOptions] = None) -> DocumentPage:
        """Changes a page's details (`mode: "meta"`) or replaces its content (`mode: "content"`).
        
        Needs `document:update` and edit access to the page.
        
        - **meta**: title, icon, place in the tree, status, sensitivity, visibility, header. Publishing a page of a document that requires approval files an approval instead (`approvalWorkflowId`).
        - **content**: `contentJson` (a ProseMirror document) and `contentHtml`. With `baseUpdatedAt`, a page changed since answers 409 `conflictReload` with what it holds now. With `locale`, the content is that language's translation. A version is kept at most once an hour, or when `snapshotVersion` is set.
        
        `PATCH /api/documents/{documentId}/pages/{pageId}`
        """
        return _pick(self._request("PATCH", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}", query=None, body=body, multipart=False, options=options), "page")  # type: ignore[no-any-return]


class DocumentsSharesResource(_Resource):

    def create(self, document_id: str, body: DocumentsSharesCreateBody, *, options: Optional[RequestOptions] = None) -> DocumentShare:
        """Creates a public share link to a document or one of its pages.
        
        Needs `document:share`, edit access, public pages on the plan; counts against the plan's limit of public documents. Anyone with the link can read what it shares.
        
        `POST /api/documents/{documentId}/shares`
        """
        return _pick(self._request("POST", f"/api/documents/{_seg(document_id)}/shares", query=None, body=body, multipart=False, options=options), "share")  # type: ignore[no-any-return]

    def list(self, document_id: str, *, options: Optional[RequestOptions] = None) -> List[DocumentShare]:
        """Lists a document's live share links.
        
        The link's secret `token` only for a caller who may edit the document.
        
        `GET /api/documents/{documentId}/shares`
        """
        return _pick(self._request("GET", f"/api/documents/{_seg(document_id)}/shares", query=None, body=None, multipart=False, options=options), "shares")  # type: ignore[no-any-return]

    def revoke(self, document_id: str, share_id: str, *, options: Optional[RequestOptions] = None) -> DocumentsSharesRevokeResponse:
        """Revokes a share link; it stops working at once.
        
        `DELETE /api/documents/{documentId}/shares/{shareId}`
        """
        return self._request("DELETE", f"/api/documents/{_seg(document_id)}/shares/{_seg(share_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class DocumentsVersionsResource(_Resource):

    def get(self, document_id: str, page_id: str, version_id: str, *, options: Optional[RequestOptions] = None) -> DocumentsVersionsGetResponseVersion:
        """One saved version of a page, with its content.
        
        `GET /api/documents/{documentId}/pages/{pageId}/versions/{versionId}`
        """
        return _pick(self._request("GET", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}/versions/{_seg(version_id)}", query=None, body=None, multipart=False, options=options), "version")  # type: ignore[no-any-return]

    def list(self, document_id: str, page_id: str, *, options: Optional[RequestOptions] = None) -> List[DocumentVersionSummary]:
        """Lists a page's saved versions, newest first, without their content.
        
        Without longer version history on the plan, only the 30 newest (`trimmed`).
        
        `GET /api/documents/{documentId}/pages/{pageId}/versions`
        """
        return _pick(self._request("GET", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}/versions", query=None, body=None, multipart=False, options=options), "versions")  # type: ignore[no-any-return]

    def restore(self, document_id: str, page_id: str, version_id: str, *, options: Optional[RequestOptions] = None) -> DocumentPage:
        """Puts a saved version back as the page's content.
        
        `POST /api/documents/{documentId}/pages/{pageId}/versions/{versionId}`
        """
        return _pick(self._request("POST", f"/api/documents/{_seg(document_id)}/pages/{_seg(page_id)}/versions/{_seg(version_id)}", query=None, body=None, multipart=False, options=options), "page")  # type: ignore[no-any-return]


class DocumentsResource(_Resource):
    """Documents — The Documents hub: documents made of a tree of pages, with comments, versions, share links and mail merge.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.comments = DocumentsCommentsResource(request)
        self.mail_merge = DocumentsMailMergeResource(request)
        self.pages = DocumentsPagesResource(request)
        self.shares = DocumentsSharesResource(request)
        self.versions = DocumentsVersionsResource(request)

    def bulk(self, body: DocumentsBulkBody, *, options: Optional[RequestOptions] = None) -> DocumentsBulkResponse:
        """Deletes, duplicates or changes the visibility of up to 500 documents at once.
        
        Needs `document:update`; each document also needs edit access. A document that fails does not fail the batch: it is listed in `failed` with a reason (`not_found`, `forbidden`, `limit`, …).
        
        `POST /api/documents/bulk`
        """
        return self._request("POST", f"/api/documents/bulk", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def compare(self, document_id: str, *, against: str, options: Optional[RequestOptions] = None) -> DocumentsCompareResponse:
        """The paragraphs of two documents, ready to be compared.
        
        Each side holds only the pages the caller may read; a vault page's text is never included. The comparison itself is left to the caller.
        
        `GET /api/documents/{documentId}/compare`
        """
        return self._request("GET", f"/api/documents/{_seg(document_id)}/compare", query={"against": against}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def create(self, body: DocumentsCreateBody, *, options: Optional[RequestOptions] = None) -> Document:
        """Creates a document, empty or from a template.
        
        Needs `document:create` and the Documents hub on the plan; counts against the plan's document limit. The caller becomes its admin.
        
        `POST /api/documents`
        """
        return _pick(self._request("POST", f"/api/documents", query=None, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def delete(self, document_id: str, *, purge: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> DocumentsDeleteResponse:
        """Moves a document to the trash, or deletes a trashed one for good with `purge=1`.
        
        Needs `document:delete` and edit access. Purging refuses (409) a document that is not in the trash, so no single request takes a live document to nothing.
        
        `DELETE /api/documents/{documentId}`
        """
        return self._request("DELETE", f"/api/documents/{_seg(document_id)}", query={"purge": purge}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def duplicate(self, document_id: str, body: DocumentsDuplicateBody, *, options: Optional[RequestOptions] = None) -> Document:
        """Copies a document with the pages the caller may read.
        
        Needs `document:create` and read access; counts against the plan's document limit.
        
        `POST /api/documents/{documentId}/duplicate`
        """
        return _pick(self._request("POST", f"/api/documents/{_seg(document_id)}/duplicate", query=None, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def export(self, document_id: str, *, format: Optional[Literal["docx", "pdf", "md", "html"]] = None, pages: Optional[str] = None, merge: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a document as a Word, PDF, Markdown or HTML file.
        
        Answers the file itself. Pages the caller may not read are left out; a vault page is listed as a note, never with its text.
        
        `GET /api/documents/{documentId}/export`
        """
        return self._request("GET", f"/api/documents/{_seg(document_id)}/export", query={"format": format, "pages": pages, "merge": merge}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, document_id: str, *, options: Optional[RequestOptions] = None) -> Document:
        """One document, with what the caller may do with it.
        
        `GET /api/documents/{documentId}`
        """
        return _pick(self._request("GET", f"/api/documents/{_seg(document_id)}", query=None, body=None, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def google(self, *, organization_id: str, connection_id: Optional[str] = None, q: Optional[str] = None, page_token: Optional[str] = None, options: Optional[RequestOptions] = None) -> DocumentsGoogleResponse:
        """The Google accounts the caller can import from and, with `connectionId`, their Google documents.
        
        A Google account is connected in the dashboard (Migration Center), which needs `migration:create` — reported as `canConnect`.
        
        `GET /api/documents/google`
        """
        return self._request("GET", f"/api/documents/google", query={"organizationId": organization_id, "connectionId": connection_id, "q": q, "pageToken": page_token}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def import_(self, document_id: str, body: DocumentsImportBody, *, options: Optional[RequestOptions] = None) -> DocumentsImportResponse:
        """Imports Markdown, HTML or a Google document into a document as new pages.
        
        Needs `document:update` and edit access; counts against the plan's page limit. Top-level headings become pages and the next level their subpages. Send one of `markdown`, `html`, or `googleConnectionId` with `googleFileId` (GET /api/documents/google lists them). A .docx, .md or .html file can be sent instead as multipart form data in a `file` field (20 MB at most).
        
        `POST /api/documents/{documentId}/import`
        """
        return self._request("POST", f"/api/documents/{_seg(document_id)}/import", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, workspace_id: Optional[str] = None, search: Optional[str] = None, tag: Optional[str] = None, folder: Optional[str] = None, folder_workspace_id: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, trash: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> List[Document]:
        """Lists one page of the documents the caller may open, with counts.
        
        Needs `document:read` and the Documents hub on the plan. One of `organizationId` and `workspaceId` is required. With `trash=1` (and `organizationId`) it lists the organisation's trashed documents instead, all at once.
        
        `GET /api/documents`
        """
        return _pick(self._request("GET", f"/api/documents", query={"organizationId": organization_id, "workspaceId": workspace_id, "search": search, "tag": tag, "folder": folder, "folderWorkspaceId": folder_workspace_id, "page": page, "limit": limit, "trash": trash}, body=None, multipart=False, options=options), "documents")  # type: ignore[no-any-return]

    def move(self, document_id: str, body: DocumentsMoveBody, *, options: Optional[RequestOptions] = None) -> DocumentsMoveResponse:
        """Moves a document to another workspace of its organisation, or to none.
        
        Needs `document:update`, edit access, and membership of the destination workspace.
        
        `PUT /api/documents/{documentId}/move`
        """
        return self._request("PUT", f"/api/documents/{_seg(document_id)}/move", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def restore(self, document_id: str, *, options: Optional[RequestOptions] = None) -> bool:
        """Takes a document back out of the trash.
        
        Needs `document:delete` and edit access. `restored: false` when it was not in the trash.
        
        `POST /api/documents/{documentId}/restore`
        """
        return _pick(self._request("POST", f"/api/documents/{_seg(document_id)}/restore", query=None, body=None, multipart=False, options=options), "restored")  # type: ignore[no-any-return]

    def search(self, *, q: str, organization_id: str, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[DocumentsSearchResponseHitsItem]:
        """Searches the names, page titles and text of the documents the caller may open.
        
        Restricted and vault pages are never searched. Fewer than two characters find nothing.
        
        `GET /api/documents/search`
        """
        return _pick(self._request("GET", f"/api/documents/search", query={"q": q, "organizationId": organization_id, "workspaceId": workspace_id}, body=None, multipart=False, options=options), "hits")  # type: ignore[no-any-return]

    def set_favorite(self, document_id: str, body: DocumentsSetFavoriteBody, *, options: Optional[RequestOptions] = None) -> bool:
        """Stars a document for the caller, or unstars it.
        
        `PUT /api/documents/{documentId}/favorite`
        """
        return _pick(self._request("PUT", f"/api/documents/{_seg(document_id)}/favorite", query=None, body=body, multipart=False, options=options), "favorite")  # type: ignore[no-any-return]

    def templates(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> List[DocumentTemplate]:
        """Lists the document templates: the platform's and the organisation's own, most used first.
        
        `GET /api/documents/templates`
        """
        return _pick(self._request("GET", f"/api/documents/templates", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "templates")  # type: ignore[no-any-return]

    def update(self, document_id: str, body: DocumentsUpdateBody, *, options: Optional[RequestOptions] = None) -> Document:
        """Changes a document's name, description, icon, cover, visibility, access list, settings, AI indexing or tags.
        
        Needs `document:update` and edit access. Only the fields sent change. Changing `permissions` needs the document's creator or one of its admins; narrowing access closes the live editing sessions of who lost it.
        
        `PATCH /api/documents/{documentId}`
        """
        return _pick(self._request("PATCH", f"/api/documents/{_seg(document_id)}", query=None, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]


class EndpointsResource(_Resource):
    """API endpoints — APIs you build on the platform and publish to your own callers.
    """

    def consumers(self, endpoint_id: str, *, options: Optional[RequestOptions] = None) -> List[EndpointsConsumersResponseDataItemsItem]:
        """Lists who calls an endpoint: each API key with the routes it called and how often.
        
        `GET /api/endpoints/{endpointId}/consumers`
        """
        return _pick(self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/consumers", query=None, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def create(self, body: CreateEndpointInput, *, options: Optional[RequestOptions] = None) -> Endpoint:
        """Creates an API endpoint.
        
        `POST /api/endpoints`
        """
        return _pick(self._request("POST", f"/api/endpoints", query=None, body=body, multipart=False, options=options), "endpoint")  # type: ignore[no-any-return]

    def create_api_key(self, endpoint_id: str, body: CreateEndpointApiKeyInput, *, options: Optional[RequestOptions] = None) -> EndpointApiKey:
        """Creates an API key for an endpoint's callers; the answer carries the key, once.
        
        `POST /api/endpoints/{endpointId}/api-keys`
        """
        return self._request("POST", f"/api/endpoints/{_seg(endpoint_id)}/api-keys", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create_env_var(self, endpoint_id: str, body: CreateEndpointEnvVarInput, *, options: Optional[RequestOptions] = None) -> EndpointEnvVar:
        """Adds an environment variable to an endpoint.
        
        `POST /api/endpoints/{endpointId}/env`
        """
        return _pick(self._request("POST", f"/api/endpoints/{_seg(endpoint_id)}/env", query=None, body=body, multipart=False, options=options), "envVar")  # type: ignore[no-any-return]

    def create_webhook(self, endpoint_id: str, body: CreateEndpointWebhookInput, *, options: Optional[RequestOptions] = None) -> EndpointsCreateWebhookResponse:
        """Adds a webhook to an endpoint; the answer carries its signing secret, once.
        
        `POST /api/endpoints/{endpointId}/webhooks`
        """
        return self._request("POST", f"/api/endpoints/{_seg(endpoint_id)}/webhooks", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete(self, endpoint_id: str, *, options: Optional[RequestOptions] = None) -> EndpointsDeleteResponse:
        """Moves an endpoint to the trash; its URL stops answering.
        
        `DELETE /api/endpoints/{endpointId}`
        """
        return self._request("DELETE", f"/api/endpoints/{_seg(endpoint_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_api_key(self, endpoint_id: str, key_id: str, *, options: Optional[RequestOptions] = None) -> EndpointsDeleteApiKeyResponse:
        """Revokes an endpoint API key.
        
        `DELETE /api/endpoints/{endpointId}/api-keys/{keyId}`
        """
        return self._request("DELETE", f"/api/endpoints/{_seg(endpoint_id)}/api-keys/{_seg(key_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_env_var(self, endpoint_id: str, var_id: str, *, options: Optional[RequestOptions] = None) -> EndpointsDeleteEnvVarResponse:
        """Removes an environment variable from an endpoint.
        
        `DELETE /api/endpoints/{endpointId}/env/{varId}`
        """
        return self._request("DELETE", f"/api/endpoints/{_seg(endpoint_id)}/env/{_seg(var_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_webhook(self, endpoint_id: str, webhook_id: str, *, options: Optional[RequestOptions] = None) -> EndpointsDeleteWebhookResponse:
        """Removes a webhook from an endpoint.
        
        `DELETE /api/endpoints/{endpointId}/webhooks/{webhookId}`
        """
        return self._request("DELETE", f"/api/endpoints/{_seg(endpoint_id)}/webhooks/{_seg(webhook_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def dependencies(self, endpoint_id: str, *, options: Optional[RequestOptions] = None) -> EndpointsDependenciesResponseData:
        """Lists what an endpoint's routes use: workflows, tables and environment variables.
        
        `GET /api/endpoints/{endpointId}/dependencies`
        """
        return _pick(self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/dependencies", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def explain_capture(self, endpoint_id: str, body: EndpointsExplainCaptureBody, *, options: Optional[RequestOptions] = None) -> EndpointsExplainCaptureResponseData:
        """Explains with AI why a recorded request failed and how to fix it.
        
        Counts against the organization's AI budget.
        
        `POST /api/endpoints/{endpointId}/explain`
        """
        return _pick(self._request("POST", f"/api/endpoints/{_seg(endpoint_id)}/explain", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, endpoint_id: str, *, options: Optional[RequestOptions] = None) -> Endpoint:
        """Returns an endpoint with its versions, routes and the URL callers reach it at.
        
        `GET /api/endpoints/{endpointId}`
        """
        return self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_activity(self, endpoint_id: str, *, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[EndpointsGetActivityResponseActivitiesItem]:
        """Lists what happened to an endpoint — deploys, changes, errors — newest first.
        
        `GET /api/endpoints/{endpointId}/activity`
        """
        return _pick(self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/activity", query={"limit": limit}, body=None, multipart=False, options=options), "activities")  # type: ignore[no-any-return]

    def get_analytics(self, endpoint_id: str, *, version: Optional[str] = None, time_range: Optional[Literal["24h", "7d", "30d", "90d"]] = None, options: Optional[RequestOptions] = None) -> EndpointsGetAnalyticsResponse:
        """Returns an endpoint's requests, errors and response times, overall and per version.
        
        `GET /api/endpoints/{endpointId}/analytics`
        """
        return self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/analytics", query={"version": version, "timeRange": time_range}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_auth_config(self, endpoint_id: str, *, options: Optional[RequestOptions] = None) -> EndpointAuthConfig:
        """Returns how an endpoint checks a JWT or OAuth2 bearer token; never a secret, only whether one is stored.
        
        `GET /api/endpoints/{endpointId}/auth-config`
        """
        return self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/auth-config", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_capture(self, endpoint_id: str, capture_id: str, *, options: Optional[RequestOptions] = None) -> EndpointsGetCaptureResponseData:
        """Returns one recorded request of an endpoint, with its request and response.
        
        `GET /api/endpoints/{endpointId}/captures/{captureId}`
        """
        return _pick(self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/captures/{_seg(capture_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_docs(self, endpoint_id: str, *, version: Optional[str] = None, format: Optional[Literal["json", "yaml"]] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Returns an OpenAPI description of an endpoint for its callers.
        
        With `format=yaml` the answer is YAML text.
        
        `GET /api/endpoints/{endpointId}/docs`
        """
        return self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/docs", query={"version": version, "format": format}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_timings(self, endpoint_id: str, metric_id: str, *, options: Optional[RequestOptions] = None) -> EndpointsGetTimingsResponseData:
        """Returns where the time of one request went, step by step.
        
        `GET /api/endpoints/{endpointId}/waterfall/{metricId}`
        """
        return _pick(self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/waterfall/{_seg(metric_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, workspace_id: Optional[str] = None, search: Optional[str] = None, folder: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Endpoint]:
        """Lists the API endpoints of an organization the caller may open.
        
        `GET /api/endpoints`
        """
        return _pick(self._request("GET", f"/api/endpoints", query={"organizationId": organization_id, "workspaceId": workspace_id, "search": search, "folder": folder, "page": page, "limit": limit}, body=None, multipart=False, options=options), "endpoints")  # type: ignore[no-any-return]

    def list_api_keys(self, endpoint_id: str, *, options: Optional[RequestOptions] = None) -> List[EndpointApiKey]:
        """Lists the API keys callers use for an endpoint, without the keys themselves.
        
        `GET /api/endpoints/{endpointId}/api-keys`
        """
        return self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/api-keys", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_captures(self, endpoint_id: str, *, errors_only: Optional[Literal["true"]] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[EndpointsListCapturesResponseDataItemsItem]:
        """Lists the recorded requests of an endpoint, newest first.
        
        `GET /api/endpoints/{endpointId}/captures`
        """
        return _pick(self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/captures", query={"errorsOnly": errors_only, "limit": limit}, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def list_env_vars(self, endpoint_id: str, *, options: Optional[RequestOptions] = None) -> List[EndpointEnvVar]:
        """Lists an endpoint's environment variables; secret values are masked.
        
        `GET /api/endpoints/{endpointId}/env`
        """
        return self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/env", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_webhooks(self, endpoint_id: str, *, options: Optional[RequestOptions] = None) -> List[EndpointWebhook]:
        """Lists the webhooks an endpoint calls on its events, without their secrets.
        
        `GET /api/endpoints/{endpointId}/webhooks`
        """
        return self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/webhooks", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def log_activity(self, endpoint_id: str, body: EndpointsLogActivityBody, *, options: Optional[RequestOptions] = None) -> EndpointsLogActivityResponse:
        """Writes a note into an endpoint's activity — a deploy, a rollback, a config change.
        
        `POST /api/endpoints/{endpointId}/activity`
        """
        return self._request("POST", f"/api/endpoints/{_seg(endpoint_id)}/activity", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def replace(self, endpoint_id: str, body: UpdateEndpointInput, *, options: Optional[RequestOptions] = None) -> Endpoint:
        """Changes an endpoint — its routes, versions, auth or settings — and records the change in its history.
        
        `PUT /api/endpoints/{endpointId}`
        """
        return self._request("PUT", f"/api/endpoints/{_seg(endpoint_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def shadow_results(self, endpoint_id: str, *, diverged_only: Optional[Literal["true"]] = None, options: Optional[RequestOptions] = None) -> EndpointsShadowResultsResponseData:
        """Compares a shadow version's answers with the live version's, request by request.
        
        `GET /api/endpoints/{endpointId}/shadow-results`
        """
        return _pick(self._request("GET", f"/api/endpoints/{_seg(endpoint_id)}/shadow-results", query={"divergedOnly": diverged_only}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def suspend_api_key(self, endpoint_id: str, key_id: str, body: EndpointsSuspendApiKeyBody, *, options: Optional[RequestOptions] = None) -> EndpointsSuspendApiKeyResponseData:
        """Suspends an endpoint API key, or resumes it.
        
        `POST /api/endpoints/{endpointId}/api-keys/{keyId}/suspend`
        """
        return _pick(self._request("POST", f"/api/endpoints/{_seg(endpoint_id)}/api-keys/{_seg(key_id)}/suspend", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def test_auth(self, endpoint_id: str, body: EndpointsTestAuthBody, *, options: Optional[RequestOptions] = None) -> EndpointsTestAuthResponse:
        """Checks whether the endpoint's saved token setup accepts a token, and if not, why.
        
        The token is used for this check only; it is neither logged nor stored.
        
        `POST /api/endpoints/{endpointId}/auth-test`
        """
        return self._request("POST", f"/api/endpoints/{_seg(endpoint_id)}/auth-test", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, endpoint_id: str, body: UpdateEndpointInput, *, options: Optional[RequestOptions] = None) -> Endpoint:
        """Changes an endpoint without a new history entry — how a restore from its history is saved.
        
        `PATCH /api/endpoints/{endpointId}`
        """
        return _pick(self._request("PATCH", f"/api/endpoints/{_seg(endpoint_id)}", query=None, body=body, multipart=False, options=options), "endpoint")  # type: ignore[no-any-return]

    def update_auth_config(self, endpoint_id: str, body: EndpointsUpdateAuthConfigBody, *, options: Optional[RequestOptions] = None) -> EndpointAuthConfig:
        """Sets how an endpoint checks a JWT or OAuth2 bearer token.
        
        A blank secret keeps the stored one. An HS256 secret has at least 32 bytes.
        
        `PUT /api/endpoints/{endpointId}/auth-config`
        """
        return self._request("PUT", f"/api/endpoints/{_seg(endpoint_id)}/auth-config", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_env_var(self, endpoint_id: str, var_id: str, body: EndpointsUpdateEnvVarBody, *, options: Optional[RequestOptions] = None) -> EndpointEnvVar:
        """Changes an endpoint's environment variable; only the fields sent change.
        
        `PATCH /api/endpoints/{endpointId}/env/{varId}`
        """
        return _pick(self._request("PATCH", f"/api/endpoints/{_seg(endpoint_id)}/env/{_seg(var_id)}", query=None, body=body, multipart=False, options=options), "envVar")  # type: ignore[no-any-return]

    def update_webhook(self, endpoint_id: str, webhook_id: str, body: EndpointsUpdateWebhookBody, *, options: Optional[RequestOptions] = None) -> EndpointWebhook:
        """Changes an endpoint webhook's URL, events or state.
        
        `PATCH /api/endpoints/{endpointId}/webhooks/{webhookId}`
        """
        return self._request("PATCH", f"/api/endpoints/{_seg(endpoint_id)}/webhooks/{_seg(webhook_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class FeatureGatesResource(_Resource):
    """Feature gates
    """

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> FeatureGates:
        """Returns which features are on for the caller, by gate key.
        
        Each gate is evaluated for the caller, their roles and, with `organizationId`, that organisation's plan. `platform:marketplace` says whether the marketplace is switched on; while it is off every `marketplace*` gate is `false`. Cached privately for 60 seconds.
        
        `GET /api/feature-gates`
        """
        return _pick(self._request("GET", f"/api/feature-gates", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class FeatureRequestsResource(_Resource):
    """Feature requests — The platform's public roadmap: ideas every signed-in person can submit, vote on and discuss.
    """

    def add_comment(self, id: str, body: FeatureRequestsAddCommentBody, *, options: Optional[RequestOptions] = None) -> FeatureRequestComment:
        """Comments on a feature request.
        
        Its submitter is notified.
        
        `POST /api/feature-requests/{id}/comments`
        """
        return _pick(self._request("POST", f"/api/feature-requests/{_seg(id)}/comments", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: FeatureRequestsCreateBody, *, options: Optional[RequestOptions] = None) -> FeatureRequest:
        """Submits a feature request, with the caller's vote on it.
        
        The platform's administrators are notified.
        
        `POST /api/feature-requests`
        """
        return _pick(self._request("POST", f"/api/feature-requests", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, id: str, *, options: Optional[RequestOptions] = None) -> FeatureRequestsGetResponseData:
        """Returns one feature request with its comments and whether the caller voted.
        
        `GET /api/feature-requests/{id}`
        """
        return _pick(self._request("GET", f"/api/feature-requests/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, status: Optional[str] = None, category: Optional[FeatureRequestCategory] = None, sort: Optional[Literal["upvotes", "newest"]] = None, options: Optional[RequestOptions] = None) -> List[FeatureRequestsListResponseDataItem]:
        """Lists up to 500 feature requests, most voted or newest first, with whether the caller voted.
        
        `GET /api/feature-requests`
        """
        return _pick(self._request("GET", f"/api/feature-requests", query={"status": status, "category": category, "sort": sort}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_comments(self, id: str, *, options: Optional[RequestOptions] = None) -> List[FeatureRequestsListCommentsResponseDataItem]:
        """Lists a feature request's comments, oldest first.
        
        `GET /api/feature-requests/{id}/comments`
        """
        return _pick(self._request("GET", f"/api/feature-requests/{_seg(id)}/comments", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def unvote(self, id: str, *, options: Optional[RequestOptions] = None) -> FeatureRequestsUnvoteResponseData:
        """Takes back the caller's vote on a feature request.
        
        Answers 404 when the caller had not voted.
        
        `DELETE /api/feature-requests/{id}/vote`
        """
        return _pick(self._request("DELETE", f"/api/feature-requests/{_seg(id)}/vote", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def vote(self, id: str, *, options: Optional[RequestOptions] = None) -> FeatureRequestsVoteResponseData:
        """Adds the caller's vote to a feature request.
        
        A second vote answers 409.
        
        `POST /api/feature-requests/{id}/vote`
        """
        return _pick(self._request("POST", f"/api/feature-requests/{_seg(id)}/vote", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class HelpResource(_Resource):
    """Help
    """

    def get_article(self, id: str, *, options: Optional[RequestOptions] = None) -> HelpArticle:
        """Returns one published help article with its text.
        
        By id only; to find an article by its slug, list with `slug`.
        
        `GET /api/help/articles/{id}`
        """
        return _pick(self._request("GET", f"/api/help/articles/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_articles(self, *, locale: Optional[str] = None, search: Optional[str] = None, category_id: Optional[str] = None, slug: Optional[str] = None, route: Optional[str] = None, options: Optional[RequestOptions] = None) -> HelpListArticlesResponseData:
        """Lists the published help articles of one language, with the help categories.
        
        The list leaves out each article's text; `help.getArticle` returns it. With `search`, the articles are ranked by relevance (full text over title, excerpt, tags and text, at most 20); otherwise by their sort order.
        
        `GET /api/help/articles`
        """
        return _pick(self._request("GET", f"/api/help/articles", query={"locale": locale, "search": search, "categoryId": category_id, "slug": slug, "route": route}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class InvoicingApprovalRulesResource(_Resource):

    def create(self, body: InvoicingApprovalRulesCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Creates a purchase approval rule: the first active rule whose conditions all hold decides who approves, in one or two steps.
        
        Needs `invoicing:settings` and purchase approvals on the plan.
        
        `POST /api/invoicing/purchase-approval-rules` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/purchase-approval-rules", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "rule")  # type: ignore[no-any-return]

    def delete(self, rule_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingApprovalRulesDeleteResponse:
        """Deletes a purchase approval rule.
        
        `DELETE /api/invoicing/purchase-approval-rules/{ruleId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/purchase-approval-rules/{_seg(rule_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the purchase approval rules in their order, and the roles and members a step can name.
        
        Needs `invoicing:settings` and purchase approvals on the plan.
        
        `GET /api/invoicing/purchase-approval-rules` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/purchase-approval-rules", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "rules")  # type: ignore[no-any-return]

    def update(self, rule_id: str, body: InvoicingApprovalRulesUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes a purchase approval rule; invoices already waiting keep their steps.
        
        `PATCH /api/invoicing/purchase-approval-rules/{ruleId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/purchase-approval-rules/{_seg(rule_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "rule")  # type: ignore[no-any-return]


class InvoicingCustomersResource(_Resource):

    def check_vat(self, customer_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingCustomersCheckVatResponse:
        """Checks a customer's stored VAT ID again with VIES / HMRC and stores the answer.
        
        `POST /api/invoicing/customers/{customerId}/vat-check` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/customers/{_seg(customer_id)}/vat-check", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def create(self, body: InvoicingCustomerInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingCustomer:
        """Creates a customer; their VAT ID is checked with VIES / HMRC.
        
        Needs `invoicing:create`. Without a number of its own one is drawn from the customer range. Reverse charge applies only to a validated VAT ID.
        
        `POST /api/invoicing/customers` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/customers", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "customer")  # type: ignore[no-any-return]

    def create_from_crm(self, body: InvoicingCustomersCreateFromCrmBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingCustomer:
        """Creates a customer from a CRM record, linked to it.
        
        Needs `invoicing:create`. `overrides` win over what the record maps to. 409 `invoicingCrmRecordTaken` when the record is a customer already.
        
        `POST /api/invoicing/customers/from-crm` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/customers/from-crm", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "customer")  # type: ignore[no-any-return]

    def delete(self, customer_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingCustomersDeleteResponse:
        """Deletes a customer no document names.
        
        409 `invoicingHasDocuments` otherwise — archive them instead.
        
        `DELETE /api/invoicing/customers/{customerId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/customers/{_seg(customer_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, customer_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingCustomer:
        """One customer, their latest 20 documents and what they owe per currency.
        
        `GET /api/invoicing/customers/{customerId}` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/customers/{_seg(customer_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "customer")  # type: ignore[no-any-return]

    def import_(self, body: Union[InvoicingCustomersImportBody, Dict[str, Any]], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingCustomersImportResponse:
        """Imports customers from a CSV file — a dry run first, then the write.
        
        Needs `invoicing:create`. `options` (JSON): encoding, delimiter, hasHeader, `mapping` (a customer field or null per file column), numberFormat (comma | dot), `duplicate` (match by customerNumber or email, then skip or update; or null), `dryRun`. VAT IDs are stored unchecked. An .xlsx is refused: save the sheet as CSV.
        
        `POST /api/invoicing/customers/import` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/customers/import", query={"organizationId": organization_id}, body=body, multipart=True, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, q: Optional[str] = None, include_archived: Optional[Literal["1"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[InvoicingCustomer]:
        """Lists the customers the caller may see, by name.
        
        `GET /api/invoicing/customers` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/customers", query={"organizationId": organization_id, "q": q, "includeArchived": include_archived, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "customers")  # type: ignore[no-any-return]

    def preview_from_crm(self, *, organization_id: Optional[str] = None, database_id: str, record_id: str, options: Optional[RequestOptions] = None) -> InvoicingCustomersPreviewFromCrmResponse:
        """What a CRM record would become as a customer, and which column fed which field.
        
        The record is read under the CRM's own rules. `existing` is the customer already linked to it.
        
        `GET /api/invoicing/customers/from-crm` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/customers/from-crm", query={"organizationId": organization_id, "databaseId": database_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, customer_id: str, body: InvoicingCustomersUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingCustomer:
        """Changes a customer, or archives and restores them.
        
        Needs `invoicing:create`. A changed VAT ID is checked again. Issued documents keep the customer as they were. Who sees them is changed by their creator or `invoicing:settings` only.
        
        `PATCH /api/invoicing/customers/{customerId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/customers/{_seg(customer_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "customer")  # type: ignore[no-any-return]


class InvoicingDocumentsResource(_Resource):

    def answer_quote(self, document_id: str, body: InvoicingDocumentsAnswerQuoteBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Records the customer's answer to an issued quote: accepted or declined.
        
        Needs `invoicing:finalize`. Only an issued quote that is still open.
        
        `POST /api/invoicing/documents/{documentId}/quote` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/quote", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def bank_lines(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocumentsBankLinesResponse:
        """The bank lines an invoice was paid with, as the Banking hub matched them.
        
        Date and amount always; account, counterpart and purpose only where the caller may read that account's lines.
        
        `GET /api/invoicing/documents/{documentId}/bank` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/documents/{_seg(document_id)}/bank", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def check_einvoice(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocumentsCheckEinvoiceResponse:
        """Checks a draft's e-invoice with the KoSIT validator, written with the number it would get — nothing is drawn.
        
        Needs `invoicing:create` and e-invoicing on the plan. The verdict is written to the document's history. `report` is null when the draft is not an e-invoice.
        
        `POST /api/invoicing/documents/{documentId}/einvoice-check` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/einvoice-check", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def convert(self, document_id: str, body: InvoicingDocumentsConvertBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Makes a new draft from an issued document: an order confirmation or invoice from a quote, a partial or final invoice, a credit note or cancellation of an invoice.
        
        Needs `invoicing:create` (a credit note or cancellation: `invoicing:cancel`).
        
        - quote → order_confirmation | invoice
        - order_confirmation → invoice | delivery_note
        - quote / order confirmation → invoice with `invoiceKind`: `partial` (`percent` of the gross or `amountCents`) or `final` (every line, the issued partial invoices deducted)
        - invoice → credit_note (all lines, chosen `lines` with smaller quantities, or a gross `amountCents`) | cancellation
        
        409 `invoicingIsDraft` (finalize the source first), 409 `invoicingInvalidTransition`, 422 `invoicingOverCredit` / `invoicingPartialExceeds`.
        
        `POST /api/invoicing/documents/{documentId}/convert` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/convert", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def create(self, body: InvoicingDraftInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Creates a draft — for a customer, from catalogue products and lines.
        
        Needs `invoicing:create`. The customer gives the language, currency, terms and discount; the template the texts. An invoice without a service date gets the document date. Credit notes and cancellations are made from their invoice (convert).
        
        `POST /api/invoicing/documents` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/documents", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def delete(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocumentsDeleteResponse:
        """Moves a draft to the trash.
        
        Needs `invoicing:create`. A finalized document is never deleted (409 `invoicingFinalized`, §147 AO).
        
        `DELETE /api/invoicing/documents/{documentId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/documents/{_seg(document_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def duplicate(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Makes a new draft of the same type with the same customer, lines and texts.
        
        Needs `invoicing:create`. No number, payments or links are copied. A credit note or cancellation is refused: it is made from its invoice.
        
        `POST /api/invoicing/documents/{documentId}/duplicate` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/duplicate", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def export(self, *, organization_id: Optional[str] = None, type_: Optional[str] = None, status: Optional[str] = None, payment_status: Optional[str] = None, customer_id: Optional[str] = None, issuer_id: Optional[str] = None, chain_id: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, q: Optional[str] = None, visibility: Optional[str] = None, mine: Optional[Literal["1"]] = None, kind: Optional[Literal["dunning"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads documents as a CSV file, filtered like the list — or, with `kind=dunning`, the dunning notices sent.
        
        Needs `invoicing:export`. Every document of the organisation, whoever may see it in the hub: the books are always complete. At most 10,000 rows.
        
        `GET /api/invoicing/documents/export` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/documents/export", query={"organizationId": organization_id, "type": type_, "status": status, "paymentStatus": payment_status, "customerId": customer_id, "issuerId": issuer_id, "chainId": chain_id, "from": from_, "to": to, "q": q, "visibility": visibility, "mine": mine, "kind": kind}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def finalize(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Issues a draft: its number is drawn, it is frozen and its PDF archived.
        
        Needs `invoicing:finalize` (a credit note or cancellation: `invoicing:cancel`). From then on the document can never be changed or deleted. Refusals: 422 `invoicingIncomplete` with `issues` (what §14 UStG still misses), 422 `invoicingOverCredit`, 409 `invoicingNotDraft` / `invoicingAlreadyCancelled` / `invoicingNumberTaken`. An e-invoice needs e-invoicing on the plan and passes the KoSIT validator (422 `invoicingEinvoiceInvalid` with `report`; the draft keeps no number). The plan's monthly document limit counts every type but credit notes and cancellations.
        
        `POST /api/invoicing/documents/{documentId}/finalize` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/finalize", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def get(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocumentsGetResponse:
        """One document with its lines, history, payments, the documents of its deal and its e-invoice.
        
        `GET /api/invoicing/documents/{documentId}` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/documents/{_seg(document_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, type_: Optional[str] = None, status: Optional[str] = None, payment_status: Optional[str] = None, customer_id: Optional[str] = None, issuer_id: Optional[str] = None, chain_id: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, q: Optional[str] = None, visibility: Optional[str] = None, mine: Optional[Literal["1"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[InvoicingDocument]:
        """Lists one page of the documents the caller may see, newest first with drafts on top, with totals per currency.
        
        Needs `invoicing:read`.
        
        `GET /api/invoicing/documents` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/documents", query={"organizationId": organization_id, "type": type_, "status": status, "paymentStatus": payment_status, "customerId": customer_id, "issuerId": issuer_id, "chainId": chain_id, "from": from_, "to": to, "q": q, "visibility": visibility, "mine": mine, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "documents")  # type: ignore[no-any-return]

    def mark_sent(self, document_id: str, body: InvoicingDocumentsMarkSentBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Records that an issued document went out another way: handed over, printed, mailed from elsewhere.
        
        Needs `invoicing:finalize`.
        
        `POST /api/invoicing/documents/{documentId}/sent` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/sent", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def pdf(self, document_id: str, *, organization_id: Optional[str] = None, download: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a document's PDF: an issued one as archived, a draft rendered now and stamped as a draft.
        
        The header `X-Content-SHA256` carries an issued document's stored hash. 502 `invoicingPdfFailed` when the renderer does not answer.
        
        `GET /api/invoicing/documents/{documentId}/pdf` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/documents/{_seg(document_id)}/pdf", query={"organizationId": organization_id, "download": download}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def send(self, document_id: str, body: InvoicingDocumentsSendBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocumentsSendResponse:
        """Sends an issued document by e-mail with its PDF (and an XRechnung's XML).
        
        Needs `invoicing:finalize`. From the Mail hub mailbox `accountId` (the Mail hub's rules apply), else from the platform's sender with Reply-To the issuer. Records the sending. 409 `invoicingIsDraft`, 422 `invoicingNoRecipient`, 502 `invoicingPdfFailed` / `invoicingSendFailed`.
        
        `POST /api/invoicing/documents/{documentId}/send` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/send", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def send_defaults(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocumentsSendDefaultsResponse:
        """What sending a document by e-mail starts from: the recipients, the subject, and the mailboxes the caller may send from.
        
        Needs `invoicing:finalize`. No mailboxes: the platform's sender is used.
        
        `GET /api/invoicing/documents/{documentId}/send` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/documents/{_seg(document_id)}/send", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, document_id: str, body: InvoicingDraftPatch, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Changes a draft; totals, tax and legal notes are computed again.
        
        Needs `invoicing:create`. A finalized document is refused (409 `invoicingNotDraft`) — except `visibility` / `workspaceId` alone, which change at any status (its creator or `invoicing:settings`).
        
        `PATCH /api/invoicing/documents/{documentId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/documents/{_seg(document_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def xml(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads an issued e-invoice's XML exactly as archived at finalize.
        
        XRechnung UBL / CII, or the factur-x.xml of a ZUGFeRD PDF; checked against its stored hash (`X-Content-SHA256`). 404 `invoicingEinvoiceNotIssued` for a draft or a document without an e-invoice.
        
        `GET /api/invoicing/documents/{documentId}/xml` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/documents/{_seg(document_id)}/xml", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class InvoicingDunningResource(_Resource):

    def get_notice(self, notice_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """One dunning notice.
        
        `GET /api/invoicing/dunning/notices/{noticeId}` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/dunning/notices/{_seg(notice_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "notice")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InvoicingDunningListResponseItemsItem]:
        """The proposed dunning notices waiting for review, oldest first, with their invoices.
        
        Needs the plan's dunning feature.
        
        `GET /api/invoicing/dunning` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/dunning", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "items")  # type: ignore[no-any-return]

    def notice_pdf(self, notice_id: str, *, organization_id: Optional[str] = None, download: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a dunning notice as PDF: a sent one as archived, a proposed one as a preview.
        
        `GET /api/invoicing/dunning/notices/{noticeId}/pdf` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/dunning/notices/{_seg(notice_id)}/pdf", query={"organizationId": organization_id, "download": download}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def pause_customer(self, customer_id: str, body: InvoicingDunningPauseCustomerBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> bool:
        """Excludes a customer from dunning, or includes them again.
        
        Needs `invoicing:payments` and the plan's dunning feature. While paused no notice is proposed for their invoices and waiting proposals are dropped.
        
        `PATCH /api/invoicing/customers/{customerId}/dunning` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/customers/{_seg(customer_id)}/dunning", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "paused")  # type: ignore[no-any-return]

    def pause_document(self, document_id: str, body: InvoicingDunningPauseDocumentBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Pauses or resumes the dunning of an invoice; pausing drops a waiting proposal.
        
        Needs `invoicing:payments` and the plan's dunning feature.
        
        `PATCH /api/invoicing/documents/{documentId}/dunning` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/documents/{_seg(document_id)}/dunning", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def propose(self, document_id: str, body: InvoicingDunningProposeBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Proposes a dunning notice for an invoice now: the next level, or a chosen one above every level sent.
        
        Needs `invoicing:payments` and the plan's dunning feature. 409 `invoicingDunningNotDunnable` with `reason` (paid, cancelled, not due, paused, last level sent); 409 `invoicingDunningWaiting` when one waits for review already.
        
        `POST /api/invoicing/documents/{documentId}/dunning` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/dunning", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "notice")  # type: ignore[no-any-return]

    def remove_notice(self, notice_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDunningRemoveNoticeResponse:
        """Removes a proposed dunning notice; a sent one is a record and stays.
        
        Needs `invoicing:payments` and the plan's dunning feature. 409 `invoicingDunningNoticeSent`.
        
        `DELETE /api/invoicing/dunning/notices/{noticeId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/dunning/notices/{_seg(notice_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def send_defaults(self, notice_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDunningSendDefaultsResponse:
        """What sending a dunning notice starts from: the recipients, the subject, the mailboxes the caller may send from.
        
        `GET /api/invoicing/dunning/notices/{noticeId}/send` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/dunning/notices/{_seg(notice_id)}/send", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def send_notice(self, notice_id: str, body: InvoicingDunningSendNoticeBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Sends a proposed dunning notice by e-mail, or records that it went out on paper.
        
        Needs `invoicing:payments` and the plan's dunning feature. Its amounts are brought to today and its PDF archived; then it never changes.
        
        `POST /api/invoicing/dunning/notices/{noticeId}/send` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/dunning/notices/{_seg(notice_id)}/send", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "notice")  # type: ignore[no-any-return]

    def state(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDunningStateResponse:
        """An invoice's dunning: the levels, the notices so far, the next level and when it is due, and what a notice would claim today.
        
        `state` is null for anything but an issued invoice.
        
        `GET /api/invoicing/documents/{documentId}/dunning` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/documents/{_seg(document_id)}/dunning", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class InvoicingInboundMailboxesResource(_Resource):

    def add(self, body: InvoicingInboundMailboxesAddBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Receives supplier invoices from a Mail hub mailbox, automatically or by hand.
        
        Needs `invoicing:settings`, signed in as somebody who may open the mailbox in the Mail hub (an API token never reads mail). `backfillDays` (automatic only): a one-time import of the last N days.
        
        `POST /api/invoicing/inbound/mailboxes` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/inbound/mailboxes", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "mailbox")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The Mail hub mailboxes the organisation receives supplier invoices from, and what the newest mails came to.
        
        `GET /api/invoicing/inbound/mailboxes` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/inbound/mailboxes", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "mailboxes")  # type: ignore[no-any-return]

    def remove(self, mailbox_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingInboundMailboxesRemoveResponse:
        """Stops receiving from a mailbox; documents already taken stay.
        
        `DELETE /api/invoicing/inbound/mailboxes/{mailboxId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/inbound/mailboxes/{_seg(mailbox_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, mailbox_id: str, body: InvoicingInboundMailboxesUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Switches a receiving mailbox between automatic and manual.
        
        Needs `invoicing:settings`. To automatic only for somebody signed in who may open the mailbox.
        
        `PATCH /api/invoicing/inbound/mailboxes/{mailboxId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/inbound/mailboxes/{_seg(mailbox_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "mailbox")  # type: ignore[no-any-return]


class InvoicingInboundResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.mailboxes = InvoicingInboundMailboxesResource(request)

    def delete(self, inbound_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingInboundDeleteResponse:
        """Deletes a rejected received document, or one that could not be read as an e-invoice, with its original.
        
        409 `invoicingInboundNotDeletable` otherwise: an approved or booked one is kept. Its uploader or `invoicing:payments`.
        
        `DELETE /api/invoicing/inbound/{inboundId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/inbound/{_seg(inbound_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, inbound_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingInboundGetResponse:
        """One received e-invoice with its EN 16931 data, validation report, history and duplicates.
        
        `GET /api/invoicing/inbound/{inboundId}` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/inbound/{_seg(inbound_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, status: Optional[str] = None, validation: Optional[str] = None, format: Optional[str] = None, source: Optional[str] = None, supplier: Optional[str] = None, q: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, duplicates: Optional[Literal["1"]] = None, open: Optional[Literal["1"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the received e-invoices the caller may see, newest first, with totals per currency.
        
        Needs receiving invoices on the plan.
        
        `GET /api/invoicing/inbound` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/inbound", query={"organizationId": organization_id, "status": status, "validation": validation, "format": format, "source": source, "supplier": supplier, "q": q, "from": from_, "to": to, "duplicates": duplicates, "open": open, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "documents")  # type: ignore[no-any-return]

    def original(self, inbound_id: str, *, organization_id: Optional[str] = None, download: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a received document exactly as it arrived.
        
        Checked against the hash stored on arrival (`X-Content-SHA256`). XML always as an attachment; a PDF inline unless `download=1`.
        
        `GET /api/invoicing/inbound/{inboundId}/original` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/inbound/{_seg(inbound_id)}/original", query={"organizationId": organization_id, "download": download}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def revalidate(self, inbound_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Validates a received e-invoice's stored original again with the KoSIT validator.
        
        Needs `invoicing:create`. For when the validator was not reachable on arrival or its rules were updated; only the XML read out of the original is validated. 503 `invoicingInboundValidatorUnavailable` (with the unchanged `document`) when it still does not answer — the earlier verdict stays. 409 `invoicingInboundNotValidatable` for a file without XML. 10 a minute.
        
        `POST /api/invoicing/inbound/{inboundId}/revalidate` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/inbound/{_seg(inbound_id)}/revalidate", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def transition(self, inbound_id: str, body: InvoicingInboundTransitionBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Checks, approves, books, rejects or reopens a received e-invoice.
        
        Needs `invoicing:payments`. check: received → checked; approve: → approved; book: approved → booked; reject (with a `note`): → rejected; reopen: rejected → received. Anything else: 409 `invoicingInboundInvalidTransition`.
        
        `POST /api/invoicing/inbound/{inboundId}/status` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/inbound/{_seg(inbound_id)}/status", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def update(self, inbound_id: str, body: InvoicingInboundUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes who sees a received e-invoice.
        
        Its uploader or `invoicing:settings`.
        
        `PATCH /api/invoicing/inbound/{inboundId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/inbound/{_seg(inbound_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "document")  # type: ignore[no-any-return]

    def upload(self, body: Union[InvoicingInboundUploadBody, Dict[str, Any]], *, organization_id: Optional[str] = None, filename: Optional[str] = None, visibility: Optional[Literal["private", "workspace", "organization"]] = None, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InvoicingInboundUploadResponseResultsItem]:
        """Receives supplier e-invoices: XRechnung, ZUGFeRD / Factur-X or a plain PDF.
        
        Needs `invoicing:create` and receiving invoices on the plan. Multipart with one or more `files` (or `file`), optional `visibility` and `workspaceId`; an API client may also send the raw file as the body (application/xml or application/pdf) with its name in `X-Filename` or `?filename=`. At most 20 files of 20 MB. Every file is stored unchangeable with its SHA-256, read, validated and flagged when it repeats an earlier one; nothing is refused for its content. 422 `invoicingInboundNotStored` when none was stored. 30 a minute.
        
        `POST /api/invoicing/inbound` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/inbound", query={"organizationId": organization_id, "filename": filename, "visibility": visibility, "workspaceId": workspace_id}, body=body, multipart=True, options=options), "results")  # type: ignore[no-any-return]


class InvoicingIssuersResource(_Resource):

    def create(self, body: InvoicingIssuerInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingIssuer:
        """Creates an issuing company with a number range for every document type.
        
        Needs `invoicing:settings`. A second active company needs multiple companies on the plan and counts against its limit.
        
        `POST /api/invoicing/issuers` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/issuers", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "issuer")  # type: ignore[no-any-return]

    def delete(self, issuer_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingIssuersDeleteResponse:
        """Deletes an issuing company that never issued anything.
        
        Needs `invoicing:settings`. 409 `invoicingHasDocuments` otherwise — archive it instead.
        
        `DELETE /api/invoicing/issuers/{issuerId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/issuers/{_seg(issuer_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, issuer_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingIssuer:
        """One issuing company with its number ranges.
        
        `GET /api/invoicing/issuers/{issuerId}` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/issuers/{_seg(issuer_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "issuer")  # type: ignore[no-any-return]

    def get_dunning_settings(self, issuer_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingIssuersGetDunningSettingsResponse:
        """A company's dunning settings: the levels, their built-in texts, and the base rate for default interest.
        
        `GET /api/invoicing/issuers/{issuerId}/dunning` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/issuers/{_seg(issuer_id)}/dunning", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, include_archived: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> List[InvoicingIssuer]:
        """Lists the organisation's issuing companies, the default first.
        
        `GET /api/invoicing/issuers` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/issuers", query={"organizationId": organization_id, "includeArchived": include_archived}, body=None, multipart=False, options=options), "issuers")  # type: ignore[no-any-return]

    def set_dunning_settings(self, issuer_id: str, body: InvoicingIssuersSetDunningSettingsBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Replaces a company's dunning settings.
        
        Needs `invoicing:settings` and the plan's dunning feature. Checked strictly: 400 `invoicingDunningSettingsInvalid` with `field`, 400 `invoicingUnknownMergeField`.
        
        `PUT /api/invoicing/issuers/{issuerId}/dunning` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PUT", f"/api/invoicing/issuers/{_seg(issuer_id)}/dunning", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def update(self, issuer_id: str, body: InvoicingIssuersUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingIssuer:
        """Changes an issuing company, or archives and restores it.
        
        Needs `invoicing:settings`. Restoring counts as one more active company.
        
        `PATCH /api/invoicing/issuers/{issuerId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/issuers/{_seg(issuer_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "issuer")  # type: ignore[no-any-return]


class InvoicingLedgerAccountsResource(_Resource):

    def create(self, body: InvoicingLedgerAccountsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Adds a general-ledger account inside the chart's range for its kind.
        
        Needs `invoicing:bookkeeping` and the ledger on the plan. 422 `invoicingLedgerAccountOutOfRange`, 409 `invoicingLedgerAccountNumberTaken`.
        
        `POST /api/invoicing/ledger/accounts` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/ledger/accounts", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "account")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, q: Optional[str] = None, kind: Optional[Literal["asset", "liability", "equity", "revenue", "expense", "debtor", "creditor"]] = None, personal: Optional[Literal["1"]] = None, inactive: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """A company's chart of accounts.
        
        Needs `invoicing:export` or `invoicing:bookkeeping`.
        
        `GET /api/invoicing/ledger/accounts` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/ledger/accounts", query={"organizationId": organization_id, "issuerId": issuer_id, "q": q, "kind": kind, "personal": personal, "inactive": inactive}, body=None, multipart=False, options=options), "accounts")  # type: ignore[no-any-return]

    def update(self, account_id: str, body: InvoicingLedgerAccountsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Renames an account, (de)activates it, or changes its default tax code or EÜR line.
        
        Needs `invoicing:bookkeeping` and the ledger on the plan. System accounts stay active.
        
        `PATCH /api/invoicing/ledger/accounts/{accountId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/ledger/accounts/{_seg(account_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "account")  # type: ignore[no-any-return]


class InvoicingLedgerDatevResource(_Resource):

    def export(self, body: InvoicingLedgerDatevExportBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a DATEV export: the booking batch (EXTF), the customer and supplier master data, or a ZIP with both and the documents' PDFs.
        
        Needs `invoicing:export` and DATEV on the plan, and the adviser and client number in the books' settings. A range inside one fiscal year. Every export is recorded.
        
        `POST /api/invoicing/ledger/datev` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/ledger/datev", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The DATEV exports made so far.
        
        `GET /api/invoicing/ledger/datev` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/ledger/datev", query={"organizationId": organization_id, "issuerId": issuer_id}, body=None, multipart=False, options=options), "exports")  # type: ignore[no-any-return]


class InvoicingLedgerEntriesResource(_Resource):

    def list(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, account: Optional[str] = None, q: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The journal, newest first: every entry with its lines and what reversed it.
        
        Needs `invoicing:export` or `invoicing:bookkeeping`. The books complete.
        
        `GET /api/invoicing/ledger/entries` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/ledger/entries", query={"organizationId": organization_id, "issuerId": issuer_id, "from": from_, "to": to, "account": account, "q": q, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "entries")  # type: ignore[no-any-return]

    def post(self, body: InvoicingLedgerEntriesPostBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Posts a manual journal entry: balanced, on the chart, in an open month.
        
        Needs `invoicing:bookkeeping` and the ledger on the plan. With `clientKey`, sending it again answers the entry already posted.
        
        `POST /api/invoicing/ledger/entries` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/ledger/entries", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "entry")  # type: ignore[no-any-return]

    def reverse(self, entry_id: str, body: InvoicingLedgerEntriesReverseBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Reverses a manual entry or opening balance (Storno): the same lines with the sides swapped, once.
        
        Needs `invoicing:bookkeeping`. An automatic entry follows its document (409 `invoicingLedgerAutoEntry`): correct the document instead.
        
        `POST /api/invoicing/ledger/entries/{entryId}/reverse` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/ledger/entries/{_seg(entry_id)}/reverse", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "entry")  # type: ignore[no-any-return]


class InvoicingLedgerPeriodsResource(_Resource):

    def list(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, fiscal_year: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The months of a fiscal year: closed or open, and exported to DATEV.
        
        `GET /api/invoicing/ledger/periods` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/ledger/periods", query={"organizationId": organization_id, "issuerId": issuer_id, "fiscalYear": fiscal_year}, body=None, multipart=False, options=options), "periods")  # type: ignore[no-any-return]

    def set(self, body: InvoicingLedgerPeriodsSetBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingLedgerPeriodsSetResponse:
        """Closes a month (nothing can be posted in it any more) or reopens it.
        
        Needs `invoicing:bookkeeping`. Reopening a month a DATEV export covered asks first (409 `invoicingLedgerPeriodExported`) until `confirmExported`. Closing answers `warnings` for mapped bank accounts that do not reconcile.
        
        `POST /api/invoicing/ledger/periods` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/ledger/periods", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class InvoicingLedgerSettingsResource(_Resource):

    def create(self, body: InvoicingLedgerSettingsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Switches a company's books on, with an SKR03 or SKR04 chart.
        
        Needs `invoicing:bookkeeping` and the ledger or EÜR on the plan. 409 `invoicingLedgerBooksAlreadyOn`.
        
        `POST /api/invoicing/ledger/settings` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/ledger/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def get(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """A company's books: chart, method, VAT mode, fiscal year; null when it keeps none.
        
        `GET /api/invoicing/ledger/settings` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/ledger/settings", query={"organizationId": organization_id, "issuerId": issuer_id}, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def update(self, body: InvoicingLedgerSettingsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes a company's books; the chart, first booking date and fiscal year start only until the first posting.
        
        `PATCH /api/invoicing/ledger/settings` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/ledger/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class InvoicingLedgerYearEndResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, fiscal_year: Optional[int] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """What closing a fiscal year would do, or did: the result, the carried-forward balances, whether it can be closed.
        
        `GET /api/invoicing/ledger/year-end` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/ledger/year-end", query={"organizationId": organization_id, "issuerId": issuer_id, "fiscalYear": fiscal_year}, body=None, multipart=False, options=options), "yearEnd")  # type: ignore[no-any-return]

    def set(self, body: InvoicingLedgerYearEndSetBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Closes a fiscal year with its closing entries, or reopens it.
        
        Needs `invoicing:bookkeeping` and the ledger on the plan. Balance method only, every month closed.
        
        `POST /api/invoicing/ledger/year-end` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/ledger/year-end", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "yearEnd")  # type: ignore[no-any-return]


class InvoicingLedgerResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.accounts = InvoicingLedgerAccountsResource(request)
        self.datev = InvoicingLedgerDatevResource(request)
        self.entries = InvoicingLedgerEntriesResource(request)
        self.periods = InvoicingLedgerPeriodsResource(request)
        self.settings = InvoicingLedgerSettingsResource(request)
        self.year_end = InvoicingLedgerYearEndResource(request)

    def events(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The books' own history: set up, settings changed, months closed and reopened, accounts changed, DATEV exports.
        
        `GET /api/invoicing/ledger/events` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/ledger/events", query={"organizationId": organization_id, "issuerId": issuer_id, "limit": limit}, body=None, multipart=False, options=options), "events")  # type: ignore[no-any-return]

    def opening(self, body: InvoicingLedgerOpeningBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Posts opening balances at the first booking date, each against the carried-forward account.
        
        Needs `invoicing:bookkeeping` and the ledger on the plan.
        
        `POST /api/invoicing/ledger/opening` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/ledger/opening", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "entry")  # type: ignore[no-any-return]

    def report(self, kind: str, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, fiscal_year: Optional[int] = None, period: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, account: Optional[str] = None, side: Optional[str] = None, format: Optional[Literal["json", "csv", "pdf"]] = None, lang: Optional[Literal["de", "en", "es", "fr"]] = None, options: Optional[RequestOptions] = None) -> InvoicingLedgerReportResponse:
        """One report of the books: EÜR, VAT return (UStVA), trial balance, account sheet, P&L, balance sheet or open items.
        
        Needs `invoicing:export` or `invoicing:bookkeeping`. JSON with the figures and a ready table; `format=csv` or `pdf` downloads it. The books complete.
        
        `GET /api/invoicing/ledger/reports/{kind}` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/ledger/reports/{_seg(kind)}", query={"organizationId": organization_id, "issuerId": issuer_id, "fiscalYear": fiscal_year, "period": period, "from": from_, "to": to, "account": account, "side": side, "format": format, "lang": lang}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def start(self, body: InvoicingLedgerStartBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingLedgerStartResponse:
        """Starts a company's books: posts its history from the first booking date, once.
        
        Needs `invoicing:bookkeeping`. Small books run at once; larger ones are queued (`status: queued`). A second run posts only what is missing.
        
        `POST /api/invoicing/ledger/start` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/ledger/start", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class InvoicingNumberRangesResource(_Resource):

    def list(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InvoicingNumberRange]:
        """Lists the number ranges — one per company and document type, and the customer-number range — with the next number each would draw.
        
        `GET /api/invoicing/number-ranges` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/number-ranges", query={"organizationId": organization_id, "issuerId": issuer_id}, body=None, multipart=False, options=options), "ranges")  # type: ignore[no-any-return]

    def preview(self, body: InvoicingNumberRangesPreviewBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingNumberRangesPreviewResponse:
        """What a number pattern would produce; nothing is drawn or stored.
        
        `POST /api/invoicing/number-ranges/preview` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/number-ranges/preview", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, range_id: str, body: InvoicingNumberRangesUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingNumberRange:
        """Changes a number range's format, until a number was drawn from it.
        
        Needs `invoicing:settings`. 409 `invoicingRangeLocked` once a number was drawn; 422 `invoicingInvalidPattern` with `issues`.
        
        `PATCH /api/invoicing/number-ranges/{rangeId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/number-ranges/{_seg(range_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "range")  # type: ignore[no-any-return]


class InvoicingPaymentRunsResource(_Resource):

    def close(self, run_id: str, body: InvoicingPaymentRunsCloseBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Confirms that the bank executed a payment run (each item becomes a payment), or cancels it.
        
        Needs `invoicing:payments`. 409 `invoicingPaymentRunClosed` once confirmed or cancelled.
        
        `POST /api/invoicing/payment-runs/{runId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/payment-runs/{_seg(run_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "run")  # type: ignore[no-any-return]

    def create(self, body: InvoicingPaymentRunsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Creates a SEPA payment run: a credit transfer file (pain.001) paying purchase invoices, to upload to online banking.
        
        Needs `invoicing:payments`. Approved or booked invoices of that company with money owed, in EUR, with a payee IBAN, in no other open run; from one of the company's bank accounts; on a date not in the past. 409 `invoicingPaymentRunNotPayable` with `refused`. Nothing is sent to a bank.
        
        `POST /api/invoicing/payment-runs` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/payment-runs", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "run")  # type: ignore[no-any-return]

    def file(self, run_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a payment run's pain.001.001.09 XML exactly as written.
        
        `GET /api/invoicing/payment-runs/{runId}/file` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/payment-runs/{_seg(run_id)}/file", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, run_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """One SEPA payment run with its items.
        
        `GET /api/invoicing/payment-runs/{runId}` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/payment-runs/{_seg(run_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "run")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the SEPA payment runs, newest first.
        
        `GET /api/invoicing/payment-runs` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/payment-runs", query={"organizationId": organization_id, "limit": limit}, body=None, multipart=False, options=options), "runs")  # type: ignore[no-any-return]


class InvoicingPaymentsResource(_Resource):

    def list(self, document_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InvoicingPayment]:
        """The payments recorded on an invoice, oldest first.
        
        `GET /api/invoicing/documents/{documentId}/payments` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/documents/{_seg(document_id)}/payments", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "payments")  # type: ignore[no-any-return]

    def record(self, document_id: str, body: InvoicingPaymentsRecordBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingPayment:
        """Records a payment on an issued invoice, or a refund paid back (negative).
        
        Needs `invoicing:payments`. The payment status follows (open → partially_paid → paid). 409 `invoicingNotPayable` for anything but an issued invoice.
        
        `POST /api/invoicing/documents/{documentId}/payments` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/documents/{_seg(document_id)}/payments", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "payment")  # type: ignore[no-any-return]

    def remove(self, document_id: str, payment_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingDocument:
        """Removes a payment recorded by mistake; the payment status is computed again.
        
        Needs `invoicing:payments`.
        
        `DELETE /api/invoicing/documents/{documentId}/payments/{paymentId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("DELETE", f"/api/invoicing/documents/{_seg(document_id)}/payments/{_seg(payment_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "document")  # type: ignore[no-any-return]


class InvoicingPurchasesResource(_Resource):

    def ai_fill(self, purchase_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingPurchaseAiSuggestion:
        """Has the platform AI read a draft purchase invoice's original receipt and suggest supplier, numbers, dates, amounts, rate and IBAN.
        
        Needs `invoicing:create` and the plan's AI for invoicing. The suggestion is kept on the draft beside its fields; nothing is filled in or booked by it. 503 `invoicingPurchaseAiUnavailable` without platform AI; 429 when the organisation's AI quota is used up; 422 `invoicingPurchaseAiUnreadable` with `reason` (`heicNotReadable`, `noTextLayer`, `noOriginal`). 10 a minute.
        
        `POST /api/invoicing/purchases/{purchaseId}/ai-fill` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/purchases/{_seg(purchase_id)}/ai-fill", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "suggestion")  # type: ignore[no-any-return]

    def attach_original(self, purchase_id: str, body: Union[InvoicingPurchasesAttachOriginalBody, Dict[str, Any]], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Attaches the original to a purchase invoice that has none; written once.
        
        Needs `invoicing:create`. PDF, JPEG, PNG or HEIC, 20 MB at most. 409 `invoicingPurchaseOriginalExists`.
        
        `POST /api/invoicing/purchases/{purchaseId}/original` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/purchases/{_seg(purchase_id)}/original", query={"organizationId": organization_id}, body=body, multipart=True, options=options), "purchase")  # type: ignore[no-any-return]

    def bank_lines(self, purchase_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InvoicingBankLine]:
        """The bank lines a purchase invoice was paid with, as the Banking hub matched them.
        
        Needs `invoicing:read`. Date and amount always; account, counterpart and purpose only where the caller may read that account's lines. `banking` is false when the caller has no Banking hub.
        
        `GET /api/invoicing/purchases/{purchaseId}/bank` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/purchases/{_seg(purchase_id)}/bank", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "lines")  # type: ignore[no-any-return]

    def create(self, body: InvoicingPurchaseInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Enters a purchase invoice by hand, as a draft.
        
        Needs `invoicing:create` and purchases on the plan. The due date follows the supplier's payment terms, the payee IBAN the supplier. A receipt can be uploaded instead as multipart: `file` (PDF, JPEG, PNG or HEIC, 20 MB at most) and optional `data` (this JSON). 30 a minute.
        
        `POST /api/invoicing/purchases` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/purchases", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "purchase")  # type: ignore[no-any-return]

    def delete(self, purchase_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingPurchasesDeleteResponse:
        """Deletes a draft purchase invoice.
        
        409 `invoicingPurchaseKept` once approved or booked.
        
        `DELETE /api/invoicing/purchases/{purchaseId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/purchases/{_seg(purchase_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_payment(self, purchase_id: str, payment_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Removes a payment recorded on a purchase invoice by mistake; a posted one is reversed in the journal.
        
        Needs `invoicing:payments`.
        
        `DELETE /api/invoicing/purchases/{purchaseId}/payments/{paymentId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("DELETE", f"/api/invoicing/purchases/{_seg(purchase_id)}/payments/{_seg(payment_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "purchase")  # type: ignore[no-any-return]

    def from_inbound(self, body: InvoicingPurchasesFromInboundBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Makes a purchase invoice from a received e-invoice: the supplier matched or created, the lines with their tax.
        
        Needs `invoicing:create`. One per received document (409 `invoicingPurchaseExists`); 422 `invoicingPurchaseNotEinvoice` for a file that is not an e-invoice.
        
        `POST /api/invoicing/purchases/from-inbound` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/purchases/from-inbound", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "purchase")  # type: ignore[no-any-return]

    def from_inbound_status(self, *, organization_id: Optional[str] = None, inbound_id: str, options: Optional[RequestOptions] = None) -> InvoicingPurchasesFromInboundStatusResponse:
        """The purchase invoice made from a received e-invoice, if any.
        
        `purchase` is null when there is none or the caller may not see it; `exists` says which.
        
        `GET /api/invoicing/purchases/from-inbound` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/purchases/from-inbound", query={"organizationId": organization_id, "inboundId": inbound_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, purchase_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingPurchasesGetResponse:
        """One purchase invoice with its lines, payments, history, supplier, approval and original.
        
        `GET /api/invoicing/purchases/{purchaseId}` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/purchases/{_seg(purchase_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, status: Optional[str] = None, payment: Optional[str] = None, approval: Optional[str] = None, source: Optional[str] = None, supplier_id: Optional[str] = None, issuer_id: Optional[str] = None, q: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, open: Optional[Literal["1"]] = None, in_run: Optional[Literal["0", "1"]] = None, mine: Optional[Literal["1"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the purchase invoices the caller may see, newest first, with totals and what waits for approval, is overdue or is to be paid.
        
        Needs purchases on the plan.
        
        `GET /api/invoicing/purchases` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/purchases", query={"organizationId": organization_id, "status": status, "payment": payment, "approval": approval, "source": source, "supplierId": supplier_id, "issuerId": issuer_id, "q": q, "from": from_, "to": to, "open": open, "inRun": in_run, "mine": mine, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "purchases")  # type: ignore[no-any-return]

    def options_(self, *, organization_id: Optional[str] = None, issuer_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingPurchasesOptionsResponse:
        """What a purchase invoice's lines can be booked to: the issuing companies with their bank accounts, and for one company its chart's expense and asset accounts — or, with its books off, the categories already used.
        
        Needs `invoicing:read`. Without `issuerId`, the default company. `taxCodes` is the fixed list a line's `taxCode` takes.
        
        `GET /api/invoicing/purchases/options` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/purchases/options", query={"organizationId": organization_id, "issuerId": issuer_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def original(self, purchase_id: str, *, organization_id: Optional[str] = None, download: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a purchase invoice's original as stored: the uploaded receipt or the received e-invoice.
        
        `GET /api/invoicing/purchases/{purchaseId}/original` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/purchases/{_seg(purchase_id)}/original", query={"organizationId": organization_id, "download": download}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def record_payment(self, purchase_id: str, body: InvoicingPurchasesRecordPaymentBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Records a payment on an approved or booked purchase invoice — by default what is open, today, by bank transfer.
        
        Needs `invoicing:payments`. More than is open: 422 `invoicingPurchaseExceedsOpen`.
        
        `POST /api/invoicing/purchases/{purchaseId}/payments` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/purchases/{_seg(purchase_id)}/payments", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "payment")  # type: ignore[no-any-return]

    def transition(self, purchase_id: str, body: InvoicingPurchasesTransitionBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Submits a purchase invoice for approval, approves or rejects it, reopens it, or books it.
        
        submit (`invoicing:create`): the approval steps are worked out and the approvers told. approve / reject (with a `note`): the step's approver; who decided step 1 does not decide step 2. reopen (`invoicing:payments`): approved → draft. book (`invoicing:payments`): approved → booked, posted to the ledger when the books are on. 422 `invoicingPurchaseIncomplete` with `issues`; 409 `invoicingPurchaseInvalidTransition`.
        
        `POST /api/invoicing/purchases/{purchaseId}/status` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/purchases/{_seg(purchase_id)}/status", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "purchase")  # type: ignore[no-any-return]

    def update(self, purchase_id: str, body: InvoicingPurchaseInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes a draft purchase invoice; `lines` replace them all.
        
        Needs `invoicing:create`. 409 `invoicingPurchaseNotDraft` once approved or booked — except `visibility` / `workspaceId` alone. A waiting approval is withdrawn.
        
        `PATCH /api/invoicing/purchases/{purchaseId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/purchases/{_seg(purchase_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "purchase")  # type: ignore[no-any-return]


class InvoicingRecurringResource(_Resource):

    def create(self, body: InvoicingRecurringCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Creates a recurring invoice: an invoice repeated on a schedule, as a draft, finalized, or finalized and sent.
        
        Needs `invoicing:create` and recurring invoices on the plan; the modes `finalize` and `finalize_send` need `invoicing:finalize`.
        
        `POST /api/invoicing/recurring` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/recurring", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "profile")  # type: ignore[no-any-return]

    def delete(self, profile_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingRecurringDeleteResponse:
        """Deletes a recurring invoice and its run history; the invoices it made stay.
        
        `DELETE /api/invoicing/recurring/{profileId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/recurring/{_seg(profile_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, profile_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """One recurring invoice with its run history, newest first.
        
        `GET /api/invoicing/recurring/{profileId}` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/recurring/{_seg(profile_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "profile")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, customer_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the recurring invoices the caller may see, with their next runs.
        
        `GET /api/invoicing/recurring` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/recurring", query={"organizationId": organization_id, "customerId": customer_id}, body=None, multipart=False, options=options), "profiles")  # type: ignore[no-any-return]

    def prefill(self, *, organization_id: Optional[str] = None, document_id: str, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """What a new recurring invoice made from an invoice starts from; nothing is saved.
        
        `GET /api/invoicing/recurring/from-document` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/recurring/from-document", query={"organizationId": organization_id, "documentId": document_id}, body=None, multipart=False, options=options), "prefill")  # type: ignore[no-any-return]

    def update(self, profile_id: str, body: InvoicingRecurringUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes a recurring invoice, or pauses and resumes it.
        
        Needs `invoicing:create` and recurring invoices on the plan. Resuming starts from today: periods missed while paused are not billed.
        
        `PATCH /api/invoicing/recurring/{profileId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/recurring/{_seg(profile_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "profile")  # type: ignore[no-any-return]


class InvoicingReportsResource(_Resource):

    def dataset(self, *, organization_id: Optional[str] = None, dataset: Literal["summary", "revenueByMonth", "revenueByCustomer", "revenueByProduct", "openItems", "ageing", "paidVsOpen", "vatByRate", "vatByMonth", "quoteConversion", "expensesByMonth", "expensesBySupplier", "expensesByAccount", "inputVatByRate", "payablesAgeing", "resultByMonth"], period: Optional[Literal["month", "lastMonth", "quarter", "lastQuarter", "year", "lastYear", "12m"]] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """One dataset of the hub's numbers as rows: revenue, open items, VAT, quote conversion, expenses, payables, result.
        
        Read as the caller: the whole books with `invoicing:export`, else what they may see. Amounts in major units with each row's currency. The purchase datasets need purchases on the plan.
        
        `GET /api/invoicing/reports` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/reports", query={"organizationId": organization_id, "dataset": dataset, "period": period}, body=None, multipart=False, options=options), "rows")  # type: ignore[no-any-return]

    def tax_returns(self, *, organization_id: Optional[str] = None, issuer_id: str, from_: str, to: str, format: Optional[Literal["ec-sales", "oss"]] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """One company's EC sales list (Zusammenfassende Meldung), One-Stop-Shop figures and the €10,000 threshold for a period.
        
        Needs `invoicing:export`; the whole books. `format=ec-sales` or `oss` downloads that one as CSV.
        
        `GET /api/invoicing/reports/tax-returns` — Token permission: `read:invoicing`.
        """
        return self._request("GET", f"/api/invoicing/reports/tax-returns", query={"organizationId": organization_id, "issuerId": issuer_id, "from": from_, "to": to, "format": format}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class InvoicingSuppliersResource(_Resource):

    def create(self, body: InvoicingSupplierInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Creates a supplier.
        
        Needs `invoicing:create`. IBAN and BIC are checked; a VAT ID, tax number or IBAN another supplier has answers 409 `invoicingSupplierDuplicate` with `duplicates` unless `allowDuplicate`.
        
        `POST /api/invoicing/suppliers` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/suppliers", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "supplier")  # type: ignore[no-any-return]

    def delete(self, supplier_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingSuppliersDeleteResponse:
        """Deletes a supplier no purchase invoice names.
        
        409 `invoicingSupplierHasInvoices` otherwise — archive them instead.
        
        `DELETE /api/invoicing/suppliers/{supplierId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/suppliers/{_seg(supplier_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, supplier_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """One supplier, with how many purchase invoices name them and what is open per currency.
        
        `GET /api/invoicing/suppliers/{supplierId}` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/suppliers/{_seg(supplier_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "supplier")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, q: Optional[str] = None, include_archived: Optional[Literal["1"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the suppliers the caller may see, by name.
        
        `GET /api/invoicing/suppliers` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/suppliers", query={"organizationId": organization_id, "q": q, "includeArchived": include_archived, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "suppliers")  # type: ignore[no-any-return]

    def update(self, supplier_id: str, body: InvoicingSuppliersUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Changes a supplier, or archives and restores them.
        
        `PATCH /api/invoicing/suppliers/{supplierId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/suppliers/{_seg(supplier_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "supplier")  # type: ignore[no-any-return]


class InvoicingTemplatesResource(_Resource):

    def create(self, body: InvoicingTemplatesCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingTemplate:
        """Creates a PDF template; the first is the default.
        
        Needs `invoicing:settings`; counts against the plan's template limit. Images must be the organisation's; the layout is checked strictly (400 `invoicingUnknownMergeField` / `invoicingLayoutInvalid`).
        
        `POST /api/invoicing/templates` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("POST", f"/api/invoicing/templates", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "template")  # type: ignore[no-any-return]

    def delete(self, template_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingTemplatesDeleteResponse:
        """Deletes a PDF template; documents that used it render with the default.
        
        `DELETE /api/invoicing/templates/{templateId}` — Token permission: `write:invoicing`.
        """
        return self._request("DELETE", f"/api/invoicing/templates/{_seg(template_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, template_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingTemplate:
        """One PDF template.
        
        `GET /api/invoicing/templates/{templateId}` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/templates/{_seg(template_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "template")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InvoicingTemplate]:
        """Lists the organisation's PDF templates, with the layout every unset key falls back to and the fonts on offer.
        
        `GET /api/invoicing/templates` — Token permission: `read:invoicing`.
        """
        return _pick(self._request("GET", f"/api/invoicing/templates", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "templates")  # type: ignore[no-any-return]

    def preview(self, body: InvoicingTemplatesPreviewBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Renders a template as a PDF — with a given document, or the built-in sample — without storing anything.
        
        Needs `invoicing:settings`. Answers the PDF. The config sent, else the template `templateId`, else the default. 30 a minute.
        
        `POST /api/invoicing/templates/preview` — Token permission: `write:invoicing`.
        """
        return self._request("POST", f"/api/invoicing/templates/preview", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, template_id: str, body: InvoicingTemplatesUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InvoicingTemplate:
        """Changes a PDF template; `config` and `texts` replace what was stored.
        
        Needs `invoicing:settings`. Send `config` whole, `layout` included.
        
        `PATCH /api/invoicing/templates/{templateId}` — Token permission: `write:invoicing`.
        """
        return _pick(self._request("PATCH", f"/api/invoicing/templates/{_seg(template_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "template")  # type: ignore[no-any-return]


class InvoicingResource(_Resource):
    """Invoicing — Quotes, order confirmations, invoices and credit notes with e-invoices (XRechnung, ZUGFeRD); customers, issuing companies, number ranges and PDF templates; payments and dunning; recurring invoices; received e-invoices, purchase invoices, suppliers and SEPA payment runs; the books (EÜR or double entry) with DATEV export. Every operation works in one organisation (`organizationId`) and needs the role's `invoicing:*` permissions held at organisation level. A finalized document is never changed or deleted: it is corrected with a credit note or a cancellation.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.approval_rules = InvoicingApprovalRulesResource(request)
        self.customers = InvoicingCustomersResource(request)
        self.documents = InvoicingDocumentsResource(request)
        self.dunning = InvoicingDunningResource(request)
        self.inbound = InvoicingInboundResource(request)
        self.issuers = InvoicingIssuersResource(request)
        self.ledger = InvoicingLedgerResource(request)
        self.number_ranges = InvoicingNumberRangesResource(request)
        self.payment_runs = InvoicingPaymentRunsResource(request)
        self.payments = InvoicingPaymentsResource(request)
        self.purchases = InvoicingPurchasesResource(request)
        self.recurring = InvoicingRecurringResource(request)
        self.reports = InvoicingReportsResource(request)
        self.suppliers = InvoicingSuppliersResource(request)
        self.templates = InvoicingTemplatesResource(request)


class ItemFoldersResource(_Resource):
    """Item folders — Folders for the lists of databases, documents, endpoints, reports, projects and workflows — shared per workspace and per kind. Organising only: an item's address, sharing and content never change with its folder. Folders nest up to five levels; an item is in one folder or in none. Reading needs `<kind>:read` and the workspace; making, renaming and deleting folders and filing items needs `<kind>:update`.
    """

    def create(self, body: ItemFoldersCreateBody, *, options: Optional[RequestOptions] = None) -> ItemFolder:
        """Creates a folder in one kind of list of a workspace.
        
        400 `pageFolderCycle` when the folder would sit deeper than five levels; 404 `folderNotFound` for a parent that is not a folder of that list.
        
        `POST /api/item-folders`
        """
        return _pick(self._request("POST", f"/api/item-folders", query=None, body=body, multipart=False, options=options), "data.folder")  # type: ignore[no-any-return]

    def delete(self, folder_id: str, *, options: Optional[RequestOptions] = None) -> ItemFoldersDeleteResponseData:
        """Deletes a folder; its items go to no folder and its subfolders move up one level.
        
        No item is deleted.
        
        `DELETE /api/item-folders/{folderId}`
        """
        return _pick(self._request("DELETE", f"/api/item-folders/{_seg(folder_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, workspace_id: str, kind: ItemFolderKind, options: Optional[RequestOptions] = None) -> ItemFolders:
        """Lists the folders of one kind of item in a workspace, and which item is filed where.
        
        `GET /api/item-folders`
        """
        return _pick(self._request("GET", f"/api/item-folders", query={"workspaceId": workspace_id, "kind": kind}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def move(self, body: ItemFoldersMoveBody, *, options: Optional[RequestOptions] = None) -> float:
        """Files items of one list in a folder, or takes them out of every folder.
        
        Only items of that kind in that workspace are filed; other ids are skipped, and `moved` counts the rest. Nothing about the items themselves changes.
        
        `POST /api/item-folders/move`
        """
        return _pick(self._request("POST", f"/api/item-folders/move", query=None, body=body, multipart=False, options=options), "data.moved")  # type: ignore[no-any-return]

    def update(self, folder_id: str, body: ItemFoldersUpdateBody, *, options: Optional[RequestOptions] = None) -> ItemFolder:
        """Renames a folder or moves it into another folder.
        
        Only the fields sent change. 400 `pageFolderCycle` when the move would put it inside itself or deeper than five levels.
        
        `PATCH /api/item-folders/{folderId}`
        """
        return _pick(self._request("PATCH", f"/api/item-folders/{_seg(folder_id)}", query=None, body=body, multipart=False, options=options), "data.folder")  # type: ignore[no-any-return]


class LanguagesResource(_Resource):
    """Languages
    """

    def list(self, *, options: Optional[RequestOptions] = None) -> List[PlatformLanguage]:
        """Lists the languages the platform is available in.
        
        Answers without a token. Only enabled languages, in the administrator's order; cached for five minutes.
        
        `GET /api/languages` — No token needed.
        """
        return self._request("GET", f"/api/languages", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class MailAiResource(_Resource):

    def draft_reply(self, body: MailAiDraftReplyBody, *, options: Optional[RequestOptions] = None) -> MailAiDraftReplyResponseData:
        """Drafts a reply to a conversation with AI; nothing is sent.
        
        Needs AI writing help on the plan, counts against the organisation's AI allowance (429 when used up) and is refused to a person who opted out of AI. Reads the last four messages of a conversation the caller can open.
        
        `POST /api/mail/ai/draft-reply`
        """
        return _pick(self._request("POST", f"/api/mail/ai/draft-reply", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def rewrite(self, body: MailAiRewriteBody, *, options: Optional[RequestOptions] = None) -> str:
        """Rewrites a message text more formal, friendlier, shorter, longer or as instructed.
        
        Needs AI writing help on the plan, counts against the organisation's AI allowance (429 when used up) and is refused to a person who opted out of AI.
        
        `POST /api/mail/ai/rewrite`
        """
        return _pick(self._request("POST", f"/api/mail/ai/rewrite", query=None, body=body, multipart=False, options=options), "data.body")  # type: ignore[no-any-return]

    def subject(self, body: MailAiSubjectBody, *, options: Optional[RequestOptions] = None) -> str:
        """Suggests a subject line for a message text.
        
        Needs AI writing help on the plan, counts against the organisation's AI allowance (429 when used up) and is refused to a person who opted out of AI.
        
        `POST /api/mail/ai/subject`
        """
        return _pick(self._request("POST", f"/api/mail/ai/subject", query=None, body=body, multipart=False, options=options), "data.subject")  # type: ignore[no-any-return]

    def summarize_thread(self, body: MailAiSummarizeThreadBody, *, options: Optional[RequestOptions] = None) -> MailAiSummarizeThreadResponseData:
        """Summarises a conversation with AI: the gist, key points, what is asked and the tone.
        
        Needs AI writing help on the plan, counts against the organisation's AI allowance (429 when used up) and is refused to a person who opted out of AI. A conversation the caller can open.
        
        `POST /api/mail/ai/summarize-thread`
        """
        return _pick(self._request("POST", f"/api/mail/ai/summarize-thread", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class MailImapResource(_Resource):

    def action(self, body: MailImapActionBody, *, options: Optional[RequestOptions] = None) -> MailImapActionResponse:
        """Marks a message of a saved IMAP connection read or unread, or deletes it.
        
        Not in the usual envelope. The connection must be the caller's own.
        
        `POST /api/imap/action`
        """
        return self._request("POST", f"/api/imap/action", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def fetch(self, body: MailImapFetchBody, *, options: Optional[RequestOptions] = None) -> List[MailImapFetchResponseEmailsItem]:
        """Reads messages from the mailbox of a saved IMAP connection.
        
        Not in the usual envelope. The connection must be the caller's own (404 `connectionNotFound`); its host must be public (`imapHostRefused`).
        
        `POST /api/imap/fetch`
        """
        return _pick(self._request("POST", f"/api/imap/fetch", query=None, body=body, multipart=False, options=options), "emails")  # type: ignore[no-any-return]

    def verify(self, body: MailImapVerifyBody, *, options: Optional[RequestOptions] = None) -> MailImapVerifyResponse:
        """Tries an IMAP login, before a mailbox is connected with it.
        
        Not in the usual envelope. The host must be public. Ten an account in ten minutes. 500 `imapAuthFailed` for a refused login, `imapConnectFailed` when the server does not answer as one.
        
        `POST /api/imap/verify`
        """
        return self._request("POST", f"/api/imap/verify", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class MailSmtpResource(_Resource):

    def verify(self, body: MailSmtpVerifyBody, *, options: Optional[RequestOptions] = None) -> MailSmtpVerifyResponse:
        """Tries an SMTP login, before a mailbox is connected with it.
        
        Not in the usual envelope. The host must be public. Ten an account in ten minutes. Port 465 is TLS, 587 STARTTLS.
        
        `POST /api/smtp/verify`
        """
        return self._request("POST", f"/api/smtp/verify", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class MailResource(_Resource):
    """Mail — The Mail hub: mailboxes (IMAP, Gmail, Outlook and the platform's own address), conversations and messages, drafts, sending now or queued, labels, signatures, snippets, rules, blocked senders, out-of-office replies and PGP. Everything needs Mail on the caller's plan (403 otherwise). A mailbox is its owner's; one shared with an organisation can be read and sent from by its members, while its settings stay the owner's.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.ai = MailAiResource(request)
        self.imap = MailImapResource(request)
        self.smtp = MailSmtpResource(request)

    def add_pgp_key(self, body: MailAddPgpKeyBody, *, options: Optional[RequestOptions] = None) -> MailPgpKey:
        """Adds an armored PGP key: a contact's public key or the caller's own key pair.
        
        Needs PGP on the plan and `mail:manage_pgp_keys`. A private key is stored encrypted and stays locked by its own passphrase. 409 when it is already there.
        
        `POST /api/mail/pgp/keys`
        """
        return _pick(self._request("POST", f"/api/mail/pgp/keys", query=None, body=body, multipart=False, options=options), "data.key")  # type: ignore[no-any-return]

    def apply_invite_reply(self, id: str, *, options: Optional[RequestOptions] = None) -> MailApplyInviteReplyResponseData:
        """Records a guest's answer, attached to a message, on the appointment it answers.
        
        Needs Calendar too. Only when the message's sender is the guest answering and already on the guest list of an appointment the caller can edit; doing it again changes nothing.
        
        `POST /api/mail/attachments/{id}/apply-reply`
        """
        return _pick(self._request("POST", f"/api/mail/attachments/{_seg(id)}/apply-reply", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def apply_rule(self, id: str, body: MailApplyRuleBody, *, options: Optional[RequestOptions] = None) -> MailApplyRuleResponseData:
        """Runs a rule once over the mail already stored.
        
        The newest 2,000 messages of a folder of the rule's mailbox (or of the caller's own mailboxes). Moves and deletes happen on the mail server too.
        
        `POST /api/mail/rules/{id}/apply`
        """
        return _pick(self._request("POST", f"/api/mail/rules/{_seg(id)}/apply", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def block_sender(self, body: MailBlockSenderBody, *, options: Optional[RequestOptions] = None) -> MailBlockSenderResponseDataSender:
        """Blocks an address or a domain: new mail from it is filed in spam.
        
        Blocking one already blocked answers it with `created: false`.
        
        `POST /api/mail/blocked-senders`
        """
        return _pick(self._request("POST", f"/api/mail/blocked-senders", query=None, body=body, multipart=False, options=options), "data.sender")  # type: ignore[no-any-return]

    def cancel_scheduled(self, id: str, *, options: Optional[RequestOptions] = None) -> MailCancelScheduledResponse:
        """Cancels a queued send that has not gone out, or dismisses a failed one.
        
        409 when it is already sending or gone.
        
        `DELETE /api/mail/scheduled/{id}`
        """
        return self._request("DELETE", f"/api/mail/scheduled/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def check_platform_address(self, *, username: Optional[str] = None, options: Optional[RequestOptions] = None) -> MailCheckPlatformAddressResponse:
        """Whether a name is still free on the platform's own mail domain.
        
        Not in the usual envelope. Without `username` it answers only the domain. `reason` when refused: contains_plus, too_short, invalid_chars.
        
        `GET /api/mail/platform-address/check`
        """
        return self._request("GET", f"/api/mail/platform-address/check", query={"username": username}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def counts(self, *, account_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MailCountsResponseData:
        """Unread conversations per folder and per mailbox, starred, drafts and queued sends.
        
        `GET /api/mail/counts`
        """
        return _pick(self._request("GET", f"/api/mail/counts", query={"accountId": account_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_account(self, body: MailCreateAccountBody, *, options: Optional[RequestOptions] = None) -> MailAccount:
        """Connects an IMAP/SMTP mailbox and starts its first sync.
        
        Needs external mailboxes on the plan and room under its mailbox limit. The servers must be reachable public hosts (400 otherwise). Gmail and Outlook are connected in a browser; the platform's own address is POST /api/mail/platform-address.
        
        `POST /api/mail/accounts`
        """
        return _pick(self._request("POST", f"/api/mail/accounts", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_alias(self, account_id: str, body: MailCreateAliasBody, *, options: Optional[RequestOptions] = None) -> MailAlias:
        """Adds a send-as address to a mailbox and mails a confirmation link to it.
        
        Only the mailbox's owner; anybody else gets 404. It can be sent from once the link in that inbox is opened. At most 20 per mailbox; 10 requests an hour.
        
        `POST /api/mail/accounts/{accountId}/aliases`
        """
        return _pick(self._request("POST", f"/api/mail/accounts/{_seg(account_id)}/aliases", query=None, body=body, multipart=False, options=options), "data.alias")  # type: ignore[no-any-return]

    def create_draft(self, body: MailCreateDraftBody, *, options: Optional[RequestOptions] = None) -> MailDraft:
        """Saves a new draft in a mailbox the caller can send from.
        
        A reply keeps In-Reply-To / References and its conversation, when the caller may open it.
        
        `POST /api/mail/drafts`
        """
        return _pick(self._request("POST", f"/api/mail/drafts", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_folder(self, account_id: str, body: MailCreateFolderBody, *, options: Optional[RequestOptions] = None) -> MailCreateFolderResponseData:
        """Creates a folder on the mailbox's server.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `POST /api/mail/accounts/{accountId}/folders`
        """
        return _pick(self._request("POST", f"/api/mail/accounts/{_seg(account_id)}/folders", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_label(self, body: MailCreateLabelBody, *, options: Optional[RequestOptions] = None) -> MailLabel:
        """Creates a label.
        
        At most 100 (429).
        
        `POST /api/mail/labels`
        """
        return _pick(self._request("POST", f"/api/mail/labels", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_platform_address(self, body: MailCreatePlatformAddressBody, *, options: Optional[RequestOptions] = None) -> MailCreatePlatformAddressResponseData:
        """Creates the caller's mailbox on the platform's own domain.
        
        Needs `mail:manage_platform` and the platform address on the plan. Having one already answers it. The name may not contain `+` (reserved for sub-addresses); without one it is made from the caller's name.
        
        `POST /api/mail/platform-address`
        """
        return _pick(self._request("POST", f"/api/mail/platform-address", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_rule(self, body: MailCreateRuleBody, *, options: Optional[RequestOptions] = None) -> MailRule:
        """Creates a rule that acts on new mail.
        
        On one of the caller's own mailboxes, or on all of them. At most 100 (429).
        
        `POST /api/mail/rules`
        """
        return _pick(self._request("POST", f"/api/mail/rules", query=None, body=body, multipart=False, options=options), "data.rule")  # type: ignore[no-any-return]

    def create_signature(self, body: MailCreateSignatureBody, *, options: Optional[RequestOptions] = None) -> MailSignature:
        """Creates a signature.
        
        The HTML is sanitised. At most 25 (429). A new default replaces the old one.
        
        `POST /api/mail/signatures`
        """
        return _pick(self._request("POST", f"/api/mail/signatures", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_snippet(self, body: MailCreateSnippetBody, *, options: Optional[RequestOptions] = None) -> MailSnippet:
        """Creates a snippet.
        
        The HTML is sanitised. At most 200 (429); a shortcut already used answers 409.
        
        `POST /api/mail/snippets`
        """
        return _pick(self._request("POST", f"/api/mail/snippets", query=None, body=body, multipart=False, options=options), "data.snippet")  # type: ignore[no-any-return]

    def create_thread_note(self, thread_id: str, body: MailCreateThreadNoteBody, *, options: Optional[RequestOptions] = None) -> MailThreadNote:
        """Adds an internal note to a conversation.
        
        The people it mentions and the assignee are notified.
        
        `POST /api/mail/threads/{threadId}/notes`
        """
        return _pick(self._request("POST", f"/api/mail/threads/{_seg(thread_id)}/notes", query=None, body=body, multipart=False, options=options), "data.note")  # type: ignore[no-any-return]

    def decrypt(self, email_id: str, body: MailDecryptBody, *, options: Optional[RequestOptions] = None) -> MailDecryptResponseData:
        """Decrypts a PGP-encrypted message with the caller's own keys and checks its signature.
        
        Needs PGP on the plan. The passphrase is used once and never stored; 428 when a key needs one and none was sent, 422 when no key opens it, 403 without a private key. `signatureValid` is null when there was nothing to check against.
        
        `POST /api/mail/emails/{emailId}/decrypt`
        """
        return _pick(self._request("POST", f"/api/mail/emails/{_seg(email_id)}/decrypt", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_account(self, id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteAccountResponse:
        """Disconnects a mailbox and deletes its stored mail here.
        
        Only the mailbox's owner; anybody else gets 404. The platform address cannot be deleted (400). The mail on the server is not touched.
        
        `DELETE /api/mail/accounts/{id}`
        """
        return self._request("DELETE", f"/api/mail/accounts/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_alias(self, account_id: str, alias_id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteAliasResponse:
        """Removes a send-as address from a mailbox.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `DELETE /api/mail/accounts/{accountId}/aliases/{aliasId}`
        """
        return self._request("DELETE", f"/api/mail/accounts/{_seg(account_id)}/aliases/{_seg(alias_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_attachment(self, id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Deletes an upload that has not been sent yet.
        
        An attachment of a sent message cannot be deleted (403). Answers 204.
        
        `DELETE /api/mail/attachments/{id}`
        """
        return self._request("DELETE", f"/api/mail/attachments/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_draft(self, id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteDraftResponse:
        """Deletes a draft of the caller's.
        
        `DELETE /api/mail/drafts/{id}`
        """
        return self._request("DELETE", f"/api/mail/drafts/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_folder(self, account_id: str, *, path: str, options: Optional[RequestOptions] = None) -> MailDeleteFolderResponseData:
        """Deletes a folder on the mailbox's server.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `DELETE /api/mail/accounts/{accountId}/folders`
        """
        return _pick(self._request("DELETE", f"/api/mail/accounts/{_seg(account_id)}/folders", query={"path": path}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_label(self, id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteLabelResponse:
        """Deletes a label.
        
        A system label cannot be deleted (400).
        
        `DELETE /api/mail/labels/{id}`
        """
        return self._request("DELETE", f"/api/mail/labels/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_pgp_key(self, id: str, *, options: Optional[RequestOptions] = None) -> MailDeletePgpKeyResponse:
        """Removes a PGP key from the caller's keyring for good.
        
        Needs PGP on the plan and `mail:manage_pgp_keys`.
        
        `DELETE /api/mail/pgp/keys/{id}`
        """
        return self._request("DELETE", f"/api/mail/pgp/keys/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_rule(self, id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteRuleResponse:
        """Deletes a rule.
        
        `DELETE /api/mail/rules/{id}`
        """
        return self._request("DELETE", f"/api/mail/rules/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_signature(self, id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteSignatureResponse:
        """Deletes a signature.
        
        `DELETE /api/mail/signatures/{id}`
        """
        return self._request("DELETE", f"/api/mail/signatures/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_snippet(self, id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteSnippetResponse:
        """Deletes a snippet.
        
        `DELETE /api/mail/snippets/{id}`
        """
        return self._request("DELETE", f"/api/mail/snippets/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_thread(self, thread_id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteThreadResponse:
        """Moves a conversation to the trash; one already in the trash is deleted for good.
        
        On the mail server too.
        
        `DELETE /api/mail/threads/{threadId}`
        """
        return self._request("DELETE", f"/api/mail/threads/{_seg(thread_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_thread_note(self, thread_id: str, note_id: str, *, options: Optional[RequestOptions] = None) -> MailDeleteThreadNoteResponse:
        """Deletes a note from a conversation.
        
        Its author or the conversation's owner (403 otherwise).
        
        `DELETE /api/mail/threads/{threadId}/notes/{noteId}`
        """
        return self._request("DELETE", f"/api/mail/threads/{_seg(thread_id)}/notes/{_seg(note_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def desk(self, *, account_id: Optional[str] = None, assignee: Optional[str] = None, options: Optional[RequestOptions] = None) -> MailDeskResponseData:
        """The inbox as an Action desk: the open conversations that still ask something, each in one of five sections with the reason.
        
        In the inbox, not snoozed or resolved; the newest 200.
        
        `GET /api/mail/desk`
        """
        return _pick(self._request("GET", f"/api/mail/desk", query={"accountId": account_id, "assignee": assignee}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def download_attachment(self, id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Downloads an attachment of a message the caller can open.
        
        `GET /api/mail/attachments/{id}`
        """
        return self._request("GET", f"/api/mail/attachments/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def empty_trash(self, body: MailEmptyTrashBody, *, options: Optional[RequestOptions] = None) -> MailEmptyTrashResponseData:
        """Deletes everything in the trash for good, here and on the mail server.
        
        Of one mailbox, or of every mailbox of the caller's own.
        
        `POST /api/mail/trash/empty`
        """
        return _pick(self._request("POST", f"/api/mail/trash/empty", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_account(self, id: str, *, options: Optional[RequestOptions] = None) -> MailGetAccountResponseData:
        """One mailbox the caller can open.
        
        Never the password; `loginUsername` only for the owner of an IMAP mailbox.
        
        `GET /api/mail/accounts/{id}`
        """
        return _pick(self._request("GET", f"/api/mail/accounts/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_account_organization(self, account_id: str, *, options: Optional[RequestOptions] = None) -> MailGetAccountOrganizationResponseData:
        """Which organisation a shared mailbox is shared with, and which it could be.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `GET /api/mail/accounts/{accountId}/organization`
        """
        return _pick(self._request("GET", f"/api/mail/accounts/{_seg(account_id)}/organization", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_auto_response(self, account_id: str, *, options: Optional[RequestOptions] = None) -> MailAutoResponse:
        """A mailbox's out-of-office reply and forwarding.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `GET /api/mail/accounts/{accountId}/auto-response`
        """
        return _pick(self._request("GET", f"/api/mail/accounts/{_seg(account_id)}/auto-response", query=None, body=None, multipart=False, options=options), "data.settings")  # type: ignore[no-any-return]

    def get_contact(self, address: str, *, options: Optional[RequestOptions] = None) -> MailGetContactResponseData:
        """What the caller's mail says about one address: name, first and last mail, counts both ways and reply rate.
        
        `GET /api/mail/contacts/{address}`
        """
        return _pick(self._request("GET", f"/api/mail/contacts/{_seg(address)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_opens(self, email_id: str, *, options: Optional[RequestOptions] = None) -> MailGetOpensResponseData:
        """How often a sent message with a read receipt was opened, and when first and last.
        
        `GET /api/mail/emails/{emailId}/opens`
        """
        return _pick(self._request("GET", f"/api/mail/emails/{_seg(email_id)}/opens", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_platform_address(self, *, options: Optional[RequestOptions] = None) -> MailAccount:
        """The caller's mailbox on the platform's own domain, or null.
        
        `GET /api/mail/platform-address`
        """
        return _pick(self._request("GET", f"/api/mail/platform-address", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_raw(self, email_id: str, *, download: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a message's original source from the mail server, as text or as an .eml file.
        
        404 `mailRawNotOnServer` when the server no longer has it, 413 `mailRawTooLarge`, 502 `mailRawUnreachable`.
        
        `GET /api/mail/emails/{emailId}/raw`
        """
        return self._request("GET", f"/api/mail/emails/{_seg(email_id)}/raw", query={"download": download}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_retention(self, account_id: str, *, options: Optional[RequestOptions] = None) -> MailGetRetentionResponseData:
        """How many days a mailbox's mail is kept here.
        
        Only the mailbox's owner; anybody else gets 404. 0 keeps it for ever.
        
        `GET /api/mail/accounts/{accountId}/retention`
        """
        return _pick(self._request("GET", f"/api/mail/accounts/{_seg(account_id)}/retention", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_thread(self, thread_id: str, *, options: Optional[RequestOptions] = None) -> MailGetThreadResponseData:
        """One conversation with its messages, oldest first, and their attachments; marks it read.
        
        Each message carries `safety` (SPF/DKIM/DMARC and the sender checks) and, on received mail, a `verificationCode` found in it. Inline images are embedded in `htmlBody`.
        
        `GET /api/mail/threads/{threadId}`
        """
        return _pick(self._request("GET", f"/api/mail/threads/{_seg(thread_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_accounts(self, *, options: Optional[RequestOptions] = None) -> List[MailListAccountsResponseDataItem]:
        """Lists the mailboxes the caller can open: their own and those shared with them.
        
        `GET /api/mail/accounts`
        """
        return _pick(self._request("GET", f"/api/mail/accounts", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_aliases(self, account_id: str, *, options: Optional[RequestOptions] = None) -> List[MailAlias]:
        """Lists the addresses a mailbox may send as.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `GET /api/mail/accounts/{accountId}/aliases`
        """
        return _pick(self._request("GET", f"/api/mail/accounts/{_seg(account_id)}/aliases", query=None, body=None, multipart=False, options=options), "data.aliases")  # type: ignore[no-any-return]

    def list_blocked_senders(self, *, options: Optional[RequestOptions] = None) -> List[MailListBlockedSendersResponseDataSendersItem]:
        """Lists the caller's blocked senders, oldest first.
        
        `GET /api/mail/blocked-senders`
        """
        return _pick(self._request("GET", f"/api/mail/blocked-senders", query=None, body=None, multipart=False, options=options), "data.senders")  # type: ignore[no-any-return]

    def list_drafts(self, *, options: Optional[RequestOptions] = None) -> List[MailDraft]:
        """Lists the caller's drafts, last changed first.
        
        `GET /api/mail/drafts`
        """
        return _pick(self._request("GET", f"/api/mail/drafts", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_folders(self, account_id: str, *, options: Optional[RequestOptions] = None) -> MailListFoldersResponseData:
        """Lists a mailbox's folders on its server, and which of them are synced.
        
        Only the mailbox's owner; anybody else gets 404. Asks the mail server, so it fails (500 `actionFailed`) when the server cannot be reached.
        
        `GET /api/mail/accounts/{accountId}/folders`
        """
        return _pick(self._request("GET", f"/api/mail/accounts/{_seg(account_id)}/folders", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_labels(self, *, options: Optional[RequestOptions] = None) -> List[MailLabel]:
        """Lists the caller's labels.
        
        `GET /api/mail/labels`
        """
        return _pick(self._request("GET", f"/api/mail/labels", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_newsletters(self, *, limit: Optional[int] = None, cursor: Optional[str] = None, hints: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> MailListNewslettersResponseData:
        """Lists the newsletters in the inboxes and archives the caller can open, newest first.
        
        `GET /api/mail/newsletters`
        """
        return _pick(self._request("GET", f"/api/mail/newsletters", query={"limit": limit, "cursor": cursor, "hints": hints}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_pgp_keys(self, *, options: Optional[RequestOptions] = None) -> List[MailPgpKey]:
        """Lists the caller's PGP keys: their own and their contacts'.
        
        Needs PGP on the plan. Private keys are never answered.
        
        `GET /api/mail/pgp/keys`
        """
        return _pick(self._request("GET", f"/api/mail/pgp/keys", query=None, body=None, multipart=False, options=options), "data.keys")  # type: ignore[no-any-return]

    def list_rules(self, *, options: Optional[RequestOptions] = None) -> List[MailRule]:
        """Lists the caller's rules in the order they run.
        
        `GET /api/mail/rules`
        """
        return _pick(self._request("GET", f"/api/mail/rules", query=None, body=None, multipart=False, options=options), "data.rules")  # type: ignore[no-any-return]

    def list_scheduled(self, *, options: Optional[RequestOptions] = None) -> List[MailScheduledSend]:
        """Lists the caller's queued sends, latest send time first.
        
        The newest 200, in every status.
        
        `GET /api/mail/scheduled`
        """
        return _pick(self._request("GET", f"/api/mail/scheduled", query=None, body=None, multipart=False, options=options), "data.scheduled")  # type: ignore[no-any-return]

    def list_signatures(self, *, options: Optional[RequestOptions] = None) -> List[MailSignature]:
        """Lists the caller's signatures.
        
        `GET /api/mail/signatures`
        """
        return _pick(self._request("GET", f"/api/mail/signatures", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_snippets(self, *, options: Optional[RequestOptions] = None) -> List[MailSnippet]:
        """Lists the caller's snippets (canned replies), by name.
        
        `GET /api/mail/snippets`
        """
        return _pick(self._request("GET", f"/api/mail/snippets", query=None, body=None, multipart=False, options=options), "data.snippets")  # type: ignore[no-any-return]

    def list_subaddresses(self, *, options: Optional[RequestOptions] = None) -> List[MailListSubaddressesResponseDataSubaddressesItem]:
        """Lists the `+tag` addresses of the caller's mailboxes that received mail, with who used them.
        
        `GET /api/mail/subaddresses`
        """
        return _pick(self._request("GET", f"/api/mail/subaddresses", query=None, body=None, multipart=False, options=options), "data.subaddresses")  # type: ignore[no-any-return]

    def list_teammates(self, account_id: str, *, options: Optional[RequestOptions] = None) -> List[MailTeammate]:
        """The people a conversation of this mailbox can be assigned to.
        
        A shared inbox: every member of the organisation it is shared with. Otherwise only its owner.
        
        `GET /api/mail/accounts/{accountId}/teammates`
        """
        return _pick(self._request("GET", f"/api/mail/accounts/{_seg(account_id)}/teammates", query=None, body=None, multipart=False, options=options), "data.teammates")  # type: ignore[no-any-return]

    def list_thread_notes(self, thread_id: str, *, options: Optional[RequestOptions] = None) -> List[MailThreadNote]:
        """Lists a conversation's internal notes, oldest first.
        
        Notes are for teammates and never sent to the customer.
        
        `GET /api/mail/threads/{threadId}/notes`
        """
        return _pick(self._request("GET", f"/api/mail/threads/{_seg(thread_id)}/notes", query=None, body=None, multipart=False, options=options), "data.notes")  # type: ignore[no-any-return]

    def list_threads(self, *, folder: Optional[str] = None, account_id: Optional[str] = None, unread: Optional[bool] = None, has_attachments: Optional[bool] = None, starred: Optional[bool] = None, label: Optional[str] = None, assignee: Optional[str] = None, status: Optional[Literal["open", "pending", "resolved", "waiting"]] = None, sort_by: Optional[Literal["date", "subject", "sender"]] = None, sort_dir: Optional[Literal["asc", "desc"]] = None, view: Optional[Literal["threaded", "flat"]] = None, page: Optional[int] = None, limit: Optional[int] = None, nudges: Optional[Literal["1"]] = None, follow_ups: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> MailListThreadsResponseData:
        """Lists one page of conversations of a folder, newest first, across the caller's mailboxes or of one.
        
        `view=flat` lists single messages instead (each with `_actualThreadId`); assignee and status filters apply to conversations only.
        
        `GET /api/mail/threads`
        """
        return _pick(self._request("GET", f"/api/mail/threads", query={"folder": folder, "accountId": account_id, "unread": unread, "hasAttachments": has_attachments, "starred": starred, "label": label, "assignee": assignee, "status": status, "sortBy": sort_by, "sortDir": sort_dir, "view": view, "page": page, "limit": limit, "nudges": nudges, "followUps": follow_ups}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def lookup_pgp_keys(self, body: MailLookupPgpKeysBody, *, options: Optional[RequestOptions] = None) -> Dict[str, MailLookupPgpKeysResponseDataKeysValue]:
        """Says which of the given addresses the caller holds a public key for.
        
        Needs PGP on the plan. 30 a minute.
        
        `POST /api/mail/pgp/lookup`
        """
        return _pick(self._request("POST", f"/api/mail/pgp/lookup", query=None, body=body, multipart=False, options=options), "data.keys")  # type: ignore[no-any-return]

    def mark_all_read(self, body: MailMarkAllReadBody, *, options: Optional[RequestOptions] = None) -> MailMarkAllReadResponseData:
        """Marks every conversation of a view read, here and on the mail server.
        
        `POST /api/mail/threads/mark-all-read`
        """
        return _pick(self._request("POST", f"/api/mail/threads/mark-all-read", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def parse_invite(self, id: str, *, options: Optional[RequestOptions] = None) -> MailParseInviteResponseData:
        """Reads the appointments of a calendar invitation attached to a message.
        
        Each event says whether it is already in one of the caller's calendars (`match`); `calendars` are those it could be added to. 400 when the attachment is not an .ics file.
        
        `GET /api/mail/attachments/{id}/parse-ics`
        """
        return _pick(self._request("GET", f"/api/mail/attachments/{_seg(id)}/parse-ics", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def patch_thread(self, thread_id: str, body: MailPatchThreadBody, *, options: Optional[RequestOptions] = None) -> MailThread:
        """Changes a conversation: read, starred, folder, labels, assignee, status or desk section.
        
        Read and starred apply to its messages and to the mail server too; a new folder moves its messages there on the server. Assigning notifies the new assignee; resolving completes the tasks waiting on it.
        
        `PATCH /api/mail/threads/{threadId}`
        """
        return _pick(self._request("PATCH", f"/api/mail/threads/{_seg(thread_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def rename_folder(self, account_id: str, body: MailRenameFolderBody, *, options: Optional[RequestOptions] = None) -> MailRenameFolderResponseData:
        """Renames or moves a folder on the mailbox's server.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `PATCH /api/mail/accounts/{accountId}/folders`
        """
        return _pick(self._request("PATCH", f"/api/mail/accounts/{_seg(account_id)}/folders", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def reply(self, email_id: str, body: MailReplyBody, *, options: Optional[RequestOptions] = None) -> MailReplyResponseData:
        """Replies to a message now, from its mailbox, in its conversation.
        
        To its sender; with `replyAll` the other recipients in Cc. The subject gets `Re:`.
        
        `POST /api/mail/emails/{emailId}/reply`
        """
        return _pick(self._request("POST", f"/api/mail/emails/{_seg(email_id)}/reply", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def resend_alias_confirmation(self, account_id: str, alias_id: str, *, options: Optional[RequestOptions] = None) -> MailAlias:
        """Mails a send-as address's confirmation link again.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `POST /api/mail/accounts/{accountId}/aliases/{aliasId}`
        """
        return _pick(self._request("POST", f"/api/mail/accounts/{_seg(account_id)}/aliases/{_seg(alias_id)}", query=None, body=None, multipart=False, options=options), "data.alias")  # type: ignore[no-any-return]

    def rethread(self, account_id: str, *, options: Optional[RequestOptions] = None) -> MailRethreadResponseData:
        """Merges a mailbox's conversations that were split although they share a subject.
        
        Only the mailbox's owner; anybody else gets 404. Each group of conversations with the same normalised subject becomes its oldest one.
        
        `POST /api/mail/accounts/{accountId}/rethread`
        """
        return _pick(self._request("POST", f"/api/mail/accounts/{_seg(account_id)}/rethread", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def rsvp(self, id: str, body: MailRsvpBody, *, options: Optional[RequestOptions] = None) -> MailRsvpResponseData:
        """Answers a calendar invitation attached to a message: accepted, declined or tentative.
        
        Mails the organiser a calendar reply from the message's mailbox.
        
        `POST /api/mail/attachments/{id}/rsvp`
        """
        return _pick(self._request("POST", f"/api/mail/attachments/{_seg(id)}/rsvp", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def save_attachment_to_assets(self, id: str, body: MailSaveAttachmentToAssetsBody, *, options: Optional[RequestOptions] = None) -> MailSaveAttachmentToAssetsResponseData:
        """Saves an attachment as a file in Assets.
        
        Saving the same attachment again answers the existing file (`created: false`).
        
        `POST /api/mail/attachments/{id}/save-to-assets`
        """
        return _pick(self._request("POST", f"/api/mail/attachments/{_seg(id)}/save-to-assets", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def schedule(self, body: MailScheduleBody, *, options: Optional[RequestOptions] = None) -> MailScheduleResponseData:
        """Queues a send: in ten seconds with a chance to undo, or at a chosen time.
        
        `kind: scheduled` needs `sendAt` between 30 seconds and 365 days ahead. The queue sends with the same rules as POST /api/mail/send. 60 a minute.
        
        `POST /api/mail/scheduled`
        """
        return _pick(self._request("POST", f"/api/mail/scheduled", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def search(self, *, q: Optional[str] = None, account_id: Optional[str] = None, folder: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, has_attachment: Optional[bool] = None, is_unread: Optional[bool] = None, is_starred: Optional[bool] = None, after: Optional[str] = None, before: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[MailEmail]:
        """Searches the messages of every mailbox the caller can open, best matches first.
        
        `q` takes web-search syntax: quoted phrases, `-excluded`, `OR`. With at least one filter `q` may be empty, and the newest matches come first.
        
        `GET /api/mail/search`
        """
        return _pick(self._request("GET", f"/api/mail/search", query={"q": q, "accountId": account_id, "folder": folder, "from": from_, "to": to, "hasAttachment": has_attachment, "isUnread": is_unread, "isStarred": is_starred, "after": after, "before": before, "limit": limit}, body=None, multipart=False, options=options), "data.emails")  # type: ignore[no-any-return]

    def search_contacts(self, *, q: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[MailSearchContactsResponseDataContactsItem]:
        """Suggests addresses the caller has corresponded with, most frequent first.
        
        `GET /api/mail/contacts/search`
        """
        return _pick(self._request("GET", f"/api/mail/contacts/search", query={"q": q, "limit": limit}, body=None, multipart=False, options=options), "data.contacts")  # type: ignore[no-any-return]

    def send(self, body: MailSendBody, *, options: Optional[RequestOptions] = None) -> MailSendResponseData:
        """Sends a message now and waits for the mail server.
        
        From a mailbox the caller can send from. The header `Idempotency-Key` makes a retry answer the first result for 24 hours. 60 a minute. Documents (`documentAttachments`) are attached only by a queued send (POST /api/mail/scheduled).
        
        `POST /api/mail/send`
        """
        return _pick(self._request("POST", f"/api/mail/send", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_account_organization(self, account_id: str, body: MailSetAccountOrganizationBody, *, options: Optional[RequestOptions] = None) -> MailSetAccountOrganizationResponseData:
        """Chooses the organisation a shared mailbox is shared with.
        
        Only the mailbox's owner; anybody else gets 404. One of the owner's own organisations (403 otherwise), with room for the mailbox under its plan.
        
        `PUT /api/mail/accounts/{accountId}/organization`
        """
        return _pick(self._request("PUT", f"/api/mail/accounts/{_seg(account_id)}/organization", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_auto_response(self, account_id: str, body: MailSetAutoResponseBody, *, options: Optional[RequestOptions] = None) -> MailAutoResponse:
        """Sets a mailbox's out-of-office reply and forwarding, whole.
        
        Only the mailbox's owner; anybody else gets 404. An enabled reply needs a subject and a message, forwarding an address other than the mailbox's own.
        
        `PUT /api/mail/accounts/{accountId}/auto-response`
        """
        return _pick(self._request("PUT", f"/api/mail/accounts/{_seg(account_id)}/auto-response", query=None, body=body, multipart=False, options=options), "data.settings")  # type: ignore[no-any-return]

    def set_crm_sync(self, account_id: str, body: MailSetCrmSyncBody, *, options: Optional[RequestOptions] = None) -> MailSetCrmSyncResponseData:
        """Shows a mailbox's conversations in the CRM, or stops.
        
        Only the mailbox's owner; anybody else gets 404. Nothing is copied: in the CRM a conversation is shown only to those who may open the mailbox.
        
        `PUT /api/mail/accounts/{accountId}/crm`
        """
        return _pick(self._request("PUT", f"/api/mail/accounts/{_seg(account_id)}/crm", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_flags(self, email_id: str, body: MailSetFlagsBody, *, options: Optional[RequestOptions] = None) -> MailEmail:
        """Changes one message: read, starred, archived, trashed, folder or labels.
        
        Read and starred are set on the mail server too, and the conversation's unread count follows.
        
        `PATCH /api/mail/emails/{emailId}/flags`
        """
        return _pick(self._request("PATCH", f"/api/mail/emails/{_seg(email_id)}/flags", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_folders(self, account_id: str, body: MailSetFoldersBody, *, options: Optional[RequestOptions] = None) -> MailSetFoldersResponseData:
        """Chooses which of a mailbox's folders are synced.
        
        Only the mailbox's owner; anybody else gets 404.
        
        `PUT /api/mail/accounts/{accountId}/folders`
        """
        return _pick(self._request("PUT", f"/api/mail/accounts/{_seg(account_id)}/folders", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_retention(self, account_id: str, body: MailSetRetentionBody, *, options: Optional[RequestOptions] = None) -> MailSetRetentionResponseData:
        """Sets how many days a mailbox's mail is kept here.
        
        Only the mailbox's owner; anybody else gets 404. 0 keeps it for ever.
        
        `PATCH /api/mail/accounts/{accountId}/retention`
        """
        return _pick(self._request("PATCH", f"/api/mail/accounts/{_seg(account_id)}/retention", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def snooze_thread(self, thread_id: str, body: MailSnoozeThreadBody, *, options: Optional[RequestOptions] = None) -> MailSnoozeThreadResponseData:
        """Hides a conversation until a time, then brings it back unread to its folder.
        
        `POST /api/mail/threads/{threadId}/snooze`
        """
        return _pick(self._request("POST", f"/api/mail/threads/{_seg(thread_id)}/snooze", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def storage(self, *, options: Optional[RequestOptions] = None) -> MailStorageResponseData:
        """Where the caller's mail storage stands against the plan, and that of each organisation sharing a mailbox with them.
        
        `limitMb` -1 is unlimited. A full pool refuses new uploads; incoming mail still arrives.
        
        `GET /api/mail/storage`
        """
        return _pick(self._request("GET", f"/api/mail/storage", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def sync_account(self, id: str, body: MailSyncAccountBody, *, options: Optional[RequestOptions] = None) -> MailSyncAccountResponseData:
        """Starts a sync of a mailbox now, or asks for one folder to be synced.
        
        Without `folder`: the owner only, a full sync in the background (400 when sync is off). With `folder`: anybody who can open the mailbox; `syncing` says whether a sync was queued.
        
        `POST /api/mail/accounts/{id}/sync`
        """
        return _pick(self._request("POST", f"/api/mail/accounts/{_seg(id)}/sync", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def thread_document_html(self, thread_id: str, body: MailThreadDocumentHtmlBody, *, options: Optional[RequestOptions] = None) -> MailThreadDocumentHtmlResponseData:
        """Renders a conversation as the HTML of one document page, for saving it as a document.
        
        It only reads: the page is created with the documents API. The dates follow the caller's regional settings. 413 when the conversation is too long for one page.
        
        `POST /api/mail/threads/{threadId}/document-html`
        """
        return _pick(self._request("POST", f"/api/mail/threads/{_seg(thread_id)}/document-html", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def unblock_sender(self, id: str, *, options: Optional[RequestOptions] = None) -> MailUnblockSenderResponse:
        """Unblocks a sender; mail already in spam stays there.
        
        `DELETE /api/mail/blocked-senders/{id}`
        """
        return self._request("DELETE", f"/api/mail/blocked-senders/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def unsnooze_thread(self, thread_id: str, *, options: Optional[RequestOptions] = None) -> MailUnsnoozeThreadResponse:
        """Ends a conversation's snooze and puts it back in its folder.
        
        `DELETE /api/mail/threads/{threadId}/snooze`
        """
        return self._request("DELETE", f"/api/mail/threads/{_seg(thread_id)}/snooze", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def unsubscribe(self, email_id: str, *, options: Optional[RequestOptions] = None) -> MailUnsubscribeResponseData:
        """Unsubscribes from the list a message came from, in one click where the sender allows it.
        
        When the sender offers one-click unsubscribe over https it is done here (`unsubscribed: true`); otherwise the answer carries the page or address to use (`method: manual` or `link`). 404 when the message offers no way.
        
        `POST /api/mail/emails/{emailId}/unsubscribe`
        """
        return _pick(self._request("POST", f"/api/mail/emails/{_seg(email_id)}/unsubscribe", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_account(self, id: str, body: MailUpdateAccountBody, *, options: Optional[RequestOptions] = None) -> MailAccount:
        """Changes a mailbox's name, sender name, sharing, sync or servers and login.
        
        Only the mailbox's owner; anybody else gets 404. Only the fields sent change. A changed IMAP login is tried once before it is saved (400 with the reason when it fails); an empty password keeps the stored one. Sharing with the organisation needs the team inbox feature and room in the pool it moves to.
        
        `PUT /api/mail/accounts/{id}`
        """
        return _pick(self._request("PUT", f"/api/mail/accounts/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_draft(self, id: str, body: MailUpdateDraftBody, *, options: Optional[RequestOptions] = None) -> MailDraft:
        """Changes a draft of the caller's.
        
        Only the fields sent change.
        
        `PUT /api/mail/drafts/{id}`
        """
        return _pick(self._request("PUT", f"/api/mail/drafts/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_label(self, id: str, body: MailUpdateLabelBody, *, options: Optional[RequestOptions] = None) -> MailLabel:
        """Renames or recolours a label.
        
        A system label cannot be changed (400).
        
        `PUT /api/mail/labels/{id}`
        """
        return _pick(self._request("PUT", f"/api/mail/labels/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_pgp_key(self, id: str, body: MailUpdatePgpKeyBody, *, options: Optional[RequestOptions] = None) -> MailUpdatePgpKeyResponseDataKey:
        """Renames a PGP key or makes it the default.
        
        Needs PGP on the plan and `mail:manage_pgp_keys`.
        
        `PATCH /api/mail/pgp/keys/{id}`
        """
        return _pick(self._request("PATCH", f"/api/mail/pgp/keys/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data.key")  # type: ignore[no-any-return]

    def update_rule(self, id: str, body: MailUpdateRuleBody, *, options: Optional[RequestOptions] = None) -> MailRule:
        """Changes a rule.
        
        `PATCH /api/mail/rules/{id}`
        """
        return _pick(self._request("PATCH", f"/api/mail/rules/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data.rule")  # type: ignore[no-any-return]

    def update_signature(self, id: str, body: MailUpdateSignatureBody, *, options: Optional[RequestOptions] = None) -> MailSignature:
        """Changes a signature.
        
        Only the fields sent change; the HTML is sanitised.
        
        `PUT /api/mail/signatures/{id}`
        """
        return _pick(self._request("PUT", f"/api/mail/signatures/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_snippet(self, id: str, body: MailUpdateSnippetBody, *, options: Optional[RequestOptions] = None) -> MailSnippet:
        """Changes a snippet.
        
        `PATCH /api/mail/snippets/{id}`
        """
        return _pick(self._request("PATCH", f"/api/mail/snippets/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data.snippet")  # type: ignore[no-any-return]

    def upload_attachment(self, body: Union[MailUploadAttachmentBody, Dict[str, Any]], *, options: Optional[RequestOptions] = None) -> MailUploadAttachmentResponseData:
        """Uploads a file to attach to a message; send its id in `attachmentIds`.
        
        25 MB at most; executable types are refused (415). Counts against the plan's mail storage.
        
        `POST /api/mail/attachments/upload`
        """
        return _pick(self._request("POST", f"/api/mail/attachments/upload", query=None, body=body, multipart=True, options=options), "data")  # type: ignore[no-any-return]


class MarketplaceResource(_Resource):
    """Marketplace — Templates, workflows, blocks, files and services that sellers offer and organizations buy: browsing the storefront, free installs, orders and purchases, reviews, questions, disputes, and a seller's own shop, sales and payouts. The marketplace can be switched off for the whole platform; while it is, every operation here answers 403 `featureDisabledByAdmin`. Paid purchases happen in the dashboard, in the payment provider's form; a seller's offers are products of the Products hub (`products.marketplace.*`).
    """

    def accept_delivery(self, order_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceOrder:
        """Accepts a service delivery as the buyer, which completes the order.
        
        The seller's payout hold starts now.
        
        `POST /api/marketplace/orders/{orderId}/accept`
        """
        return _pick(self._request("POST", f"/api/marketplace/orders/{_seg(order_id)}/accept", query=None, body=None, multipart=False, options=options), "data.order")  # type: ignore[no-any-return]

    def add_dispute_evidence(self, dispute_id: str, body: MarketplaceAddDisputeEvidenceBody, *, options: Optional[RequestOptions] = None) -> MarketplaceAddDisputeEvidenceResponse:
        """Adds evidence to a dispute.
        
        Needs the dispute center on the platform (`marketplace_disputes`).
        
        `POST /api/marketplace/disputes/{disputeId}/evidence`
        """
        return self._request("POST", f"/api/marketplace/disputes/{_seg(dispute_id)}/evidence", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def add_to_wishlist(self, body: MarketplaceAddToWishlistBody, *, options: Optional[RequestOptions] = None) -> MarketplaceAddToWishlistResponse:
        """Puts a listing on the caller's wishlist.
        
        `POST /api/marketplace/wishlist`
        """
        return self._request("POST", f"/api/marketplace/wishlist", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def answer_question(self, listing_id: str, body: MarketplaceAnswerQuestionBody, *, options: Optional[RequestOptions] = None) -> MarketplaceQuestion:
        """Answers a question about the caller's listing, which publishes it, or hides an abusive one.
        
        The seller: the shop's owner or a holder of `marketplace:sell` in the listing's organization.
        
        `PATCH /api/marketplace/{listingId}/questions`
        """
        return _pick(self._request("PATCH", f"/api/marketplace/{_seg(listing_id)}/questions", query=None, body=body, multipart=False, options=options), "data.question")  # type: ignore[no-any-return]

    def ask_question(self, listing_id: str, body: MarketplaceAskQuestionBody, *, options: Optional[RequestOptions] = None) -> MarketplaceQuestion:
        """Asks the seller a question about a listing.
        
        Not the listing's own seller. Five questions an hour.
        
        `POST /api/marketplace/{listingId}/questions`
        """
        return _pick(self._request("POST", f"/api/marketplace/{_seg(listing_id)}/questions", query=None, body=body, multipart=False, options=options), "data.question")  # type: ignore[no-any-return]

    def built_with(self, listing_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[MarketplaceBuiltWithResponseDataSitesItem]:
        """Lists up to six live sites made with a listing whose owners agreed to be shown.
        
        `GET /api/marketplace/{listingId}/built-with`
        """
        return _pick(self._request("GET", f"/api/marketplace/{_seg(listing_id)}/built-with", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.sites")  # type: ignore[no-any-return]

    def cancel_dispute(self, dispute_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceCancelDisputeResponse:
        """Withdraws a dispute as its buyer; the order returns to where it was.
        
        Needs the dispute center on the platform (`marketplace_disputes`).
        
        `POST /api/marketplace/disputes/{disputeId}/cancel`
        """
        return self._request("POST", f"/api/marketplace/disputes/{_seg(dispute_id)}/cancel", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def cancel_seller_order(self, order_id: str, body: MarketplaceCancelSellerOrderBody, *, options: Optional[RequestOptions] = None) -> MarketplaceCancelSellerOrderResponseData:
        """Cancels a service order before delivery as its seller, refunding the buyer.
        
        Only a service that is `ordered` or `in_progress`. The seller's share is not paid out, or comes off the next payout.
        
        `POST /api/marketplace/seller/orders/{orderId}/cancel`
        """
        return _pick(self._request("POST", f"/api/marketplace/seller/orders/{_seg(order_id)}/cancel", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def cancel_subscription(self, subscription_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceCancelSubscriptionResponseData:
        """Cancels a subscription the caller bought at the end of its paid period.
        
        Repeating it answers `alreadyCancelling: true`.
        
        `DELETE /api/marketplace/subscriptions/{subscriptionId}`
        """
        return _pick(self._request("DELETE", f"/api/marketplace/subscriptions/{_seg(subscription_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def categories(self, *, options: Optional[RequestOptions] = None) -> List[MarketplaceCategoriesResponseDataCategoriesItem]:
        """Lists the marketplace's categories in the storefront's order, with how many listings the caller can see in each.
        
        `GET /api/marketplace/categories`
        """
        return _pick(self._request("GET", f"/api/marketplace/categories", query=None, body=None, multipart=False, options=options), "data.categories")  # type: ignore[no-any-return]

    def create_coupon(self, body: MarketplaceCreateCouponBody, *, options: Optional[RequestOptions] = None) -> MarketplaceCoupon:
        """Creates a coupon for the caller's listings, or for one of them.
        
        409 when the code exists already.
        
        `POST /api/marketplace/coupons`
        """
        return _pick(self._request("POST", f"/api/marketplace/coupons", query=None, body=body, multipart=False, options=options), "data.coupon")  # type: ignore[no-any-return]

    def create_review(self, listing_id: str, body: MarketplaceCreateReviewBody, *, options: Optional[RequestOptions] = None) -> MarketplaceReview:
        """Reviews a listing.
        
        One review per person and listing, never of one's own. Five reviews an hour.
        
        `POST /api/marketplace/{listingId}/reviews`
        """
        return _pick(self._request("POST", f"/api/marketplace/{_seg(listing_id)}/reviews", query=None, body=body, multipart=False, options=options), "data.review")  # type: ignore[no-any-return]

    def create_seller_listing(self, body: MarketplaceCreateSellerListingBody, *, options: Optional[RequestOptions] = None) -> MarketplaceCreateSellerListingResponseData:
        """Starts a new offer: creates a product of the shop's organization with its marketplace offer filled in.
        
        The offer is finished and submitted for review from the product (`products.marketplace.*`).
        
        `POST /api/marketplace/seller/listings`
        """
        return _pick(self._request("POST", f"/api/marketplace/seller/listings", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_seller_profile(self, body: MarketplaceCreateSellerProfileBody, *, options: Optional[RequestOptions] = None) -> MarketplaceSellerProfile:
        """Opens a shop: creates the caller's seller profile.
        
        One per person (409 otherwise). The shop's slug is made from the name. Being paid out needs the payout account, set up in the dashboard.
        
        `POST /api/marketplace/seller`
        """
        return _pick(self._request("POST", f"/api/marketplace/seller", query=None, body=body, multipart=False, options=options), "data.profile")  # type: ignore[no-any-return]

    def delete_coupon(self, *, id: str, options: Optional[RequestOptions] = None) -> MarketplaceDeleteCouponResponse:
        """Deletes one of the caller's coupons.
        
        `DELETE /api/marketplace/coupons`
        """
        return self._request("DELETE", f"/api/marketplace/coupons", query={"id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_review(self, listing_id: str, *, review_id: str, options: Optional[RequestOptions] = None) -> MarketplaceDeleteReviewResponse:
        """Deletes the caller's review of a listing.
        
        `DELETE /api/marketplace/{listingId}/reviews`
        """
        return self._request("DELETE", f"/api/marketplace/{_seg(listing_id)}/reviews", query={"reviewId": review_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_seller_listing(self, listing_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceDeleteSellerListingResponse:
        """Deletes one of the caller's listings that has no open or completed orders.
        
        `DELETE /api/marketplace/seller/listings/{listingId}`
        """
        return self._request("DELETE", f"/api/marketplace/seller/listings/{_seg(listing_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def deliver_order(self, order_id: str, body: MarketplaceDeliverOrderBody, *, options: Optional[RequestOptions] = None) -> MarketplaceOrder:
        """Delivers a service order as the seller.
        
        The shop's owner, or a member of the selling organization with `products:update`.
        
        `POST /api/marketplace/orders/{orderId}/deliver`
        """
        return _pick(self._request("POST", f"/api/marketplace/orders/{_seg(order_id)}/deliver", query=None, body=body, multipart=False, options=options), "data.order")  # type: ignore[no-any-return]

    def download(self, listing_id: str, body: MarketplaceDownloadBody, *, options: Optional[RequestOptions] = None) -> List[MarketplaceDownloadResponseDataFilesItem]:
        """Lists the files of a listing the caller bought, with their download links.
        
        For a buyer with access, or the listing's seller. Without `versionId`, the newest version's files.
        
        `POST /api/marketplace/{listingId}/download`
        """
        return _pick(self._request("POST", f"/api/marketplace/{_seg(listing_id)}/download", query=None, body=body, multipart=False, options=options), "data.files")  # type: ignore[no-any-return]

    def escalate_dispute(self, dispute_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceEscalateDisputeResponse:
        """Hands a dispute to the platform's mediator.
        
        Needs the dispute center on the platform (`marketplace_disputes`). Buyer or seller; repeating it does nothing.
        
        `POST /api/marketplace/disputes/{disputeId}/escalate`
        """
        return self._request("POST", f"/api/marketplace/disputes/{_seg(dispute_id)}/escalate", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def follow_shop(self, slug: str, *, options: Optional[RequestOptions] = None) -> MarketplaceFollowShopResponseData:
        """Follows a shop.
        
        `POST /api/marketplace/shop/{slug}/follow`
        """
        return _pick(self._request("POST", f"/api/marketplace/shop/{_seg(slug)}/follow", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, listing_id: str, *, organization_id: Optional[str] = None, buyer_country: Optional[str] = None, confirmed_country: Optional[str] = None, buyer_is_business: Optional[Literal["1"]] = None, buyer_vat_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MarketplaceGetResponseData:
        """Returns a listing's product page: details, tiers priced for the caller, reviews, the seller's legal pages and what the checkout would charge.
        
        `checkout.vat` tells how VAT would apply to this buyer; when the evidence of the buyer's country conflicts or is missing it answers `ok: false` with `marketplaceCountryConflict` or `marketplaceCountryRequired`, to be settled with `confirmedCountry` or `buyerCountry`.
        
        `GET /api/marketplace/{listingId}`
        """
        return _pick(self._request("GET", f"/api/marketplace/{_seg(listing_id)}", query={"organizationId": organization_id, "buyerCountry": buyer_country, "confirmedCountry": confirmed_country, "buyerIsBusiness": buyer_is_business, "buyerVatId": buyer_vat_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_collection(self, slug: str, *, organization_id: Optional[str] = None, lang: Optional[str] = None, options: Optional[RequestOptions] = None) -> MarketplaceGetCollectionResponseDataCollection:
        """Returns a published collection with its listings in the curator's order, each with the curator's note.
        
        `GET /api/marketplace/collections/{slug}`
        """
        return _pick(self._request("GET", f"/api/marketplace/collections/{_seg(slug)}", query={"organizationId": organization_id, "lang": lang}, body=None, multipart=False, options=options), "data.collection")  # type: ignore[no-any-return]

    def get_dispute(self, dispute_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceGetDisputeResponseData:
        """Returns a dispute with its messages, evidence, history and order.
        
        Needs the dispute center on the platform (`marketplace_disputes`).
        
        `GET /api/marketplace/disputes/{disputeId}`
        """
        return _pick(self._request("GET", f"/api/marketplace/disputes/{_seg(dispute_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_fees(self, *, options: Optional[RequestOptions] = None) -> MarketplaceGetFeesResponse:
        """Returns the platform's commission and payout terms for sellers.
        
        `GET /api/marketplace/fees`
        """
        return self._request("GET", f"/api/marketplace/fees", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_file(self, listing_id: str, file_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Downloads one file of a listing the caller bought.
        
        For a buyer with access, or the listing's seller. 60 downloads an hour; a tier's download cap applies (403 when reached).
        
        `GET /api/marketplace/{listingId}/files/{fileId}`
        """
        return self._request("GET", f"/api/marketplace/{_seg(listing_id)}/files/{_seg(file_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_order(self, order_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceGetOrderResponseData:
        """Returns one marketplace order of the caller, as buyer or seller.
        
        `GET /api/marketplace/orders/{orderId}`
        """
        return _pick(self._request("GET", f"/api/marketplace/orders/{_seg(order_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_seller_listing(self, listing_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceGetSellerListingResponseData:
        """Returns one of the caller's listings with its versions and files.
        
        `GET /api/marketplace/seller/listings/{listingId}`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller/listings/{_seg(listing_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_seller_profile(self, *, options: Optional[RequestOptions] = None) -> MarketplaceSellerProfile:
        """Returns the caller's seller profile, or null.
        
        `GET /api/marketplace/seller`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller", query=None, body=None, multipart=False, options=options), "data.profile")  # type: ignore[no-any-return]

    def get_shop(self, slug: str, *, options: Optional[RequestOptions] = None) -> MarketplaceGetShopResponseData:
        """Returns a seller's shop: its header with rating and trader information, its standing and its listings.
        
        The shop's listings are better browsed with GET /api/marketplace?seller={slug}, which filters and pages.
        
        `GET /api/marketplace/shop/{slug}`
        """
        return _pick(self._request("GET", f"/api/marketplace/shop/{_seg(slug)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_showcase(self, order_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceGetShowcaseResponseData:
        """Lists the projects a purchase installed, whether each is live, and whether the product page may show it.
        
        `GET /api/marketplace/purchases/{orderId}/showcase`
        """
        return _pick(self._request("GET", f"/api/marketplace/purchases/{_seg(order_id)}/showcase", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_subscriptions(self, *, options: Optional[RequestOptions] = None) -> List[MarketplaceGetSubscriptionsResponseDataSubscriptionsItem]:
        """Lists the caller's subscriptions to sellers' former subscription tiers.
        
        An offer sold by subscription is a purchase; see GET /api/marketplace/purchases.
        
        `GET /api/marketplace/subscriptions`
        """
        return _pick(self._request("GET", f"/api/marketplace/subscriptions", query=None, body=None, multipart=False, options=options), "data.subscriptions")  # type: ignore[no-any-return]

    def hard_delete_seller_listing(self, listing_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceHardDeleteSellerListingResponse:
        """Removes one of the caller's listings for good, for an erasure request.
        
        Only a listing that never had an order; past sales are kept for tax and disputes.
        
        `DELETE /api/marketplace/seller/listings/{listingId}/hard-delete`
        """
        return self._request("DELETE", f"/api/marketplace/seller/listings/{_seg(listing_id)}/hard-delete", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def hide_from_showcase(self, order_id: str, *, project_id: str, options: Optional[RequestOptions] = None) -> MarketplaceHideFromShowcaseResponseData:
        """Stops showing a project under "Built with this".
        
        `DELETE /api/marketplace/purchases/{orderId}/showcase`
        """
        return _pick(self._request("DELETE", f"/api/marketplace/purchases/{_seg(order_id)}/showcase", query={"projectId": project_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def install(self, listing_id: str, body: MarketplaceInstallBody, *, options: Optional[RequestOptions] = None) -> MarketplaceInstallResponseData:
        """Takes a free listing or a free tier: records an order without a payment.
        
        Installing it into a workspace is POST /api/marketplace/orders/{orderId}/install. A paid listing is bought in the dashboard.
        
        `POST /api/marketplace/{listingId}/install`
        """
        return _pick(self._request("POST", f"/api/marketplace/{_seg(listing_id)}/install", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def install_all(self, order_id: str, body: MarketplaceInstallAllBody, *, options: Optional[RequestOptions] = None) -> List[MarketplaceInstallAllResponseDataResultsItem]:
        """Installs every item of a bundle purchase into one workspace.
        
        Each item answers `installed`, `skipped` (`download`: files are downloaded; `alreadyInstalled`) or `failed` with the reason.
        
        `POST /api/marketplace/orders/{orderId}/install-all`
        """
        return _pick(self._request("POST", f"/api/marketplace/orders/{_seg(order_id)}/install-all", query=None, body=body, multipart=False, options=options), "data.results")  # type: ignore[no-any-return]

    def install_order(self, order_id: str, body: MarketplaceInstallOrderBody, *, options: Optional[RequestOptions] = None) -> MarketplaceInstallResult:
        """Installs what an order bought into a workspace of the organization it was bought for.
        
        Only the buyer, while the order gives access, into a workspace where they may create the resource. The newest version the order includes unless `versionId`; installing again makes a new copy. A digital asset answers its download links; a service has nothing to install.
        
        `POST /api/marketplace/orders/{orderId}/install`
        """
        return _pick(self._request("POST", f"/api/marketplace/orders/{_seg(order_id)}/install", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def install_to_workspace(self, listing_id: str, body: MarketplaceInstallToWorkspaceBody, *, options: Optional[RequestOptions] = None) -> MarketplaceInstallToWorkspaceResponseData:
        """Installs a listing the caller owns into a workspace, from their newest order that gives access.
        
        The same as POST /api/marketplace/orders/{orderId}/install with that order. The workspace must belong to the organization the purchase was made for.
        
        `POST /api/marketplace/{listingId}/install-to-workspace`
        """
        return _pick(self._request("POST", f"/api/marketplace/{_seg(listing_id)}/install-to-workspace", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, q: Optional[str] = None, category: Optional[str] = None, delivers: Optional[str] = None, kind: Optional[Literal["digital", "service"]] = None, pricing: Optional[Literal["free", "paid"]] = None, price_min: Optional[int] = None, price_max: Optional[int] = None, min_rating: Optional[int] = None, seller: Optional[str] = None, featured: Optional[bool] = None, wishlist: Optional[bool] = None, following: Optional[bool] = None, sort: Optional[Literal["relevance", "popular", "rating", "newest", "price_asc", "price_desc"]] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> MarketplaceListResponseData:
        """Browses the storefront: approved listings the caller may see, filtered, ranked and paged, with facets.
        
        `relevance` ranks by how well the search matches, sales, rating and recency; featured listings do not rank higher. Unknown filter values are ignored rather than refused.
        
        `GET /api/marketplace`
        """
        return _pick(self._request("GET", f"/api/marketplace", query={"organizationId": organization_id, "q": q, "category": category, "delivers": delivers, "kind": kind, "pricing": pricing, "priceMin": price_min, "priceMax": price_max, "minRating": min_rating, "seller": seller, "featured": featured, "wishlist": wishlist, "following": following, "sort": sort, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_collections(self, *, featured: Optional[bool] = None, lang: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[MarketplaceListCollectionsResponseDataCollectionsItem]:
        """Lists the published collections that hold at least one listing the caller can see.
        
        `GET /api/marketplace/collections`
        """
        return _pick(self._request("GET", f"/api/marketplace/collections", query={"featured": featured, "lang": lang}, body=None, multipart=False, options=options), "data.collections")  # type: ignore[no-any-return]

    def list_coupons(self, *, options: Optional[RequestOptions] = None) -> List[MarketplaceCoupon]:
        """Lists the caller's coupons as a seller.
        
        `GET /api/marketplace/coupons`
        """
        return _pick(self._request("GET", f"/api/marketplace/coupons", query=None, body=None, multipart=False, options=options), "data.coupons")  # type: ignore[no-any-return]

    def list_disputes(self, *, role: Optional[Literal["buyer", "seller"]] = None, status: Optional[MarketplaceDisputeStatus] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the disputes the caller is part of, as buyer, as seller or both.
        
        Needs the dispute center on the platform (`marketplace_disputes`).
        
        `GET /api/marketplace/disputes`
        """
        return _pick(self._request("GET", f"/api/marketplace/disputes", query={"role": role, "status": status}, body=None, multipart=False, options=options), "data.disputes")  # type: ignore[no-any-return]

    def list_legal_pages(self, *, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Lists the caller's shop legal pages: terms, return policy, privacy policy and imprint.
        
        `GET /api/marketplace/seller/legal-pages`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller/legal-pages", query=None, body=None, multipart=False, options=options), "data.legalPages")  # type: ignore[no-any-return]

    def list_order_disputes(self, order_id: str, *, options: Optional[RequestOptions] = None) -> List[MarketplaceListOrderDisputesResponseDataDisputesItem]:
        """Lists the disputes of an order the caller bought or sold.
        
        Needs the dispute center on the platform (`marketplace_disputes`).
        
        `GET /api/marketplace/orders/{orderId}/disputes`
        """
        return _pick(self._request("GET", f"/api/marketplace/orders/{_seg(order_id)}/disputes", query=None, body=None, multipart=False, options=options), "data.disputes")  # type: ignore[no-any-return]

    def list_orders(self, *, role: Optional[Literal["buyer", "seller"]] = None, options: Optional[RequestOptions] = None) -> List[MarketplaceListOrdersResponseDataOrdersItem]:
        """Lists the caller's marketplace orders as buyer or as seller, newest first.
        
        `GET /api/marketplace/orders`
        """
        return _pick(self._request("GET", f"/api/marketplace/orders", query={"role": role}, body=None, multipart=False, options=options), "data.orders")  # type: ignore[no-any-return]

    def list_payouts(self, *, days: Optional[int] = None, format: Optional[Literal["json", "csv"]] = None, options: Optional[RequestOptions] = None) -> MarketplaceListPayoutsResponseData:
        """Lists the caller's payouts over a period, with totals; or downloads them as CSV.
        
        `GET /api/marketplace/seller/payouts`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller/payouts", query={"days": days, "format": format}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_purchases(self, *, options: Optional[RequestOptions] = None) -> List[MarketplacePurchase]:
        """Lists everything the caller bought: tier, price, access, installed version and available update, licence and invoices.
        
        `GET /api/marketplace/purchases`
        """
        return _pick(self._request("GET", f"/api/marketplace/purchases", query=None, body=None, multipart=False, options=options), "data.purchases")  # type: ignore[no-any-return]

    def list_questions(self, listing_id: str, *, options: Optional[RequestOptions] = None) -> MarketplaceListQuestionsResponseData:
        """Lists a listing's answered questions and the caller's own open ones; for the seller, every open one.
        
        `GET /api/marketplace/{listingId}/questions`
        """
        return _pick(self._request("GET", f"/api/marketplace/{_seg(listing_id)}/questions", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_reviews(self, listing_id: str, *, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> MarketplaceListReviewsResponseData:
        """Lists a listing's visible reviews, newest first.
        
        `GET /api/marketplace/{listingId}/reviews`
        """
        return _pick(self._request("GET", f"/api/marketplace/{_seg(listing_id)}/reviews", query={"limit": limit, "offset": offset}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_sales(self, *, options: Optional[RequestOptions] = None) -> MarketplaceListSalesResponseData:
        """Lists the orders on the caller's listings with buyer and listing, and totals.
        
        `GET /api/marketplace/seller/sales`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller/sales", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_seller_listings(self, *, options: Optional[RequestOptions] = None) -> List[MarketplaceSellerListing]:
        """Lists the caller's own listings, newest first.
        
        `GET /api/marketplace/seller/listings`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller/listings", query=None, body=None, multipart=False, options=options), "data.listings")  # type: ignore[no-any-return]

    def list_wishlist(self, *, options: Optional[RequestOptions] = None) -> List[MarketplaceListWishlistResponseDataItemsItem]:
        """Lists the caller's wishlist, newest first.
        
        `GET /api/marketplace/wishlist`
        """
        return _pick(self._request("GET", f"/api/marketplace/wishlist", query=None, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def offer_resource(self, body: MarketplaceOfferResourceBody, *, options: Optional[RequestOptions] = None) -> MarketplaceOfferResourceResponseData:
        """Offers a project, workflow, database or endpoint in the marketplace: creates (or finds) its product with the offer filled in.
        
        Needs `products:create` and `marketplace:sell` in the resource's organization, the marketplace on the plan, and the right to change the resource. The offer is finished and submitted from the product.
        
        `POST /api/marketplace/seller/listings/publish`
        """
        return _pick(self._request("POST", f"/api/marketplace/seller/listings/publish", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def open_dispute(self, order_id: str, body: MarketplaceOpenDisputeBody, *, options: Optional[RequestOptions] = None) -> MarketplaceOpenDisputeResponseData:
        """Opens a dispute about an order as its buyer.
        
        Needs the dispute center on the platform (`marketplace_disputes`).
        
        `POST /api/marketplace/orders/{orderId}/disputes`
        """
        return _pick(self._request("POST", f"/api/marketplace/orders/{_seg(order_id)}/disputes", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def order_service(self, body: MarketplaceOrderServiceBody, *, options: Optional[RequestOptions] = None) -> MarketplaceOrder:
        """Orders a free service; a paid one is bought in the dashboard.
        
        `POST /api/marketplace/orders`
        """
        return _pick(self._request("POST", f"/api/marketplace/orders", query=None, body=body, multipart=False, options=options), "data.order")  # type: ignore[no-any-return]

    def payout_schedule(self, *, options: Optional[RequestOptions] = None) -> MarketplacePayoutScheduleResponseData:
        """Tells the caller when they will be paid: what may be paid out now, what is still held, and the next payout date.
        
        `GET /api/marketplace/seller/payout-schedule`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller/payout-schedule", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def preview(self, listing_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Returns what a read-only "Try it live" preview of an approved listing shows: a site's pages or a workflow's steps.
        
        `preview` is null for a listing with nothing to preview (a database, an endpoint, files, a service). 60 previews in ten minutes per person.
        
        `GET /api/marketplace/{listingId}/preview`
        """
        return _pick(self._request("GET", f"/api/marketplace/{_seg(listing_id)}/preview", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.preview")  # type: ignore[no-any-return]

    def refund_order(self, order_id: str, body: MarketplaceRefundOrderBody, *, options: Optional[RequestOptions] = None) -> MarketplaceRefundOrderResponseData:
        """Refunds an order, fully or partly, as a goodwill gesture of its seller.
        
        Not for an order already refunded, disputed or cancelled. A full refund marks the order `refunded`; the refunded share comes off what the seller is owed. A bundle is refunded as a whole.
        
        `POST /api/marketplace/seller/orders/{orderId}/refund`
        """
        return _pick(self._request("POST", f"/api/marketplace/seller/orders/{_seg(order_id)}/refund", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_from_wishlist(self, *, listing_id: str, options: Optional[RequestOptions] = None) -> MarketplaceRemoveFromWishlistResponse:
        """Takes a listing off the caller's wishlist.
        
        `DELETE /api/marketplace/wishlist`
        """
        return self._request("DELETE", f"/api/marketplace/wishlist", query={"listingId": listing_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def report_listing(self, listing_id: str, body: MarketplaceReportListingBody, *, options: Optional[RequestOptions] = None) -> MarketplaceReportListingResponseData:
        """Reports a listing to the platform for review.
        
        Reporting the same listing again answers `duplicate: true`.
        
        `POST /api/marketplace/listings/{listingId}/report`
        """
        return _pick(self._request("POST", f"/api/marketplace/listings/{_seg(listing_id)}/report", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def request_revision(self, order_id: str, body: MarketplaceRequestRevisionBody, *, options: Optional[RequestOptions] = None) -> MarketplaceOrder:
        """Asks the seller to revise a service delivery, while the included revisions last.
        
        `POST /api/marketplace/orders/{orderId}/revision`
        """
        return _pick(self._request("POST", f"/api/marketplace/orders/{_seg(order_id)}/revision", query=None, body=body, multipart=False, options=options), "data.order")  # type: ignore[no-any-return]

    def sales_report(self, *, days: Optional[int] = None, format: Optional[Literal["json", "csv"]] = None, options: Optional[RequestOptions] = None) -> MarketplaceSalesReportResponseData:
        """Returns the caller's revenue and orders per day and currency over a period; or downloads it as CSV.
        
        `GET /api/marketplace/seller/sales-report`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller/sales-report", query={"days": days, "format": format}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def save_legal_page(self, body: MarketplaceSaveLegalPageBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Creates or changes one of the caller's shop legal pages.
        
        `PUT /api/marketplace/seller/legal-pages`
        """
        return _pick(self._request("PUT", f"/api/marketplace/seller/legal-pages", query=None, body=body, multipart=False, options=options), "data.legalPage")  # type: ignore[no-any-return]

    def seller_usage(self, *, options: Optional[RequestOptions] = None) -> MarketplaceSellerUsageResponseData:
        """Returns the selling organization's marketplace limits and what is used.
        
        `-1` means no limit; without a selling organization every limit is 0.
        
        `GET /api/marketplace/seller/usage`
        """
        return _pick(self._request("GET", f"/api/marketplace/seller/usage", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def send_dispute_message(self, dispute_id: str, body: MarketplaceSendDisputeMessageBody, *, options: Optional[RequestOptions] = None) -> MarketplaceSendDisputeMessageResponse:
        """Sends a message on a dispute.
        
        Needs the dispute center on the platform (`marketplace_disputes`).
        
        `POST /api/marketplace/disputes/{disputeId}/messages`
        """
        return self._request("POST", f"/api/marketplace/disputes/{_seg(dispute_id)}/messages", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def send_order_message(self, order_id: str, body: MarketplaceSendOrderMessageBody, *, options: Optional[RequestOptions] = None) -> MarketplaceSendOrderMessageResponseData:
        """Sends a message on an order between buyer and seller.
        
        Not on a completed or cancelled order.
        
        `POST /api/marketplace/orders/{orderId}/messages`
        """
        return _pick(self._request("POST", f"/api/marketplace/orders/{_seg(order_id)}/messages", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def show_in_showcase(self, order_id: str, body: MarketplaceShowInShowcaseBody, *, options: Optional[RequestOptions] = None) -> MarketplaceShowInShowcaseResponseData:
        """Lets the listing's product page show a project the purchase installed under "Built with this".
        
        Only a project the order installed (422 `marketplaceShowcaseNotInstalled`); not for a refunded or cancelled order (422 `marketplaceShowcaseOrderVoid`).
        
        `POST /api/marketplace/purchases/{orderId}/showcase`
        """
        return _pick(self._request("POST", f"/api/marketplace/purchases/{_seg(order_id)}/showcase", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def unfollow_shop(self, slug: str, *, options: Optional[RequestOptions] = None) -> MarketplaceUnfollowShopResponseData:
        """Stops following a shop.
        
        `DELETE /api/marketplace/shop/{slug}/follow`
        """
        return _pick(self._request("DELETE", f"/api/marketplace/shop/{_seg(slug)}/follow", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_order_status(self, order_id: str, body: MarketplaceUpdateOrderStatusBody, *, options: Optional[RequestOptions] = None) -> MarketplaceOrder:
        """Moves a service order to its next status.
        
        The seller moves `ordered` → `in_progress` → `delivered` (and back to `in_progress` after a revision request) and `accepted` → `completed`; the buyer moves `delivered` → `accepted` or `revision_requested`. Cancelling is POST /api/marketplace/seller/orders/{orderId}/cancel, which refunds.
        
        `PUT /api/marketplace/orders/{orderId}`
        """
        return _pick(self._request("PUT", f"/api/marketplace/orders/{_seg(order_id)}", query=None, body=body, multipart=False, options=options), "data.order")  # type: ignore[no-any-return]

    def update_review(self, listing_id: str, body: MarketplaceUpdateReviewBody, *, options: Optional[RequestOptions] = None) -> MarketplaceReview:
        """Changes the caller's review of a listing.
        
        `PUT /api/marketplace/{listingId}/reviews`
        """
        return _pick(self._request("PUT", f"/api/marketplace/{_seg(listing_id)}/reviews", query=None, body=body, multipart=False, options=options), "data.review")  # type: ignore[no-any-return]

    def update_seller_listing(self, listing_id: str, body: MarketplaceUpdateSellerListingBody, *, options: Optional[RequestOptions] = None) -> MarketplaceSellerListing:
        """Changes a draft or rejected listing from before offers became products.
        
        A listing made from a product, or an approved one, answers 410 `marketplaceListingEditedInProducts` with its `productId`: change it through the product's offer.
        
        `PUT /api/marketplace/seller/listings/{listingId}`
        """
        return _pick(self._request("PUT", f"/api/marketplace/seller/listings/{_seg(listing_id)}", query=None, body=body, multipart=False, options=options), "data.listing")  # type: ignore[no-any-return]

    def update_seller_profile(self, body: MarketplaceUpdateSellerProfileBody, *, options: Optional[RequestOptions] = None) -> MarketplaceSellerProfile:
        """Changes the caller's seller profile.
        
        Only the fields sent change.
        
        `PUT /api/marketplace/seller`
        """
        return _pick(self._request("PUT", f"/api/marketplace/seller", query=None, body=body, multipart=False, options=options), "data.profile")  # type: ignore[no-any-return]

    def upload_dispute_attachment(self, dispute_id: str, body: Union[MarketplaceUploadDisputeAttachmentBody, Dict[str, Any]], *, options: Optional[RequestOptions] = None) -> MarketplaceUploadDisputeAttachmentResponseDataAttachment:
        """Uploads a file to a dispute as evidence.
        
        Multipart with `file`: at most 10 MB, images, PDF, ZIP and a few other document types.
        
        `POST /api/marketplace/disputes/{disputeId}/attachments`
        """
        return _pick(self._request("POST", f"/api/marketplace/disputes/{_seg(dispute_id)}/attachments", query=None, body=body, multipart=True, options=options), "data.attachment")  # type: ignore[no-any-return]

    def validate_coupon(self, body: MarketplaceValidateCouponBody, *, options: Optional[RequestOptions] = None) -> MarketplaceValidateCouponResponseData:
        """Checks a coupon code against a listing and returns the discount it would give.
        
        `POST /api/marketplace/coupons/validate`
        """
        return _pick(self._request("POST", f"/api/marketplace/coupons/validate", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class MessengerResource(_Resource):
    """Messenger — Team chat: channels, direct messages, threads, reactions and presence. Every operation needs the Messenger feature on the caller's plan.
    """

    def add_member(self, channel_id: str, body: MessengerAddMemberBody, *, options: Optional[RequestOptions] = None) -> MessengerChannelMember:
        """Adds a person to a channel, or joins the caller to a public channel.
        
        Adding somebody else is for the channel's owners and admins, and only a person who shares an organization with the caller or has a public profile. Counts against the plan's `max_messenger_members_per_channel`. Adding a member twice returns the existing membership.
        
        `POST /api/messenger/channels/{channelId}/members`
        """
        return _pick(self._request("POST", f"/api/messenger/channels/{_seg(channel_id)}/members", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def add_reaction(self, message_id: str, body: MessengerAddReactionBody, *, options: Optional[RequestOptions] = None) -> MessengerAddReactionResponseData:
        """Toggles the caller's reaction on a message.
        
        A person has one reaction per message: a different emoji replaces theirs, the same one removes it.
        
        `POST /api/messenger/messages/{messageId}/reactions`
        """
        return _pick(self._request("POST", f"/api/messenger/messages/{_seg(message_id)}/reactions", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def ai_draft(self, body: MessengerAiDraftBody, *, options: Optional[RequestOptions] = None) -> str:
        """Drafts a message or an answer for a channel with the platform's AI, from the channel's last 20 messages.
        
        Needs `messenger.use_ai`, membership of the channel and the `messaging:ai_compose` feature; counts against the organization's AI quota. At most 20 calls in five minutes. Nothing is sent — the text comes back for the caller to post.
        
        `POST /api/messenger/ai`
        """
        return _pick(self._request("POST", f"/api/messenger/ai", query=None, body=body, multipart=False, options=options), "data.text")  # type: ignore[no-any-return]

    def create_channel(self, body: MessengerCreateChannelBody, *, options: Optional[RequestOptions] = None) -> MessengerChannel:
        """Creates a channel; the caller becomes its owner.
        
        Needs the Channels feature; counts against the plan's `max_messenger_channels`; at most 20 an hour. A `workspace` channel needs `workspaceId`, an `organization` or `public` one an organization (given, or the workspace's).
        
        `POST /api/messenger/channels`
        """
        return _pick(self._request("POST", f"/api/messenger/channels", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_channel_webhook(self, channel_id: str, body: MessengerCreateChannelWebhookBody, *, options: Optional[RequestOptions] = None) -> MessengerCreateChannelWebhookResponseData:
        """Creates an incoming or outgoing webhook for a channel.
        
        The channel's owners and admins; needs the Messenger webhooks feature. The answer carries the secret `token` — for an incoming webhook the part of its URL that posts into the channel, for an outgoing one the key its calls are signed with.
        
        `POST /api/messenger/channels/{channelId}/webhooks`
        """
        return _pick(self._request("POST", f"/api/messenger/channels/{_seg(channel_id)}/webhooks", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_channel(self, id: str, *, options: Optional[RequestOptions] = None) -> MessengerDeleteChannelResponseData:
        """Deletes a channel with all its messages.
        
        The channel's owner only. It cannot be undone.
        
        `DELETE /api/messenger/channels/{id}`
        """
        return _pick(self._request("DELETE", f"/api/messenger/channels/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_channel_webhook(self, channel_id: str, webhook_id: str, *, options: Optional[RequestOptions] = None) -> MessengerDeleteChannelWebhookResponseData:
        """Deletes a channel's webhook.
        
        The channel's owners and admins; needs the Messenger webhooks feature.
        
        `DELETE /api/messenger/channels/{channelId}/webhooks/{webhookId}`
        """
        return _pick(self._request("DELETE", f"/api/messenger/channels/{_seg(channel_id)}/webhooks/{_seg(webhook_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_message(self, message_id: str, *, options: Optional[RequestOptions] = None) -> MessengerDeleteMessageResponseData:
        """Deletes a message.
        
        The sender, or the channel's owners and admins. The message stays in its thread as deleted, with its content removed.
        
        `DELETE /api/messenger/messages/{messageId}`
        """
        return _pick(self._request("DELETE", f"/api/messenger/messages/{_seg(message_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_channel(self, id: str, *, options: Optional[RequestOptions] = None) -> MessengerGetChannelResponseData:
        """Returns one channel with the caller's membership.
        
        A channel the caller is not in answers only if they could join it.
        
        `GET /api/messenger/channels/{id}`
        """
        return _pick(self._request("GET", f"/api/messenger/channels/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_e2_e(self, channel_id: str, *, options: Optional[RequestOptions] = None) -> MessengerGetE2EResponseData:
        """Returns whether a direct message is end-to-end encrypted, with both participants' public keys.
        
        Direct messages between two people only.
        
        `GET /api/messenger/channels/{channelId}/e2e`
        """
        return _pick(self._request("GET", f"/api/messenger/channels/{_seg(channel_id)}/e2e", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_presence(self, *, user_ids: str, options: Optional[RequestOptions] = None) -> List[MessengerPresence]:
        """Returns the presence of up to 200 people.
        
        A person who hides their presence from the caller shows as offline.
        
        `GET /api/messenger/presence`
        """
        return _pick(self._request("GET", f"/api/messenger/presence", query={"userIds": user_ids}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_settings(self, *, options: Optional[RequestOptions] = None) -> MessengerSettings:
        """Returns the caller's Messenger settings.
        
        `GET /api/messenger/settings`
        """
        return _pick(self._request("GET", f"/api/messenger/settings", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_unread(self, *, options: Optional[RequestOptions] = None) -> MessengerGetUnreadResponseData:
        """Returns how many of the caller's channels have unread messages.
        
        Channels, not messages. At most 60 calls a minute; beyond that, and without the Messenger feature, it answers 0.
        
        `GET /api/messenger/unread`
        """
        return _pick(self._request("GET", f"/api/messenger/unread", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_channels(self, *, workspace_id: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[MessengerChannelListItem]:
        """Lists the channels and DMs the caller is in, with the public channels they can join.
        
        Most recently active first, with the caller's unread count per channel.
        
        `GET /api/messenger/channels`
        """
        return _pick(self._request("GET", f"/api/messenger/channels", query={"workspaceId": workspace_id, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_channel_webhooks(self, channel_id: str, *, options: Optional[RequestOptions] = None) -> List[MessengerChannelWebhook]:
        """Lists a channel's incoming and outgoing webhooks.
        
        Members only; needs the Messenger webhooks feature. The secret token is never listed — see `messenger.revealChannelWebhook`.
        
        `GET /api/messenger/channels/{channelId}/webhooks`
        """
        return _pick(self._request("GET", f"/api/messenger/channels/{_seg(channel_id)}/webhooks", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_members(self, channel_id: str, *, options: Optional[RequestOptions] = None) -> List[MessengerListMembersResponseDataItem]:
        """Lists a channel's members with their presence.
        
        Members only. A member's email is shown only when they share an organization with the caller.
        
        `GET /api/messenger/channels/{channelId}/members`
        """
        return _pick(self._request("GET", f"/api/messenger/channels/{_seg(channel_id)}/members", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_messages(self, channel_id: str, *, before: Optional[str] = None, parent_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MessengerListMessagesResponseData:
        """Lists a channel's messages, or a thread's replies, 50 at a time, oldest first.
        
        Members only (or anyone who may join a public channel). Deleted messages are left out; a plan with a message-history limit hides older messages.
        
        `GET /api/messenger/channels/{channelId}/messages`
        """
        return _pick(self._request("GET", f"/api/messenger/channels/{_seg(channel_id)}/messages", query={"before": before, "parentId": parent_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_pinned(self, channel_id: str, *, options: Optional[RequestOptions] = None) -> MessengerListPinnedResponseData:
        """Lists a channel's pinned messages, most recently pinned first.
        
        `GET /api/messenger/channels/{channelId}/pinned`
        """
        return _pick(self._request("GET", f"/api/messenger/channels/{_seg(channel_id)}/pinned", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def lookup_users(self, *, q: str, options: Optional[RequestOptions] = None) -> List[MessengerLookupUsersResponseDataItem]:
        """Finds people the caller can message, by name or email.
        
        At least three characters; at most 20 results and 20 searches a minute. Only people with a public profile, or who share an organization with the caller.
        
        `GET /api/messenger/users`
        """
        return _pick(self._request("GET", f"/api/messenger/users", query={"q": q}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def mark_all_read(self, *, options: Optional[RequestOptions] = None) -> MessengerMarkAllReadResponseData:
        """Marks every channel the caller is in as read.
        
        `POST /api/messenger/read-all`
        """
        return _pick(self._request("POST", f"/api/messenger/read-all", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def mark_read(self, channel_id: str, body: MessengerMarkReadBody, *, options: Optional[RequestOptions] = None) -> MessengerMarkReadResponseData:
        """Marks a channel as read by the caller.
        
        Moves the caller's read position forward to the given message or time (default now); it never moves back. At most 120 a minute.
        
        `POST /api/messenger/channels/{channelId}/read`
        """
        return _pick(self._request("POST", f"/api/messenger/channels/{_seg(channel_id)}/read", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def open_dm(self, body: MessengerOpenDmBody, *, options: Optional[RequestOptions] = None) -> MessengerChannel:
        """Opens the direct message with one or more people, creating it the first time.
        
        Needs `messenger.use_dm` and the DMs feature; at most 30 an hour and eight other people. A person with a private profile, or one visible only within their organization the caller does not share, cannot be messaged.
        
        `POST /api/messenger/dms`
        """
        return _pick(self._request("POST", f"/api/messenger/dms", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def open_record_channel(self, body: MessengerOpenRecordChannelBody, *, options: Optional[RequestOptions] = None) -> MessengerOpenRecordChannelResponseData:
        """Opens the discussion channel of a database record, creating it the first time, and joins the caller to it.
        
        The caller needs access to the workspace and to the record.
        
        `POST /api/messenger/channels/record`
        """
        return _pick(self._request("POST", f"/api/messenger/channels/record", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def pin(self, message_id: str, *, options: Optional[RequestOptions] = None) -> MessengerPinResponseData:
        """Pins a message to its channel, or unpins it when it is pinned.
        
        Any member of the channel.
        
        `POST /api/messenger/messages/{messageId}/pin`
        """
        return _pick(self._request("POST", f"/api/messenger/messages/{_seg(message_id)}/pin", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_member(self, channel_id: str, *, user_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MessengerRemoveMemberResponseData:
        """Removes a person from a channel, or the caller leaves it.
        
        Removing somebody else is for the channel's owners and admins.
        
        `DELETE /api/messenger/channels/{channelId}/members`
        """
        return _pick(self._request("DELETE", f"/api/messenger/channels/{_seg(channel_id)}/members", query={"userId": user_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def reveal_channel_webhook(self, channel_id: str, webhook_id: str, *, options: Optional[RequestOptions] = None) -> MessengerRevealChannelWebhookResponseData:
        """Returns a channel webhook's secret token.
        
        The channel's owners and admins; at most 10 an hour, and every reveal is audit-logged.
        
        `POST /api/messenger/channels/{channelId}/webhooks/{webhookId}/reveal`
        """
        return _pick(self._request("POST", f"/api/messenger/channels/{_seg(channel_id)}/webhooks/{_seg(webhook_id)}/reveal", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def search(self, *, q: str, channel_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MessengerSearchResponseData:
        """Searches the messages of the caller's channels, newest first.
        
        A substring match, at most 50 results; at most 20 searches a minute.
        
        `GET /api/messenger/search`
        """
        return _pick(self._request("GET", f"/api/messenger/search", query={"q": q, "channelId": channel_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def send_message(self, channel_id: str, body: MessengerSendMessageBody, *, options: Optional[RequestOptions] = None) -> MessengerMessage:
        """Posts a message to a channel, or a reply to a thread.
        
        Members only; in an announcement channel, its owners and admins. At most 60 a minute and 10,000 characters. Attachments need the file-sharing feature. Mentions of people who are not members are dropped. A message the content filter blocks answers 422.
        
        `POST /api/messenger/channels/{channelId}/messages`
        """
        return _pick(self._request("POST", f"/api/messenger/channels/{_seg(channel_id)}/messages", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_e2_e_enabled(self, channel_id: str, body: MessengerSetE2EEnabledBody, *, options: Optional[RequestOptions] = None) -> MessengerSetE2EEnabledResponseData:
        """Turns end-to-end encryption of a direct message on or off.
        
        Direct messages between two people only. Turning it on needs the E2E feature and both participants' registered keys; once on, only the person who opened the DM may turn it off.
        
        `POST /api/messenger/channels/{channelId}/e2e`
        """
        return _pick(self._request("POST", f"/api/messenger/channels/{_seg(channel_id)}/e2e", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_presence(self, body: MessengerSetPresenceBody, *, options: Optional[RequestOptions] = None) -> MessengerSetPresenceResponseData:
        """Sets the caller's status, or reports them online.
        
        `online` without emoji, text or expiry is a heartbeat; anything else sets the caller's own status, which wins over the automatic one (focus time, meetings, absence) until it expires.
        
        `PUT /api/messenger/presence`
        """
        return _pick(self._request("PUT", f"/api/messenger/presence", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_typing(self, channel_id: str, body: MessengerSetTypingBody, *, options: Optional[RequestOptions] = None) -> MessengerSetTypingResponseData:
        """Tells the channel's open clients that the caller started or stopped typing.
        
        Nothing is stored. At most 6 calls in 10 seconds per channel.
        
        `POST /api/messenger/channels/{channelId}/typing`
        """
        return _pick(self._request("POST", f"/api/messenger/channels/{_seg(channel_id)}/typing", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_channel(self, id: str, body: MessengerUpdateChannelBody, *, options: Optional[RequestOptions] = None) -> MessengerChannel:
        """Changes a channel's name, description, topic, icon, type or visibility, or archives it.
        
        The channel's owners and admins only; widening who can find it is the owner's.
        
        `PUT /api/messenger/channels/{id}`
        """
        return _pick(self._request("PUT", f"/api/messenger/channels/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_channel_webhook(self, channel_id: str, webhook_id: str, body: MessengerUpdateChannelWebhookBody, *, options: Optional[RequestOptions] = None) -> MessengerChannelWebhook:
        """Renames, pauses or redirects a channel's webhook.
        
        The channel's owners and admins; needs the Messenger webhooks feature.
        
        `PATCH /api/messenger/channels/{channelId}/webhooks/{webhookId}`
        """
        return _pick(self._request("PATCH", f"/api/messenger/channels/{_seg(channel_id)}/webhooks/{_seg(webhook_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_message(self, message_id: str, body: MessengerUpdateMessageBody, *, options: Optional[RequestOptions] = None) -> MessengerMessageRecord:
        """Edits one of the caller's messages.
        
        Only the sender, while still a member of the channel; a deleted message answers 410.
        
        `PUT /api/messenger/messages/{messageId}`
        """
        return _pick(self._request("PUT", f"/api/messenger/messages/{_seg(message_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_settings(self, body: MessengerUpdateSettingsBody, *, options: Optional[RequestOptions] = None) -> MessengerSettings:
        """Changes the caller's Messenger settings.
        
        `PUT /api/messenger/settings`
        """
        return _pick(self._request("PUT", f"/api/messenger/settings", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class MilestonesDatabaseResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MilestonesDatabaseGetResponse:
        """Returns which database the organisation's milestones are kept in, and the databases and workspaces they could go to.
        
        Needs `milestones:share` besides `milestones:read`. `databases` lists the organisation's databases the caller may edit that are not managed by something else; `workspaces` those where a new one can be created.
        
        `GET /api/milestones/database`
        """
        return self._request("GET", f"/api/milestones/database", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def stop(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MilestonesDatabaseStopResponse:
        """Stops keeping the organisation's milestones in a database.
        
        Needs `milestones:share` besides `milestones:read`. The rows already written stay.
        
        `DELETE /api/milestones/database`
        """
        return self._request("DELETE", f"/api/milestones/database", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def sync(self, body: MilestonesDatabaseSyncBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MilestoneDatabaseResult:
        """Writes the organisation's milestones into a database, or tells what it would write.
        
        Needs `milestones:share` besides `milestones:read`. With `apply: true` the rows are written as the caller and the database is kept in sync from then on, with every new level reached; without it nothing is written. The rows go through the Databases hub's own rules (access, approvals, automations, the record limit): 403, 404 `databaseNotFound`, 409 `milestoneDatabaseIncompatible` or `limitReached` when they refuse.
        
        `POST /api/milestones/database`
        """
        return _pick(self._request("POST", f"/api/milestones/database", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "result")  # type: ignore[no-any-return]


class MilestonesResource(_Resource):
    """Milestones — An organisation's milestones: tracks of recorded figures (visitors, submissions, bookings, paid revenue, CRM contacts, workflow runs, years, referrals) with levels, and the rewards a level gives. The platform defines the tracks and levels; an organisation reads its progress, opts in to the public website badge, gives the shipping address of a physical reward, and may keep its milestones in one of its databases. Everything needs Milestones on the plan and `milestones:read` at organisation level; revenue figures need `invoicing:read` besides (without it the revenue track is left out).
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.database = MilestonesDatabaseResource(request)

    def get(self, *, organization_id: Optional[str] = None, figures: Optional[Literal["0"]] = None, options: Optional[RequestOptions] = None) -> MilestoneOverview:
        """Returns an organisation's milestone tracks with its figures, the levels reached and the rewards waiting.
        
        A surprise level not reached shows nothing but its place. Reading the figures also refreshes the organisation's evaluation, at most every ten minutes.
        
        `GET /api/milestones`
        """
        return self._request("GET", f"/api/milestones", query={"organizationId": organization_id, "figures": figures}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def submit_shipping_address(self, item_id: str, body: MilestonesSubmitShippingAddressBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MilestonesSubmitShippingAddressResponseItem:
        """Gives or corrects the shipping address of a physical reward that has not been shipped yet.
        
        Needs `milestones:share` besides `milestones:read`. The rewards waiting for one are `awaitingAddress` of milestones.get. 400 `rewardAddressInvalid` for an incomplete address; 404 `rewardItemNotFound` for an item that is not this organisation's or already shipped.
        
        `PUT /api/milestones/fulfilment/{itemId}`
        """
        return _pick(self._request("PUT", f"/api/milestones/fulfilment/{_seg(item_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "item")  # type: ignore[no-any-return]

    def update_settings(self, body: MilestonesUpdateSettingsBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> bool:
        """Switches the public website badge with the organisation's latest milestone on or off.
        
        Needs `milestones:share` besides `milestones:read`. Switched off, the badge's address answers 404 at once. It never shows revenue.
        
        `PUT /api/milestones/settings`
        """
        return _pick(self._request("PUT", f"/api/milestones/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "shareBadge")  # type: ignore[no-any-return]


class NotificationsResource(_Resource):
    """Notifications
    """

    def bulk(self, body: NotificationsBulkBody, *, options: Optional[RequestOptions] = None) -> List[str]:
        """Marks several of the caller's notifications read or unread, or deletes them.
        
        At most 500 ids at a time. Ids that are not the caller's are skipped; `changed` lists the ones acted on.
        
        `POST /api/notifications/bulk`
        """
        return _pick(self._request("POST", f"/api/notifications/bulk", query=None, body=body, multipart=False, options=options), "changed")  # type: ignore[no-any-return]

    def delete(self, *, id: str, options: Optional[RequestOptions] = None) -> NotificationsDeleteResponse:
        """Deletes one of the caller's notifications.
        
        `DELETE /api/notifications`
        """
        return self._request("DELETE", f"/api/notifications", query={"id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_settings(self, *, options: Optional[RequestOptions] = None) -> List[NotificationsGetSettingsResponseCategoriesItem]:
        """Returns the caller's notification settings: every kind of notification by category, with its channels and whether it is on.
        
        Without saved settings the platform's defaults come back; categories added to the platform since the caller saved appear with their defaults.
        
        `GET /api/settings/notifications`
        """
        return _pick(self._request("GET", f"/api/settings/notifications", query=None, body=None, multipart=False, options=options), "categories")  # type: ignore[no-any-return]

    def list(self, *, limit: Optional[int] = None, cursor: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Notification]:
        """Lists the caller's notifications, newest first, a page at a time.
        
        At most 30 calls a minute. For the next page pass the answer's `nextCursor` as `cursor`; it is null on the last page.
        
        `GET /api/notifications`
        """
        return _pick(self._request("GET", f"/api/notifications", query={"limit": limit, "cursor": cursor}, body=None, multipart=False, options=options), "notifications")  # type: ignore[no-any-return]

    def mark_all_read(self, *, options: Optional[RequestOptions] = None) -> float:
        """Marks all of the caller's notifications as read.
        
        `POST /api/notifications/mark-all-read`
        """
        return _pick(self._request("POST", f"/api/notifications/mark-all-read", query=None, body=None, multipart=False, options=options), "marked")  # type: ignore[no-any-return]

    def mark_read(self, body: NotificationsMarkReadBody, *, options: Optional[RequestOptions] = None) -> Notification:
        """Marks one of the caller's notifications as read.
        
        `PUT /api/notifications`
        """
        return self._request("PUT", f"/api/notifications", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def unread_count(self, *, options: Optional[RequestOptions] = None) -> float:
        """Returns how many of the caller's notifications are unread.
        
        At most 60 calls a minute; beyond that it answers 0.
        
        `GET /api/notifications/unread-count`
        """
        return _pick(self._request("GET", f"/api/notifications/unread-count", query=None, body=None, multipart=False, options=options), "count")  # type: ignore[no-any-return]


class OauthConnectionsResource(_Resource):

    def list(self, *, options: Optional[RequestOptions] = None) -> List[OAuthConnection]:
        """Lists the OAuth apps the caller has connected to their account and that still hold a live token.
        
        `GET /api/oauth/my-connections`
        """
        return _pick(self._request("GET", f"/api/oauth/my-connections", query=None, body=None, multipart=False, options=options), "data.connections")  # type: ignore[no-any-return]

    def revoke(self, client_id: str, *, options: Optional[RequestOptions] = None) -> OauthConnectionsRevokeResponseData:
        """Disconnects an OAuth app from the caller's account.
        
        Revokes every refresh and access token the app holds for the caller and switches off its webhook subscriptions, at once; the caller gets a security email.
        
        `DELETE /api/oauth/my-connections/{clientId}`
        """
        return _pick(self._request("DELETE", f"/api/oauth/my-connections/{_seg(client_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class OauthResource(_Resource):
    """OAuth — Who a token belongs to, and the OAuth apps (Zapier, Make, an MCP client …) the caller has connected to their account.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.connections = OauthConnectionsResource(request)

    def userinfo(self, *, options: Optional[RequestOptions] = None) -> OauthUserinfoResponseData:
        """Returns who the token or session belongs to, in OpenID Connect UserInfo form.
        
        A token holding only OAuth client scopes (`openid`, `profile`, `email`, `offline_access`, `mcp:*`) gets `sub`, plus `email` with the `email` scope and `name` and `picture` with `profile` — never the organizations. Any other token or a session gets every field.
        
        `GET /api/oauth/userinfo` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/oauth/userinfo", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class OrganizationsEmailTemplatesResource(_Resource):

    def list(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsEmailTemplatesListResponseData:
        """Lists the visitor emails the organization may word itself, in each language its projects use, with the wording that is sent.
        
        A project's own wording wins over the organization's.
        
        `GET /api/organizations/{organizationId}/email-templates`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/email-templates", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def reset(self, organization_id: str, type_: str, *, locale: str, options: Optional[RequestOptions] = None) -> OrganizationsEmailTemplatesResetResponse:
        """Goes back to the platform's wording of a visitor email in one language.
        
        `DELETE /api/organizations/{organizationId}/email-templates/{type}`
        """
        return self._request("DELETE", f"/api/organizations/{_seg(organization_id)}/email-templates/{_seg(type_)}", query={"locale": locale}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set(self, organization_id: str, type_: str, body: EmailTemplateInput, *, options: Optional[RequestOptions] = None) -> OrganizationsEmailTemplatesSetResponse:
        """Saves the organization's own wording of a visitor email in one language, for every project that has none of its own.
        
        Needs `organization.update` and the plan's custom email templates. The HTML is cleaned before it is stored.
        
        `PUT /api/organizations/{organizationId}/email-templates/{type}`
        """
        return self._request("PUT", f"/api/organizations/{_seg(organization_id)}/email-templates/{_seg(type_)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class OrganizationsResource(_Resource):
    """Organizations
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.email_templates = OrganizationsEmailTemplatesResource(request)

    def add_member(self, organization_id: str, body: OrganizationsAddMemberBody, *, options: Optional[RequestOptions] = None) -> OrganizationsAddMemberResponseData:
        """Invites a person to an organization by email, or adds them at once when the organization adds directly.
        
        Needs `organization.manage_members`. In `invite` mode (the default, see `organizations.getMemberAdding`) every address gets an invitation and the answer is the same whether or not it has an account; in `direct` mode an existing account joins at once (`added`). The seat is checked against the plan.
        
        `POST /api/organizations/{organizationId}/members`
        """
        return _pick(self._request("POST", f"/api/organizations/{_seg(organization_id)}/members", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def assign_team(self, organization_id: str, body: OrganizationsAssignTeamBody, *, options: Optional[RequestOptions] = None) -> TeamRoleAssignment:
        """Gives a team a role across the whole organization.
        
        Needs `team.assign`.
        
        `POST /api/organizations/{organizationId}/teams`
        """
        return _pick(self._request("POST", f"/api/organizations/{_seg(organization_id)}/teams", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def cancel_deletion(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsCancelDeletionResponseData:
        """Cancels an organization's scheduled deletion.
        
        Needs `organization.delete`.
        
        `DELETE /api/organizations/{organizationId}/scheduled-deletion`
        """
        return _pick(self._request("DELETE", f"/api/organizations/{_seg(organization_id)}/scheduled-deletion", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: OrganizationsCreateBody, *, options: Optional[RequestOptions] = None) -> OrganizationsCreateResponseData:
        """Creates an organization with the caller as its owner, a default workspace and the standard roles.
        
        `POST /api/organizations`
        """
        return _pick(self._request("POST", f"/api/organizations", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_freeze_window(self, organization_id: str, body: FreezeWindowInput, *, options: Optional[RequestOptions] = None) -> OrganizationsCreateFreezeWindowResponseData:
        """Adds a publish freeze window, one-off or recurring.
        
        Organization administrators only. Give `cronExpr`, or `startsAt` and `endsAt`.
        
        `POST /api/organizations/{organizationId}/freeze-windows`
        """
        return _pick(self._request("POST", f"/api/organizations/{_seg(organization_id)}/freeze-windows", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsDeleteResponseData:
        """Schedules an organization for deletion in 14 days.
        
        Needs `organization.delete`. Until then the deletion can be cancelled with `organizations.cancelDeletion`.
        
        `DELETE /api/organizations/{organizationId}`
        """
        return _pick(self._request("DELETE", f"/api/organizations/{_seg(organization_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_freeze_window(self, organization_id: str, window_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsDeleteFreezeWindowResponse:
        """Removes a publish freeze window.
        
        `DELETE /api/organizations/{organizationId}/freeze-windows/{windowId}`
        """
        return self._request("DELETE", f"/api/organizations/{_seg(organization_id)}/freeze-windows/{_seg(window_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> Organization:
        """Returns one organization; billing details only to those who may read billing.
        
        `GET /api/organizations/{organizationId}` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_member_adding(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsGetMemberAddingResponseData:
        """Returns how the organization adds a person by email: always by invitation, or directly when they have an account.
        
        `GET /api/organizations/{organizationId}/member-adding`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/member-adding", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_report_recipients(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsGetReportRecipientsResponseData:
        """Returns whether scheduled reports may go to addresses outside the organization.
        
        `GET /api/organizations/{organizationId}/report-recipients`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/report-recipients", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_scheduled_deletion(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsGetScheduledDeletionResponseData:
        """Returns when an organization is due to be deleted, if it is.
        
        `GET /api/organizations/{organizationId}/scheduled-deletion`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/scheduled-deletion", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_seat_capacity(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> SeatCapacity:
        """Returns the organization's seats: included, bought and taken, per tier on a tiered plan.
        
        `GET /api/organizations/{organizationId}/seat-capacity`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/seat-capacity", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_sharing_settings(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> AssetSharingSettings:
        """Returns the organization's file-sharing defaults and limits.
        
        `GET /api/organizations/{organizationId}/sharing-settings`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/sharing-settings", query=None, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def list(self, *, search: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Organization]:
        """Lists the organizations the caller belongs to or has a role in.
        
        `GET /api/organizations` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/organizations", query={"search": search, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_freeze_windows(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> List[FreezeWindow]:
        """Lists an organization's publish freeze windows — times nothing may go live.
        
        `GET /api/organizations/{organizationId}/freeze-windows`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/freeze-windows", query=None, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def list_invitations(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> List[OrganizationInvitation]:
        """Lists an organization's open invitations.
        
        `GET /api/organizations/{organizationId}/invitations`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/invitations", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_members(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> List[OrganizationMember]:
        """Lists an organization's members with their user details and seat.
        
        `GET /api/organizations/{organizationId}/members`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/members", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_my_memberships(self, *, options: Optional[RequestOptions] = None) -> List[OrganizationMember]:
        """Lists the caller's own organization memberships.
        
        `GET /api/organization-members`
        """
        return _pick(self._request("GET", f"/api/organization-members", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_teams(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> List[OrganizationsListTeamsResponseDataItem]:
        """Lists an organization's teams with their member counts and the roles they hold in it.
        
        `GET /api/organizations/{organizationId}/teams`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/teams", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_workspaces(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> List[Workspace]:
        """Lists the workspaces of an organization the caller can open.
        
        `GET /api/organizations/{organizationId}/workspaces`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/workspaces", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_member(self, organization_id: str, member_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsRemoveMemberResponse:
        """Removes a member from an organization.
        
        `DELETE /api/organizations/{organizationId}/members/{memberId}`
        """
        return self._request("DELETE", f"/api/organizations/{_seg(organization_id)}/members/{_seg(member_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def remove_team(self, organization_id: str, team_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsRemoveTeamResponse:
        """Takes away the roles a team holds across the organization.
        
        `DELETE /api/organizations/{organizationId}/teams/{teamId}`
        """
        return self._request("DELETE", f"/api/organizations/{_seg(organization_id)}/teams/{_seg(team_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def resend_invitation(self, organization_id: str, invitation_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsResendInvitationResponseData:
        """Sends an invitation's email again and extends it.
        
        `POST /api/organizations/{organizationId}/invitations/{invitationId}/resend`
        """
        return _pick(self._request("POST", f"/api/organizations/{_seg(organization_id)}/invitations/{_seg(invitation_id)}/resend", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def revoke_invitation(self, organization_id: str, invitation_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsRevokeInvitationResponseData:
        """Revokes an invitation, so its link no longer works.
        
        `DELETE /api/organizations/{organizationId}/invitations/{invitationId}`
        """
        return _pick(self._request("DELETE", f"/api/organizations/{_seg(organization_id)}/invitations/{_seg(invitation_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_member_adding(self, organization_id: str, body: OrganizationsSetMemberAddingBody, *, options: Optional[RequestOptions] = None) -> OrganizationsSetMemberAddingResponseData:
        """Chooses how the organization adds a person by email.
        
        `direct` is faster but tells whoever adds whether the address has an account.
        
        `PUT /api/organizations/{organizationId}/member-adding`
        """
        return _pick(self._request("PUT", f"/api/organizations/{_seg(organization_id)}/member-adding", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_report_recipients(self, organization_id: str, body: OrganizationsSetReportRecipientsBody, *, options: Optional[RequestOptions] = None) -> OrganizationsSetReportRecipientsResponseData:
        """Allows or stops scheduled reports to addresses outside the organization.
        
        Needs `organization.update`. Switching it off stops the outside addresses of every schedule at their next send.
        
        `PUT /api/organizations/{organizationId}/report-recipients`
        """
        return _pick(self._request("PUT", f"/api/organizations/{_seg(organization_id)}/report-recipients", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, organization_id: str, body: OrganizationsUpdateBody, *, options: Optional[RequestOptions] = None) -> Organization:
        """Changes an organization's name, look, settings or billing details.
        
        Needs `organization.update`; the billing fields need `billing.read` as well.
        
        `PUT /api/organizations/{organizationId}`
        """
        return _pick(self._request("PUT", f"/api/organizations/{_seg(organization_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_freeze_window(self, organization_id: str, window_id: str, body: FreezeWindowInput, *, options: Optional[RequestOptions] = None) -> OrganizationsUpdateFreezeWindowResponseData:
        """Replaces a publish freeze window.
        
        Send the whole window, as when creating it.
        
        `PATCH /api/organizations/{organizationId}/freeze-windows/{windowId}`
        """
        return _pick(self._request("PATCH", f"/api/organizations/{_seg(organization_id)}/freeze-windows/{_seg(window_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_member(self, organization_id: str, member_id: str, body: OrganizationsUpdateMemberBody, *, options: Optional[RequestOptions] = None) -> OrganizationMember:
        """Changes a member's role or seat tier.
        
        Needs `organization.manage_members`. Only an owner makes or unmakes an owner, and the last owner stays one.
        
        `PATCH /api/organizations/{organizationId}/members/{memberId}`
        """
        return _pick(self._request("PATCH", f"/api/organizations/{_seg(organization_id)}/members/{_seg(member_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_seat_settings(self, organization_id: str, body: OrganizationsUpdateSeatSettingsBody, *, options: Optional[RequestOptions] = None) -> OrganizationsUpdateSeatSettingsResponseData:
        """Sets the seat a newly added member gets, and the order seats are handed out in after a plan change.
        
        Needs `organization.manage_members`.
        
        `PATCH /api/organizations/{organizationId}/seat-settings`
        """
        return _pick(self._request("PATCH", f"/api/organizations/{_seg(organization_id)}/seat-settings", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_sharing_settings(self, organization_id: str, body: OrganizationsUpdateSharingSettingsBody, *, options: Optional[RequestOptions] = None) -> AssetSharingSettings:
        """Changes the organization's file-sharing defaults and limits.
        
        Needs `organization.update`.
        
        `PUT /api/organizations/{organizationId}/sharing-settings`
        """
        return _pick(self._request("PUT", f"/api/organizations/{_seg(organization_id)}/sharing-settings", query=None, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def version_stats(self, organization_id: str, *, options: Optional[RequestOptions] = None) -> OrganizationsVersionStatsResponseData:
        """Returns how much storage the organization's file versions take and how long they are kept.
        
        `GET /api/organizations/{organizationId}/version-stats`
        """
        return _pick(self._request("GET", f"/api/organizations/{_seg(organization_id)}/version-stats", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class PagesResource(_Resource):
    """Pages
    """

    def ab_test_action(self, page_id: str, body: PagesAbTestActionBody, *, options: Optional[RequestOptions] = None) -> PagesAbTestActionResponseData:
        """Starts, updates, pauses, resumes or stops the page's A/B test.
        
        `start` and `update` put variant B live through the publish rules — with approval required the answer is a 202 waiting for it. At most 30 calls a minute.
        
        `POST /api/pages/{pageId}/ab-test` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/ab-test", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: CreatePageInput, *, options: Optional[RequestOptions] = None) -> Page:
        """Creates a page in a project.
        
        Needs `page.create`. The page starts as a draft.
        
        `POST /api/pages` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_collection(self, body: PagesCreateCollectionBody, *, options: Optional[RequestOptions] = None) -> PagesCreateCollectionResponse:
        """Creates a list page and a detail page that show a database's records on a project's site.
        
        Needs `page.create`, access to the workspace and project, and a database of the project's organization the caller can open; the two pages count against `max_pages_per_project`. The detail page answers at `basePath` with each record's slug appended, the list page at `basePath` + `-list`. Both are drafts until published.
        
        `POST /api/collection-pages/generate`
        """
        return self._request("POST", f"/api/collection-pages/generate", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create_preview(self, page_id: str, *, rotate: Optional[Literal["true"]] = None, options: Optional[RequestOptions] = None) -> PagesCreatePreviewResponseData:
        """Returns a preview link to the page's draft, creating one when it has none.
        
        `POST /api/pages/{pageId}/preview` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/preview", query={"rotate": rotate}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_version(self, page_id: str, body: PagesCreateVersionBody, *, options: Optional[RequestOptions] = None) -> PageVersion:
        """Saves a named version of a page.
        
        `POST /api/pages/{pageId}/versions` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/versions", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, page_id: str, *, options: Optional[RequestOptions] = None) -> PagesDeleteResponseData:
        """Moves a page to the trash.
        
        `DELETE /api/pages/{pageId}` — Token permission: `write:pages`.
        """
        return _pick(self._request("DELETE", f"/api/pages/{_seg(page_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_version(self, page_id: str, version_id: str, *, options: Optional[RequestOptions] = None) -> PagesDeleteVersionResponse:
        """Deletes a saved version of a page.
        
        `DELETE /api/pages/{pageId}/versions/{versionId}` — Token permission: `write:pages`.
        """
        return self._request("DELETE", f"/api/pages/{_seg(page_id)}/versions/{_seg(version_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def discard(self, page_id: str, *, options: Optional[RequestOptions] = None) -> Page:
        """Throws away a published page's unpublished changes, putting the draft back to what is live.
        
        `POST /api/pages/{pageId}/discard` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/discard", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def duplicate(self, page_id: str, body: PagesDuplicateBody, *, copy_collection: Optional[Literal["true", "false"]] = None, options: Optional[RequestOptions] = None) -> Page:
        """Copies a page within its project as a new draft.
        
        Needs `page.create`. The copy gets a unique name and path, is never the home page, has no translations, versions or A/B test, and starts as a draft.
        
        `POST /api/pages/{pageId}/duplicate` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/duplicate", query={"copyCollection": copy_collection}, body=body, multipart=False, options=options), "data.page")  # type: ignore[no-any-return]

    def get(self, page_id: str, *, options: Optional[RequestOptions] = None) -> PagesGetResponseData:
        """Returns a page with its draft tree and whether a publish is waiting for approval.
        
        `GET /api/pages/{pageId}` — Token permission: `read:pages`.
        """
        return _pick(self._request("GET", f"/api/pages/{_seg(page_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_ab_test(self, page_id: str, *, options: Optional[RequestOptions] = None) -> PagesGetAbTestResponseData:
        """Returns the page's A/B test on the live site: status, goal, split and each variant's results.
        
        `GET /api/pages/{pageId}/ab-test` — Token permission: `read:pages`.
        """
        return _pick(self._request("GET", f"/api/pages/{_seg(page_id)}/ab-test", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_components(self, page_id: str, *, options: Optional[RequestOptions] = None) -> List[Any]:
        """Returns a page's draft component tree.
        
        `GET /api/pages/{pageId}/components` — Token permission: `read:pages`.
        """
        return _pick(self._request("GET", f"/api/pages/{_seg(page_id)}/components", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_version(self, page_id: str, version_id: str, *, options: Optional[RequestOptions] = None) -> PageVersion:
        """Returns one version of a page, with its tree.
        
        `GET /api/pages/{pageId}/versions/{versionId}` — Token permission: `read:pages`.
        """
        return _pick(self._request("GET", f"/api/pages/{_seg(page_id)}/versions/{_seg(version_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_translations(self, page_id: str, *, options: Optional[RequestOptions] = None) -> List[PageTranslationVariant]:
        """Lists the language versions of a page, the page itself included.
        
        `GET /api/pages/{pageId}/translations` — Token permission: `read:pages`.
        """
        return _pick(self._request("GET", f"/api/pages/{_seg(page_id)}/translations", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_versions(self, page_id: str, *, options: Optional[RequestOptions] = None) -> List[PageVersionSummary]:
        """Lists a page's saved versions, newest first, without their trees.
        
        `GET /api/pages/{pageId}/versions` — Token permission: `read:pages`.
        """
        return _pick(self._request("GET", f"/api/pages/{_seg(page_id)}/versions", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def restore_version(self, page_id: str, version_id: str, body: PagesRestoreVersionBody, *, options: Optional[RequestOptions] = None) -> Page:
        """Puts a version back into the page's draft, and publishes it with `publish: true`.
        
        Needs `version.restore`. Publishing goes through the publish rules — with approval required the answer says `pendingApproval`.
        
        `POST /api/pages/{pageId}/versions/{versionId}/restore` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/versions/{_seg(version_id)}/restore", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def restore_version_legacy(self, page_id: str, version_id: str, body: PagesRestoreVersionLegacyBody, *, options: Optional[RequestOptions] = None) -> Page:
        """Puts a version back into the page's draft — the older address of `pages.restoreVersion`, with the same checks.
        
        `POST /api/pages/{pageId}/versions/{versionId}` — Token permission: `write:pages`.
        
        .. deprecated:: 0.2.0 Use `pages.restoreVersion`.
        """
        _deprecated("pages.restoreVersionLegacy")
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/versions/{_seg(version_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def revoke_preview(self, page_id: str, *, options: Optional[RequestOptions] = None) -> PagesRevokePreviewResponse:
        """Revokes the page's preview link.
        
        `DELETE /api/pages/{pageId}/preview` — Token permission: `write:pages`.
        """
        return self._request("DELETE", f"/api/pages/{_seg(page_id)}/preview", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def scan(self, page_id: str, *, options: Optional[RequestOptions] = None) -> PagesScanResponseData:
        """Checks one page for outdated content and broken links.
        
        A published page is checked as visitors see it and the findings are kept for Site health; a draft is checked as it is. At most 4 calls an hour per page.
        
        `POST /api/pages/{pageId}/scan` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/scan", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_collection_mode(self, body: PagesSetCollectionModeBody, *, options: Optional[RequestOptions] = None) -> Page:
        """Makes a page a collection list or detail page of a database, or a static page again.
        
        Needs `page.update`. `list` and `detail` need `databaseId` and a `slugField` that is a column of it; a list page may name its `detailPageId` (a page of the same project, made a detail page of the same database if it is not one yet). `none` removes every collection setting.
        
        `POST /api/collection-pages/convert`
        """
        return _pick(self._request("POST", f"/api/collection-pages/convert", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def translate(self, page_id: str, body: PagesTranslateBody, *, options: Optional[RequestOptions] = None) -> Page:
        """Creates a language version of a page, machine-translated by default.
        
        Needs `page.create`. The new page joins the original's translation group; with `translate: false` its tree is copied as it is.
        
        `POST /api/pages/{pageId}/translate` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/translate", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def unverify(self, page_id: str, *, options: Optional[RequestOptions] = None) -> PagesUnverifyResponse:
        """Removes the page's content-checked mark.
        
        `DELETE /api/pages/{pageId}/verify` — Token permission: `write:pages`.
        """
        return self._request("DELETE", f"/api/pages/{_seg(page_id)}/verify", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, page_id: str, body: UpdatePageInput, *, options: Optional[RequestOptions] = None) -> Page:
        """Changes a page's draft — its tree, name, path or SEO fields — and publishes or schedules it with `status`.
        
        Needs `page.update`. Everything but `status: "published"` changes the draft only. Publishing applies freeze windows and the organization's approval requirement: when approval is required the answer is a 202 with `pendingApproval: true` and the page stays as it is live. A password or sign-in requirement added in the draft applies to the live page at once.
        
        `PUT /api/pages/{pageId}` — Token permission: `write:pages`.
        """
        return _pick(self._request("PUT", f"/api/pages/{_seg(page_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def verify(self, page_id: str, *, options: Optional[RequestOptions] = None) -> PagesVerifyResponseData:
        """Marks the page's content as checked by the caller today.
        
        `POST /api/pages/{pageId}/verify` — Token permission: `write:pages`.
        """
        return _pick(self._request("POST", f"/api/pages/{_seg(page_id)}/verify", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class PdfEsignResource(_Resource):

    def audit_trail(self, request_id: str, *, organization_id: str, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a signature request's audit trail as a PDF: the request, its signers and every event with time, address and browser.
        
        Only the person who sent the request. Teammates who see a shared request cannot download its evidence.
        
        `GET /api/pdf/esign/requests/{requestId}/audit`
        """
        return self._request("GET", f"/api/pdf/esign/requests/{_seg(request_id)}/audit", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def cancel(self, request_id: str, body: PdfEsignCancelBody, *, options: Optional[RequestOptions] = None) -> PdfEsignCancelResponseData:
        """Cancels a signature request; its signing links stop working at once.
        
        Only the person who sent the request. Cancelling again changes nothing.
        
        `POST /api/pdf/esign/requests/{requestId}/cancel`
        """
        return _pick(self._request("POST", f"/api/pdf/esign/requests/{_seg(request_id)}/cancel", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: PdfEsignCreateBody, *, options: Optional[RequestOptions] = None) -> PdfEsignCreateResponseData:
        """Sends a PDF of the asset library to up to 20 people to sign, one after the other or all at once.
        
        The invitations are emailed (sequential: the next signer once the one before signed). Each signer's `signUrl` is a secret link to their signing page.
        
        `POST /api/pdf/esign/request`
        """
        return _pick(self._request("POST", f"/api/pdf/esign/request", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, status: Optional[Literal["all", "pending", "completed", "cancelled"]] = None, scope: Optional[Literal["all", "own", "workspace", "organization"]] = None, workspace_ids: Optional[str] = None, q: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[SignatureRequestSummary]:
        """Lists the signature requests the caller can see in an organisation, newest first.
        
        The caller's own, those shared with a workspace they can open, and those shared with the organisation; `isMine` tells which are theirs.
        
        `GET /api/pdf/esign/requests`
        """
        return _pick(self._request("GET", f"/api/pdf/esign/requests", query={"organizationId": organization_id, "status": status, "scope": scope, "workspaceIds": workspace_ids, "q": q, "limit": limit}, body=None, multipart=False, options=options), "data.requests")  # type: ignore[no-any-return]

    def resend(self, request_id: str, body: PdfEsignResendBody, *, options: Optional[RequestOptions] = None) -> PdfEsignResendResponseData:
        """Emails the invitation of a pending signature request again, with the same link.
        
        Only the person who sent the request.
        
        `POST /api/pdf/esign/requests/{requestId}/resend`
        """
        return _pick(self._request("POST", f"/api/pdf/esign/requests/{_seg(request_id)}/resend", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_visibility(self, request_id: str, body: PdfEsignSetVisibilityBody, *, options: Optional[RequestOptions] = None) -> PdfEsignSetVisibilityResponseData:
        """Changes who else sees a signature request: nobody, a workspace or the whole organisation.
        
        Only the person who sent the request. `workspace` needs a workspace the caller can open.
        
        `PATCH /api/pdf/esign/requests/{requestId}`
        """
        return _pick(self._request("PATCH", f"/api/pdf/esign/requests/{_seg(request_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class PdfRedactionAuditsResource(_Resource):

    def get(self, audit_id: str, *, pdf: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> RedactionAudit:
        """Returns the record of a redaction: which file, how many spans of which kinds, and the SHA-256 before and after.
        
        Needs `asset:redact` and membership of the record's organisation. With `pdf=1` it answers a one-page PDF of the record to download instead.
        
        `GET /api/pdf/redaction-audits/{auditId}`
        """
        return _pick(self._request("GET", f"/api/pdf/redaction-audits/{_seg(audit_id)}", query={"pdf": pdf}, body=None, multipart=False, options=options), "data.audit")  # type: ignore[no-any-return]


class PdfResource(_Resource):
    """PDF — Tools for the PDF files of an organisation's asset library — editing, merging, splitting, compressing, password protection, summaries and explanations, form filling — and e-signature requests that send a PDF to be signed. A tool reads its source by asset id; one that produces a PDF saves it as a new file of the library, or replaces the source with `overwrite`.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.esign = PdfEsignResource(request)
        self.redaction_audits = PdfRedactionAuditsResource(request)

    def ai_fill(self, body: PdfAiFillBody, *, options: Optional[RequestOptions] = None) -> PdfAiFillResponseData:
        """Proposes values for a PDF form's fields from a description, with the platform's AI.
        
        Needs PDF AI on the organisation's plan (403 when switched off) and its AI allowance (429); the file must be within the plan's PDF size (413). Nothing is written: apply the values with pdf.edit (`set_form_field`). 422 for a PDF without form fields.
        
        `POST /api/pdf/ai-fill`
        """
        return _pick(self._request("POST", f"/api/pdf/ai-fill", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def compress(self, body: PdfCompressBody, *, options: Optional[RequestOptions] = None) -> Asset:
        """Writes a PDF again compactly, dropping what earlier edits left behind.
        
        Needs the PDF editor on the organisation's plan (403 when it is switched off, 429 when the plan leaves it out), a file within the plan's PDF size (413; 25 MB unless the plan says otherwise), room in its storage (403) and AI allowance left (429). Images are not resampled.
        
        `POST /api/pdf/compress`
        """
        return _pick(self._request("POST", f"/api/pdf/compress", query=None, body=body, multipart=False, options=options), "data.asset")  # type: ignore[no-any-return]

    def detect_signature_lines(self, body: PdfDetectSignatureLinesBody, *, options: Optional[RequestOptions] = None) -> List[PdfDetectSignatureLinesResponseDataLinesItem]:
        """Finds where a PDF asks for a signature, from words like "Signature" or "Unterschrift" and lines to sign on.
        
        Needs PDF AI on the organisation's plan (403 when switched off) and its AI allowance (429); the file must be within the plan's PDF size (413). A heuristic over the text layer: it misses scanned pages without one.
        
        `POST /api/pdf/detect-signature-lines`
        """
        return _pick(self._request("POST", f"/api/pdf/detect-signature-lines", query=None, body=body, multipart=False, options=options), "data.lines")  # type: ignore[no-any-return]

    def edit(self, body: PdfEditBody, *, options: Optional[RequestOptions] = None) -> Asset:
        """Applies a list of edits to a PDF — text, images, signatures, highlights, drawings, redactions, page changes, form fields, watermarks — in order.
        
        Needs the PDF editor on the organisation's plan (403 when it is switched off, 429 when the plan leaves it out), a file within the plan's PDF size (413; 25 MB unless the plan says otherwise), room in its storage (403) and AI allowance left (429). At most 500 edits. A redaction that is to remove the text and not only cover it pairs each `redact` with a `flatten_page` of that page; `redaction` then files the redaction record.
        
        `POST /api/pdf/edit`
        """
        return _pick(self._request("POST", f"/api/pdf/edit", query=None, body=body, multipart=False, options=options), "data.asset")  # type: ignore[no-any-return]

    def explain(self, body: PdfExplainBody, *, options: Optional[RequestOptions] = None) -> PdfExplainResponseData:
        """Explains one page of a PDF in plain language with the platform's AI.
        
        Needs PDF AI on the organisation's plan (403 when switched off) and its AI allowance (429); the file must be within the plan's PDF size (413). 422 when the page has no text layer. Nothing is stored.
        
        `POST /api/pdf/explain`
        """
        return _pick(self._request("POST", f"/api/pdf/explain", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def merge(self, body: PdfMergeBody, *, options: Optional[RequestOptions] = None) -> Asset:
        """Merges 2 to 20 PDFs, in the order given, into one.
        
        Needs the PDF editor on the organisation's plan (403 when it is switched off, 429 when the plan leaves it out), a file within the plan's PDF size (413; 25 MB unless the plan says otherwise), room in its storage (403) and AI allowance left (429). With `overwrite` the first file is replaced.
        
        `POST /api/pdf/merge`
        """
        return _pick(self._request("POST", f"/api/pdf/merge", query=None, body=body, multipart=False, options=options), "data.asset")  # type: ignore[no-any-return]

    def protect(self, body: PdfProtectBody, *, options: Optional[RequestOptions] = None) -> Asset:
        """Encrypts a PDF with AES-256 so it opens only with the password.
        
        Needs the PDF editor on the organisation's plan (403 when it is switched off, 429 when the plan leaves it out), a file within the plan's PDF size (413; 25 MB unless the plan says otherwise), room in its storage (403) and AI allowance left (429).
        
        `POST /api/pdf/protect`
        """
        return _pick(self._request("POST", f"/api/pdf/protect", query=None, body=body, multipart=False, options=options), "data.asset")  # type: ignore[no-any-return]

    def split(self, body: PdfSplitBody, *, options: Optional[RequestOptions] = None) -> Asset:
        """Makes a PDF of the pages given, in that order.
        
        Needs the PDF editor on the organisation's plan (403 when it is switched off, 429 when the plan leaves it out), a file within the plan's PDF size (413; 25 MB unless the plan says otherwise), room in its storage (403) and AI allowance left (429).
        
        `POST /api/pdf/split`
        """
        return _pick(self._request("POST", f"/api/pdf/split", query=None, body=body, multipart=False, options=options), "data.asset")  # type: ignore[no-any-return]

    def summarize(self, body: PdfSummarizeBody, *, options: Optional[RequestOptions] = None) -> PdfSummarizeResponseData:
        """Summarises a PDF in plain prose with the platform's AI.
        
        Needs PDF AI on the organisation's plan (403 when switched off) and its AI allowance (429); the file must be within the plan's PDF size (413). Reads the text of the first 30 pages (`truncated` says when that was not all). 422 for a scan without a text layer. Nothing is stored.
        
        `POST /api/pdf/summarize`
        """
        return _pick(self._request("POST", f"/api/pdf/summarize", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def unlock(self, body: PdfUnlockBody, *, options: Optional[RequestOptions] = None) -> Asset:
        """Removes the password of a protected PDF.
        
        Needs the PDF editor on the organisation's plan (403 when it is switched off, 429 when the plan leaves it out), a file within the plan's PDF size (413; 25 MB unless the plan says otherwise), room in its storage (403) and AI allowance left (429). 403 for a wrong password.
        
        `POST /api/pdf/unlock`
        """
        return _pick(self._request("POST", f"/api/pdf/unlock", query=None, body=body, multipart=False, options=options), "data.asset")  # type: ignore[no-any-return]


class PermissionsResource(_Resource):
    """Permissions
    """

    def create(self, body: CreatePermissionInput, *, options: Optional[RequestOptions] = None) -> Permission:
        """Creates a custom permission in an organization, for its own roles to carry.
        
        `POST /api/permissions`
        """
        return self._request("POST", f"/api/permissions", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete(self, permission_id: str, *, options: Optional[RequestOptions] = None) -> PermissionsDeleteResponse:
        """Deletes a custom permission.
        
        `DELETE /api/permissions/{permissionId}`
        """
        return self._request("DELETE", f"/api/permissions/{_seg(permission_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, search: Optional[str] = None, category: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Permission]:
        """Lists the platform's permissions and the custom permissions of the caller's organizations.
        
        With `organizationId`, only what that organization can hold and the caller could grant.
        
        `GET /api/permissions`
        """
        return _pick(self._request("GET", f"/api/permissions", query={"organizationId": organization_id, "search": search, "category": category, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, permission_id: str, body: PermissionsUpdateBody, *, options: Optional[RequestOptions] = None) -> PermissionsUpdateResponse:
        """Changes a custom permission's label, category or description.
        
        `PUT /api/permissions/{permissionId}`
        """
        return self._request("PUT", f"/api/permissions/{_seg(permission_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class PrivacyRequestsResource(_Resource):
    """Privacy requests — Requests by a person who is not a platform user — a contact, a form sender, a guest — to see (access, Art. 15 GDPR) or erase (erasure, Art. 17) what an organisation holds about them, named by their email addresses. A request always covers the whole organisation, hub by hub, so the permissions are asked at organisation level: `privacy:read` sees requests with the addresses masked, `privacy:manage` everything and runs them. Needs privacy requests on the plan. Every step is audited. A request of an organisation where the caller holds no privacy permission answers 404.
    """

    def cancel(self, request_id: str, body: PrivacyRequestsCancelBody, *, options: Optional[RequestOptions] = None) -> PrivacyRequest:
        """Cancels a privacy request that has not run yet.
        
        Needs `privacy:manage` in the request's organisation. Only a request in `draft` or `in_review`; otherwise 409.
        
        `PATCH /api/privacy-requests/{requestId}`
        """
        return _pick(self._request("PATCH", f"/api/privacy-requests/{_seg(request_id)}", query=None, body=body, multipart=False, options=options), "data.request")  # type: ignore[no-any-return]

    def create(self, body: PrivacyRequestsCreateBody, *, options: Optional[RequestOptions] = None) -> PrivacyRequest:
        """Records an access or erasure request for one to ten email addresses.
        
        Needs `privacy:manage`. Nothing is counted yet: that is privacyRequests.preview. It is due 30 days after it was received. Answers 201.
        
        `POST /api/privacy-requests`
        """
        return _pick(self._request("POST", f"/api/privacy-requests", query=None, body=body, multipart=False, options=options), "data.request")  # type: ignore[no-any-return]

    def download_export(self, request_id: str, *, format: Optional[Literal["json", "html", "pdf"]] = None, lang: Optional[Literal["en", "de", "es", "fr"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the export of an access request as JSON, or laid out for the person as HTML or PDF.
        
        Needs `privacy:manage` in the request's organisation. — never `privacy:read`: this is the person's data. Every download is audited and counted. 404 before one was generated; 410 once it expired.
        
        `GET /api/privacy-requests/{requestId}/export`
        """
        return self._request("GET", f"/api/privacy-requests/{_seg(request_id)}/export", query={"format": format, "lang": lang}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def erase(self, request_id: str, body: PrivacyRequestsEraseBody, *, options: Optional[RequestOptions] = None) -> PrivacyRequestsEraseResponseData:
        """Runs the erasure of an erasure request, hub by hub.
        
        Needs `privacy:manage` in the request's organisation. Runs only once the requester's identity was recorded as verified (privacyRequests.verifyIdentity) — otherwise 409. It cannot be undone: `confirm` must be the request's first address. A step that fails returns the request to `in_review`, and running it again repeats only the steps not done; what must be kept (signed evidence, finalized invoices, mail for a person to review …) is counted under `retained`. A completed request answers its result again and changes nothing. 409 while it is running.
        
        `POST /api/privacy-requests/{requestId}/erase`
        """
        return _pick(self._request("POST", f"/api/privacy-requests/{_seg(request_id)}/erase", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def generate_export(self, request_id: str, *, options: Optional[RequestOptions] = None) -> PrivacyRequest:
        """Generates the export of an access request: what every hub holds about the addresses, in one document.
        
        Needs `privacy:manage` in the request's organisation. Runs only once the requester's identity was recorded as verified (privacyRequests.verifyIdentity) — otherwise 409. The export is kept sealed for seven days and the request is completed; its creator is told. When a hub cannot be read nothing is stored: 502 `privacyHubsFailed` with the hubs named in `hubs`.
        
        `POST /api/privacy-requests/{requestId}/export`
        """
        return _pick(self._request("POST", f"/api/privacy-requests/{_seg(request_id)}/export", query=None, body=None, multipart=False, options=options), "data.request")  # type: ignore[no-any-return]

    def get(self, request_id: str, *, options: Optional[RequestOptions] = None) -> PrivacyRequestsGetResponseData:
        """Returns one privacy request, with its counts, its result and its latest export.
        
        Needs `privacy:read`; the addresses and the identity note only with `privacy:manage`.
        
        `GET /api/privacy-requests/{requestId}`
        """
        return _pick(self._request("GET", f"/api/privacy-requests/{_seg(request_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> PrivacyRequestsListResponseData:
        """Lists an organisation's privacy requests.
        
        Needs `privacy:read`; the addresses are masked without `privacy:manage`.
        
        `GET /api/privacy-requests`
        """
        return _pick(self._request("GET", f"/api/privacy-requests", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def preview(self, request_id: str, *, options: Optional[RequestOptions] = None) -> PrivacyRequest:
        """Counts, per hub, what the organisation holds about the request's addresses.
        
        Needs `privacy:manage` in the request's organisation. Counts only, never contents; counted again on every call. Moves a `draft` to `in_review`.
        
        `POST /api/privacy-requests/{requestId}/preview`
        """
        return _pick(self._request("POST", f"/api/privacy-requests/{_seg(request_id)}/preview", query=None, body=None, multipart=False, options=options), "data.request")  # type: ignore[no-any-return]

    def verify_identity(self, request_id: str, body: PrivacyRequestsVerifyIdentityBody, *, options: Optional[RequestOptions] = None) -> PrivacyRequest:
        """Records how the requester's identity was verified.
        
        Needs `privacy:manage` in the request's organisation. Required before the export is generated or the erasure runs. An open request may record it again as a correction; one running or answered only while it has none; a cancelled one never (409). The audit keeps the method, never the note.
        
        `POST /api/privacy-requests/{requestId}/identity`
        """
        return _pick(self._request("POST", f"/api/privacy-requests/{_seg(request_id)}/identity", query=None, body=body, multipart=False, options=options), "data.request")  # type: ignore[no-any-return]


class ProductsCategoriesResource(_Resource):

    def create(self, body: ProductsCategoriesCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductCategory:
        """Creates a product category, at the end of its parent's children unless `position` says otherwise.
        
        Needs `products:create`.
        
        `POST /api/products/categories` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/categories", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "category")  # type: ignore[no-any-return]

    def delete(self, category_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsCategoriesDeleteResponse:
        """Deletes a product category; its children move up to its parent, its products stay without a category.
        
        Needs `products:delete`.
        
        `DELETE /api/products/categories/{categoryId}` — Token permission: `write:products`.
        """
        return self._request("DELETE", f"/api/products/categories/{_seg(category_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[ProductCategory]:
        """Lists every product category the caller sees, flat; `parentId` and `position` make the tree.
        
        `GET /api/products/categories` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/categories", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "categories")  # type: ignore[no-any-return]

    def reorder(self, body: ProductsCategoriesReorderBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[ProductCategory]:
        """Puts the children of a category (or the top level) in this order; children not named follow.
        
        Needs `products:update`. Answers the children in their new order.
        
        `POST /api/products/categories/reorder` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/categories/reorder", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "categories")  # type: ignore[no-any-return]

    def update(self, category_id: str, body: ProductsCategoriesUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductCategory:
        """Renames, moves or re-places a product category.
        
        Needs `products:update`. Never under itself or one of its own children (409 `productCategoryCycle`).
        
        `PATCH /api/products/categories/{categoryId}` — Token permission: `write:products`.
        """
        return _pick(self._request("PATCH", f"/api/products/categories/{_seg(category_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "category")  # type: ignore[no-any-return]


class ProductsCustomerGroupsResource(_Resource):

    def create(self, body: ProductsCustomerGroupsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductCustomerGroup:
        """Creates a customer group.
        
        Needs `products:update` and price lists on the plan. 409 `productDuplicateName` for a name already used.
        
        `POST /api/products/customer-groups` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/customer-groups", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "customerGroup")  # type: ignore[no-any-return]

    def delete(self, group_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsCustomerGroupsDeleteResponse:
        """Deletes a customer group; customers lose it and price lists stop naming it.
        
        Needs `products:update` and price lists on the plan.
        
        `DELETE /api/products/customer-groups/{groupId}` — Token permission: `write:products`.
        """
        return self._request("DELETE", f"/api/products/customer-groups/{_seg(group_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[ProductCustomerGroup]:
        """Lists the organisation's customer groups, which customers carry and price lists name.
        
        `GET /api/products/customer-groups` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/customer-groups", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "customerGroups")  # type: ignore[no-any-return]

    def update(self, group_id: str, body: ProductsCustomerGroupsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductCustomerGroup:
        """Renames or re-places a customer group.
        
        Needs `products:update` and price lists on the plan.
        
        `PATCH /api/products/customer-groups/{groupId}` — Token permission: `write:products`.
        """
        return _pick(self._request("PATCH", f"/api/products/customer-groups/{_seg(group_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "customerGroup")  # type: ignore[no-any-return]


class ProductsInventoryCountsResource(_Resource):

    def cancel(self, count_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventoryCount:
        """Cancels an open stocktaking; nothing was booked.
        
        Needs `products:stock`.
        
        `DELETE /api/products/inventory/counts/{countId}` — Token permission: `write:products`.
        """
        return _pick(self._request("DELETE", f"/api/products/inventory/counts/{_seg(count_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "count")  # type: ignore[no-any-return]

    def create(self, body: ProductsInventoryCountsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventoryCount:
        """Starts a stocktaking: the expected quantities and average costs of every tracked item in scope are frozen now.
        
        Needs `products:stock`. Counting one storage location needs warehouses on the plan. One open count per warehouse (409 `inventoryCountOpen`); counts of different locations may run side by side.
        
        `POST /api/products/inventory/counts` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/counts", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "count")  # type: ignore[no-any-return]

    def enter(self, count_id: str, body: ProductsInventoryCountsEnterBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsInventoryCountsEnterResponse:
        """Enters counted quantities while the stocktaking is open.
        
        Needs `products:stock`. 409 `inventoryCountClosed` once it is posted or cancelled.
        
        `PATCH /api/products/inventory/counts/{countId}` — Token permission: `write:products`.
        """
        return self._request("PATCH", f"/api/products/inventory/counts/{_seg(count_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, count_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsInventoryCountsGetResponse:
        """A stocktaking with its lines.
        
        `GET /api/products/inventory/counts/{countId}` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/inventory/counts/{_seg(count_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InventoryCount]:
        """Lists the stocktakings, newest first.
        
        `GET /api/products/inventory/counts` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/counts", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "counts")  # type: ignore[no-any-return]

    def post(self, count_id: str, body: ProductsInventoryCountsPostBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsInventoryCountsPostResponse:
        """Books a stocktaking: one movement per difference between counted and expected, and the count is closed.
        
        Needs `products:stock`. Lines nobody counted are skipped, or counted as zero. With perpetual valuation each difference is posted against the stock-change account.
        
        `POST /api/products/inventory/counts/{countId}/post` — Token permission: `write:products`.
        """
        return self._request("POST", f"/api/products/inventory/counts/{_seg(count_id)}/post", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def sheet(self, count_id: str, *, organization_id: Optional[str] = None, format: Optional[Literal["csv", "pdf"]] = None, blind: Optional[Literal["1"]] = None, lang: Optional[Literal["de", "en", "es", "fr"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a stocktaking's count sheet as CSV or PDF, with or without the expected quantities.
        
        The CSV uses dot decimals and `;`; the PDF follows the caller's regional settings.
        
        `GET /api/products/inventory/counts/{countId}/sheet` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/inventory/counts/{_seg(count_id)}/sheet", query={"organizationId": organization_id, "format": format, "blind": blind, "lang": lang}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class ProductsInventoryLocationsResource(_Resource):

    def create(self, warehouse_id: str, body: ProductsInventoryLocationsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventoryLocation:
        """Adds a storage location (a bin or shelf) to a warehouse.
        
        Needs `products:stock` and warehouses on the plan. A code already used in the warehouse is refused.
        
        `POST /api/products/inventory/warehouses/{warehouseId}/locations` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/warehouses/{_seg(warehouse_id)}/locations", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "location")  # type: ignore[no-any-return]

    def update(self, location_id: str, body: ProductsInventoryLocationsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventoryLocation:
        """Changes or archives a storage location.
        
        Needs `products:stock` and warehouses on the plan.
        
        `PATCH /api/products/inventory/locations/{locationId}` — Token permission: `write:products`.
        """
        return _pick(self._request("PATCH", f"/api/products/inventory/locations/{_seg(location_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "location")  # type: ignore[no-any-return]


class ProductsInventoryMovementsResource(_Resource):

    def book(self, body: ProductsInventoryMovementsBookBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InventoryMovement]:
        """Books a stock movement by hand: goods in, goods out, a correction or an opening stock.
        
        Needs `products:stock`. Another warehouse than the default, or a storage location, needs warehouses on the plan; batches and serial numbers need them on the plan. A correction gives `quantity` (the change) or `setTo` (the new stock). Refusals: 409 `inventoryInsufficientStock`, 422 `inventorySerialsRequired` / `inventoryBatchRequired`, 409 `inventorySerialNotInStock` / `inventorySerialExists` / `inventoryNotTracked`.
        
        `POST /api/products/inventory/movements` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/movements", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "movements")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, product_id: Optional[str] = None, variant_id: Optional[str] = None, warehouse_id: Optional[str] = None, location_id: Optional[str] = None, kind: Optional[str] = None, source_type: Optional[Literal["delivery_note", "invoice", "credit_note", "cancellation", "purchase_invoice", "stocktaking", "manual", "transfer"]] = None, source_id: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, q: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, format: Optional[Literal["csv"]] = None, options: Optional[RequestOptions] = None) -> List[InventoryMovement]:
        """The stock movements journal, newest first.
        
        `format=csv` downloads the first 500 as a CSV file.
        
        `GET /api/products/inventory/movements` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/movements", query={"organizationId": organization_id, "productId": product_id, "variantId": variant_id, "warehouseId": warehouse_id, "locationId": location_id, "kind": kind, "sourceType": source_type, "sourceId": source_id, "from": from_, "to": to, "q": q, "limit": limit, "offset": offset, "format": format}, body=None, multipart=False, options=options), "movements")  # type: ignore[no-any-return]


class ProductsInventoryReorderRulesResource(_Resource):

    def delete(self, rule_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsInventoryReorderRulesDeleteResponse:
        """Removes a stock item's reorder point in a warehouse.
        
        Needs `products:stock`.
        
        `DELETE /api/products/inventory/reorder-rules/{ruleId}` — Token permission: `write:products`.
        """
        return self._request("DELETE", f"/api/products/inventory/reorder-rules/{_seg(rule_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def save(self, body: ProductsInventoryReorderRulesSaveBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventoryReorderRule:
        """Sets the reorder point of a stock item in a warehouse; a second call changes it.
        
        Needs `products:stock`.
        
        `POST /api/products/inventory/reorder-rules` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/reorder-rules", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "rule")  # type: ignore[no-any-return]


class ProductsInventorySettingsResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventorySettings:
        """Settings → Products → Inventory: the negative-stock policy, returns, and per company when goods go out and how stock is valued.
        
        `GET /api/products/inventory/settings` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/settings", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def update(self, body: ProductsInventorySettingsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventorySettings:
        """Changes the inventory settings.
        
        Needs `products:stock`. Perpetual valuation only with balance-method books (409 `inventoryPerpetualNeedsBalance`).
        
        `PUT /api/products/inventory/settings` — Token permission: `write:products`.
        """
        return _pick(self._request("PUT", f"/api/products/inventory/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class ProductsInventoryWarehousesResource(_Resource):

    def create(self, body: ProductsInventoryWarehousesCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventoryWarehouse:
        """Creates another warehouse.
        
        Needs `products:stock` and warehouses on the plan.
        
        `POST /api/products/inventory/warehouses` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/warehouses", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "warehouse")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, archived: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> List[InventoryWarehouse]:
        """Lists the organisation's warehouses with their storage locations; the default one is made on first use.
        
        `GET /api/products/inventory/warehouses` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/warehouses", query={"organizationId": organization_id, "archived": archived}, body=None, multipart=False, options=options), "warehouses")  # type: ignore[no-any-return]

    def update(self, warehouse_id: str, body: ProductsInventoryWarehousesUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventoryWarehouse:
        """Changes or archives a warehouse.
        
        Needs `products:stock`. Never archives the default warehouse (409 `inventoryDefaultWarehouse`) or one that holds stock (409 `inventoryWarehouseHasStock`). Making another the default needs warehouses on the plan.
        
        `PATCH /api/products/inventory/warehouses/{warehouseId}` — Token permission: `write:products`.
        """
        return _pick(self._request("PATCH", f"/api/products/inventory/warehouses/{_seg(warehouse_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "warehouse")  # type: ignore[no-any-return]


class ProductsInventoryResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.counts = ProductsInventoryCountsResource(request)
        self.locations = ProductsInventoryLocationsResource(request)
        self.movements = ProductsInventoryMovementsResource(request)
        self.reorder_rules = ProductsInventoryReorderRulesResource(request)
        self.settings = ProductsInventorySettingsResource(request)
        self.warehouses = ProductsInventoryWarehousesResource(request)

    def availability(self, body: ProductsInventoryAvailabilityBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[ProductsInventoryAvailabilityResponseLinesItem]:
        """For document lines: whether each product keeps stock, how, and what is on hand and available in the line's warehouse.
        
        Read only. Without a warehouse, the default one.
        
        `POST /api/products/inventory/availability` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/availability", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "lines")  # type: ignore[no-any-return]

    def batches(self, *, organization_id: Optional[str] = None, product_id: str, variant_id: Optional[str] = None, warehouse_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InventoryBatch]:
        """A stock item's batches with best-before date and what is in stock.
        
        Needs `products:read` and batches on the plan.
        
        `GET /api/products/inventory/batches` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/batches", query={"organizationId": organization_id, "productId": product_id, "variantId": variant_id, "warehouseId": warehouse_id}, body=None, multipart=False, options=options), "batches")  # type: ignore[no-any-return]

    def item(self, product_id: str, *, organization_id: Optional[str] = None, variant_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> InventoryItem:
        """A product's stock per warehouse, its batches and serial numbers in stock, and its newest movements.
        
        `GET /api/products/inventory/items/{productId}` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/items/{_seg(product_id)}", query={"organizationId": organization_id, "variantId": variant_id}, body=None, multipart=False, options=options), "item")  # type: ignore[no-any-return]

    def purchase_drafts(self, body: ProductsInventoryPurchaseDraftsBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[ProductsInventoryPurchaseDraftsResponseDraftsItem]:
        """Creates purchase invoice drafts for items below their reorder point: one per supplier last bought from.
        
        Needs `invoicing:create` with purchases on the plan, `products:read` and inventory on the plan. Each line carries the reorder quantity and the last net unit cost.
        
        `POST /api/products/inventory/reorder/purchase-draft` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/reorder/purchase-draft", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "drafts")  # type: ignore[no-any-return]

    def release_reservation(self, body: ProductsInventoryReleaseReservationBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> float:
        """Releases what an order confirmation still reserves, because the order will not be delivered.
        
        Needs `products:stock`.
        
        `POST /api/products/inventory/reservations/release` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/reservations/release", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "released")  # type: ignore[no-any-return]

    def reorder(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InventoryReorderItem]:
        """Stock items at or below their reorder point, with the supplier last bought from and the last net unit cost.
        
        Needs `products:read`. Only products the caller may see; 200 at most.
        
        `GET /api/products/inventory/reorder` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/reorder", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "items")  # type: ignore[no-any-return]

    def serials(self, *, organization_id: Optional[str] = None, product_id: str, variant_id: Optional[str] = None, warehouse_id: Optional[str] = None, status: Optional[Literal["in_stock", "out"]] = None, options: Optional[RequestOptions] = None) -> List[InventorySerial]:
        """A stock item's serial numbers and where they are.
        
        Needs `products:read` and serial numbers on the plan.
        
        `GET /api/products/inventory/serials` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/serials", query={"organizationId": organization_id, "productId": product_id, "variantId": variant_id, "warehouseId": warehouse_id, "status": status}, body=None, multipart=False, options=options), "serials")  # type: ignore[no-any-return]

    def set_tracking(self, product_id: str, body: ProductsInventorySetTrackingBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsInventorySetTrackingResponseItem:
        """Keeps stock for a product (goods only), and how: by quantity, batch or serial number.
        
        Needs `products:stock`; batches and serial numbers need them on the plan. The way changes only while the product holds no stock.
        
        `PUT /api/products/inventory/items/{productId}` — Token permission: `write:products`.
        """
        return _pick(self._request("PUT", f"/api/products/inventory/items/{_seg(product_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "item")  # type: ignore[no-any-return]

    def stock(self, *, organization_id: Optional[str] = None, q: Optional[str] = None, warehouse_id: Optional[str] = None, category_id: Optional[str] = None, below: Optional[Literal["1"]] = None, in_stock: Optional[Literal["1"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, format: Optional[Literal["csv"]] = None, options: Optional[RequestOptions] = None) -> List[InventoryStockRow]:
        """Stock per item and warehouse: quantity, reserved, available, average cost, value and reorder point.
        
        Needs `products:read` and inventory on the plan. `format=csv` downloads the same as a CSV file.
        
        `GET /api/products/inventory/stock` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/stock", query={"organizationId": organization_id, "q": q, "warehouseId": warehouse_id, "categoryId": category_id, "below": below, "inStock": in_stock, "limit": limit, "offset": offset, "format": format}, body=None, multipart=False, options=options), "rows")  # type: ignore[no-any-return]

    def transfer(self, body: ProductsInventoryTransferBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[InventoryMovement]:
        """Moves stock between two warehouses, or between two storage locations of one warehouse, at the source's average cost.
        
        Needs `products:stock` and warehouses on the plan. Nothing is posted to the books.
        
        `POST /api/products/inventory/transfers` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/transfers", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "movements")  # type: ignore[no-any-return]

    def valuation(self, *, organization_id: Optional[str] = None, date: Optional[str] = None, warehouse_id: Optional[str] = None, format: Optional[Literal["csv"]] = None, options: Optional[RequestOptions] = None) -> InventoryValuationReport:
        """The stock's value at a date — quantity times moving average cost per item and warehouse — its total, and per company the value against the stock account in the books.
        
        Needs `products:read`. Every product counts in the totals; one the caller may not see is listed without its name. `format=csv` downloads the rows as a CSV file.
        
        `GET /api/products/inventory/valuation` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/inventory/valuation", query={"organizationId": organization_id, "date": date, "warehouseId": warehouse_id, "format": format}, body=None, multipart=False, options=options), "valuation")  # type: ignore[no-any-return]

    def valuation_closing(self, body: ProductsInventoryValuationClosingBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsInventoryValuationClosingResponseClosing:
        """Posts the periodic closing entry of one company at a date: the value of its warehouses against the stock account.
        
        Needs `products:stock` and `invoicing:bookkeeping`. Once per company and day; balance-method books only (409 `inventoryPerpetualNeedsBalance`).
        
        `POST /api/products/inventory/valuation/closing` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/inventory/valuation/closing", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "closing")  # type: ignore[no-any-return]


class ProductsMarketplaceCouponsResource(_Resource):

    def create(self, body: ProductsMarketplaceCouponsCreateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> MarketplaceCoupon:
        """Creates a discount code of the organisation's seller profile, for all its listings or one of them.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`. 404 `listingNotFound` for a listing that is not the profile's; 409 `codeTaken`.
        
        `POST /api/products/marketplace/coupons` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/marketplace/coupons", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "coupon")  # type: ignore[no-any-return]

    def delete(self, *, organization_id: Optional[str] = None, id: str, options: Optional[RequestOptions] = None) -> ProductsMarketplaceCouponsDeleteResponse:
        """Deletes a discount code of the organisation's seller profile.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`. 404 `marketplaceCouponNotFound` for another seller's code.
        
        `DELETE /api/products/marketplace/coupons` — Token permission: `write:products`.
        """
        return self._request("DELETE", f"/api/products/marketplace/coupons", query={"organizationId": organization_id, "id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[MarketplaceCoupon]:
        """The discount codes of the organisation's seller profile, newest first.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`. Every holder of `marketplace:sell` in the organisation sees the same codes. 200 at most.
        
        `GET /api/products/marketplace/coupons` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/coupons", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "coupons")  # type: ignore[no-any-return]


class ProductsMarketplaceLegalPagesResource(_Resource):

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The shop's legal pages: terms, return policy, privacy, imprint.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`. 404 `sellerProfileRequired` before the shop exists.
        
        `GET /api/products/marketplace/legal-pages` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/legal-pages", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data.legalPages")  # type: ignore[no-any-return]

    def save(self, body: ProductsMarketplaceLegalPagesSaveBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Creates or changes one of the shop's legal pages.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`. The content is HTML, at most 500 KB.
        
        `PUT /api/products/marketplace/legal-pages` — Token permission: `write:products`.
        """
        return _pick(self._request("PUT", f"/api/products/marketplace/legal-pages", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "data.legalPage")  # type: ignore[no-any-return]


class ProductsMarketplaceOrdersResource(_Resource):

    def get(self, order_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """One order of the organisation's listings, with its messages, disputes, refunds and what may still be refunded.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`.
        
        `GET /api/products/marketplace/orders/{orderId}` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/orders/{_seg(order_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "order")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, q: Optional[str] = None, status: Optional[str] = None, tier: Optional[str] = None, from_: Optional[str] = None, to: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The orders of the organisation's listings, newest first (at most 200).
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`. The buyer is named by name and organisation only.
        
        `GET /api/products/marketplace/orders` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/orders", query={"organizationId": organization_id, "q": q, "status": status, "tier": tier, "from": from_, "to": to}, body=None, multipart=False, options=options), "orders")  # type: ignore[no-any-return]

    def message(self, order_id: str, body: ProductsMarketplaceOrdersMessageBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplaceOrdersMessageResponseMessage:
        """Writes to the buyer of an order, as the seller.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`. 1–5,000 characters; a completed or cancelled order takes no more messages.
        
        `POST /api/products/marketplace/orders/{orderId}/messages` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/marketplace/orders/{_seg(order_id)}/messages", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "message")  # type: ignore[no-any-return]

    def refund(self, order_id: str, body: ProductsMarketplaceOrdersRefundBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplaceOrdersRefundResponse:
        """Refunds an order, in full or in part, as a goodwill gesture of the seller.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`. The money goes back from the platform's charge and the seller's share is taken off what it is owed. Refused for an order that is refunded, cancelled, disputed or unpaid, or beyond what is left.
        
        `POST /api/products/marketplace/orders/{orderId}/refund` — Token permission: `write:products`.
        """
        return self._request("POST", f"/api/products/marketplace/orders/{_seg(order_id)}/refund", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class ProductsMarketplacePayoutAccountResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """The organisation's payout account, read fresh from the payment provider: none, pending, ready or restricted.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`.
        
        `GET /api/products/marketplace/payout-account` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/payout-account", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "account")  # type: ignore[no-any-return]

    def onboard(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplacePayoutAccountOnboardResponse:
        """Opens or continues the payout account's onboarding: answers the URL a person must visit in a browser.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`. `url` is null when the account is ready. 404 `sellerProfileRequired` before the shop exists.
        
        `POST /api/products/marketplace/payout-account` — Token permission: `write:products`.
        """
        return self._request("POST", f"/api/products/marketplace/payout-account", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class ProductsMarketplaceReviewsResource(_Resource):

    def list(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The visible reviews of the organisation's listings, newest first, with the seller's responses.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`.
        
        `GET /api/products/marketplace/reviews` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/reviews", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "reviews")  # type: ignore[no-any-return]

    def respond(self, body: ProductsMarketplaceReviewsRespondBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplaceReviewsRespondResponseReview:
        """Responds publicly to a review; an empty response takes it back.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`. 1–2,000 characters.
        
        `PATCH /api/products/marketplace/reviews` — Token permission: `write:products`.
        """
        return _pick(self._request("PATCH", f"/api/products/marketplace/reviews", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "review")  # type: ignore[no-any-return]


class ProductsMarketplaceSettingsResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """The organisation's seller settings: the shop, the trader information, the price mode, what is still missing, and the payout account's state.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`.
        
        `GET /api/products/marketplace/settings` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/settings", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def update(self, body: ProductsMarketplaceSettingsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Saves the seller settings; the first save creates the organisation's seller profile.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`. 422 `marketplaceSellerFieldInvalid` with `field` and `issue`; 409 `marketplaceShopSlugTaken` for a shop address another shop has.
        
        `PUT /api/products/marketplace/settings` — Token permission: `write:products`.
        """
        return _pick(self._request("PUT", f"/api/products/marketplace/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class ProductsMarketplaceResource(_Resource):

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.coupons = ProductsMarketplaceCouponsResource(request)
        self.legal_pages = ProductsMarketplaceLegalPagesResource(request)
        self.orders = ProductsMarketplaceOrdersResource(request)
        self.payout_account = ProductsMarketplacePayoutAccountResource(request)
        self.reviews = ProductsMarketplaceReviewsResource(request)
        self.settings = ProductsMarketplaceSettingsResource(request)

    def bundle_items(self, *, organization_id: Optional[str] = None, listing_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """What a bundle of the organisation can include: its own listings, and whether each may be bundled now.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`, with listings on the plan.
        
        `GET /api/products/marketplace/bundle-items` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/bundle-items", query={"organizationId": organization_id, "listingId": listing_id}, body=None, multipart=False, options=options), "listings")  # type: ignore[no-any-return]

    def get_offer(self, product_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplaceGetOfferResponse:
        """A product's marketplace offer and tiers, where it stands in review, and what still stops a submission.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`, with listings on the plan.
        
        `GET /api/products/{productId}/marketplace` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/{_seg(product_id)}/marketplace", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def offers(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """The organisation's products that have a marketplace offer, with where each stands, its from-price, sales and rating.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`.
        
        `GET /api/products/marketplace/offers` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/offers", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "offers")  # type: ignore[no-any-return]

    def overview(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Seller Central's overview: this month's sales, the next payout, rating, refund rate, the onboarding checklist and the to-dos.
        
        Needs the marketplace switched on by the platform, `products:read`, and `marketplace:sell` or `marketplace:view_payouts` (payout figures only with the latter).
        
        `GET /api/products/marketplace/overview` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/overview", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "overview")  # type: ignore[no-any-return]

    def pause(self, product_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> str:
        """Takes a product out of the marketplace without a review.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`, with listings on the plan. 409 `productMarketplaceNotSubmitted` without an offer.
        
        `POST /api/products/{productId}/marketplace/pause` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/{_seg(product_id)}/marketplace/pause", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "state")  # type: ignore[no-any-return]

    def payouts(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplacePayoutsResponse:
        """The seller's money: per currency what may be paid out now, what is on hold and what is owed back, the schedule, the payouts and the ledger rows not paid out yet.
        
        Needs the marketplace switched on by the platform, `products:read` and `marketplace:view_payouts`.
        
        `GET /api/products/marketplace/payouts` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/marketplace/payouts", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def preview(self, product_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """The offer as a buyer would see it now, in the storefront's shape.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`, with listings on the plan. `preview` is null without an offer.
        
        `GET /api/products/{productId}/marketplace/preview` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/{_seg(product_id)}/marketplace/preview", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "preview")  # type: ignore[no-any-return]

    def questions(self, *, organization_id: Optional[str] = None, status: Optional[Literal["pending", "published", "hidden"]] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """Buyers' questions on all of the organisation's listings, newest first.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`.
        
        `GET /api/products/marketplace/questions` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/questions", query={"organizationId": organization_id, "status": status}, body=None, multipart=False, options=options), "questions")  # type: ignore[no-any-return]

    def resume(self, product_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> str:
        """Shows a paused listing again, without a review.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`, with listings on the plan, room under the plan's listing limit and a product that is not archived.
        
        `POST /api/products/{productId}/marketplace/resume` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/{_seg(product_id)}/marketplace/resume", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "state")  # type: ignore[no-any-return]

    def sales(self, *, organization_id: Optional[str] = None, days: Optional[Literal["7", "30", "90", "365"]] = None, format: Optional[Literal["csv"]] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplaceSalesResponse:
        """The seller's sales per day and currency, gross and the seller's share.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:read`. `format=csv` downloads them as a CSV file.
        
        `GET /api/products/marketplace/sales` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/marketplace/sales", query={"organizationId": organization_id, "days": days, "format": format}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def save_offer(self, product_id: str, body: Dict[str, Any], *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplaceSaveOfferResponse:
        """Creates or changes a product's marketplace offer; an incomplete one may be saved.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`, with listings on the plan. Never goods. `enabled` is not taken here: submit, pause and resume switch it. `tiers` replaces the whole set.
        
        `PUT /api/products/{productId}/marketplace` — Token permission: `write:products`.
        """
        return self._request("PUT", f"/api/products/{_seg(product_id)}/marketplace", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def sources(self, *, organization_id: Optional[str] = None, type_: Literal["project", "page", "shared_block", "builder_block", "workflow", "database", "endpoint"], q: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Dict[str, Any]]:
        """What an offer of the organisation can deliver — its projects, pages, blocks, workflows, databases or endpoints — by name.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`, with listings on the plan. A first filter only: whether the caller may offer the one picked is checked on submission.
        
        `GET /api/products/marketplace/sources` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/sources", query={"organizationId": organization_id, "type": type_, "q": q}, body=None, multipart=False, options=options), "sources")  # type: ignore[no-any-return]

    def statement(self, payout_id: str, *, organization_id: Optional[str] = None, format: Optional[Literal["csv", "pdf", "fee-pdf"]] = None, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """The settlement statement of one payout: every ledger row it settled and their sums.
        
        Needs the marketplace switched on by the platform, `products:read` and `marketplace:view_payouts`. `format=csv` downloads it for the books; `pdf` the archived statement; `fee-pdf` the platform's fee invoice.
        
        `GET /api/products/marketplace/statements/{payoutId}` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/marketplace/statements/{_seg(payout_id)}", query={"organizationId": organization_id, "format": format}, body=None, multipart=False, options=options), "statement")  # type: ignore[no-any-return]

    def submit(self, product_id: str, body: ProductsMarketplaceSubmitBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsMarketplaceSubmitResponse:
        """Submits a product's offer for the marketplace's review.
        
        Needs the marketplace switched on by the platform, the `marketplace:sell` permission and `products:update`, with listings on the plan, and a verified e-mail address. 422 `productMarketplaceOfferInvalid` with `issues` while anything is missing; 409 `productMarketplaceNothingChanged` when what is live is what would be submitted. One open submission per offer: a second replaces the first.
        
        `POST /api/products/{productId}/marketplace/submit` — Token permission: `write:products`.
        """
        return self._request("POST", f"/api/products/{_seg(product_id)}/marketplace/submit", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class ProductsPriceListsResource(_Resource):

    def create(self, body: ProductPriceListInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductPriceList:
        """Creates a price list.
        
        Needs `products:update` and price lists on the plan.
        
        `POST /api/products/price-lists` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products/price-lists", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "priceList")  # type: ignore[no-any-return]

    def delete(self, price_list_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsPriceListsDeleteResponse:
        """Deletes a price list and its prices; document lines it priced keep their price.
        
        Needs `products:delete` and price lists on the plan.
        
        `DELETE /api/products/price-lists/{priceListId}` — Token permission: `write:products`.
        """
        return self._request("DELETE", f"/api/products/price-lists/{_seg(price_list_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def export(self, price_list_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a price list's prices as a CSV file.
        
        Needs `products:export`. Columns: product_number; product_name; variant_sku; variant; min_quantity; price.
        
        `GET /api/products/price-lists/{priceListId}/export` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/price-lists/{_seg(price_list_id)}/export", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, price_list_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsPriceListsGetResponse:
        """A price list and its prices for the products the caller sees.
        
        `GET /api/products/price-lists/{priceListId}` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/price-lists/{_seg(price_list_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def import_(self, price_list_id: str, body: ProductCsvImportInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsPriceListsImportResponse:
        """Imports prices into a price list from a CSV file: a preview first, then the write with `apply`.
        
        Needs `products:update` and price lists on the plan. With `apply`, the tiers of every item the file names are replaced by the file's; every other price stays.
        
        `POST /api/products/price-lists/{priceListId}/import` — Token permission: `write:products`.
        """
        return self._request("POST", f"/api/products/price-lists/{_seg(price_list_id)}/import", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, archived: Optional[Literal["active", "archived", "all"]] = None, options: Optional[RequestOptions] = None) -> List[ProductPriceList]:
        """Lists the organisation's price lists, with how many prices each holds, and its customer groups.
        
        `GET /api/products/price-lists` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/price-lists", query={"organizationId": organization_id, "archived": archived}, body=None, multipart=False, options=options), "priceLists")  # type: ignore[no-any-return]

    def set_prices(self, price_list_id: str, body: ProductsPriceListsSetPricesBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[ProductPrice]:
        """Replaces a price list's prices for every product the caller sees.
        
        Needs `products:update` and price lists on the plan. Prices of products the caller does not see stay. All or nothing: the same item and from-quantity twice is 409 `productDuplicateName`.
        
        `PUT /api/products/price-lists/{priceListId}/prices` — Token permission: `write:products`.
        """
        return _pick(self._request("PUT", f"/api/products/price-lists/{_seg(price_list_id)}/prices", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "prices")  # type: ignore[no-any-return]

    def update(self, price_list_id: str, body: ProductPriceListInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductPriceList:
        """Changes a price list.
        
        Needs `products:update` and price lists on the plan.
        
        `PATCH /api/products/price-lists/{priceListId}` — Token permission: `write:products`.
        """
        return _pick(self._request("PATCH", f"/api/products/price-lists/{_seg(price_list_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "priceList")  # type: ignore[no-any-return]


class ProductsSettingsResource(_Resource):

    def get(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductSettings:
        """Settings → Products: what a new product starts with, and the number prefix.
        
        `GET /api/products/settings` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/settings", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]

    def update(self, body: ProductsSettingsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductSettings:
        """Changes Settings → Products.
        
        Needs `products:update`.
        
        `PATCH /api/products/settings` — Token permission: `write:products`.
        """
        return _pick(self._request("PATCH", f"/api/products/settings", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class ProductsVariantsResource(_Resource):

    def export(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads every variant of the products the caller sees as a CSV file.
        
        Needs `products:export`. Columns: product_number; product_name; sku; options; gtin; unit_price; weight_kg; archived.
        
        `GET /api/products/variants/export` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/variants/export", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, product_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsVariantsGetResponse:
        """A product's options with their values, and its variants (archived ones too).
        
        `GET /api/products/{productId}/variants` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/{_seg(product_id)}/variants", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def import_(self, body: ProductCsvImportInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsVariantsImportResponse:
        """Imports variants from a CSV file: a preview first, then the write with `apply`.
        
        Needs `products:update` and variants on the plan. With `apply`, 422 `productImportInvalid` while rows have errors unless `skipInvalid`.
        
        `POST /api/products/variants/import` — Token permission: `write:products`.
        """
        return self._request("POST", f"/api/products/variants/import", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def set_options(self, product_id: str, body: ProductsVariantsSetOptionsBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsVariantsSetOptionsResponse:
        """Replaces a product's options; the variants follow, and the missing combinations are created.
        
        Needs `products:update` and variants on the plan. A removed value archives the variants with it; a new option gives every variant its first value. At most 100 active variants per product (422 `productVariantLimit`).
        
        `PUT /api/products/{productId}/variants` — Token permission: `write:products`.
        """
        return self._request("PUT", f"/api/products/{_seg(product_id)}/variants", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, product_id: str, body: ProductsVariantsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsVariantsUpdateResponse:
        """Changes several variants of a product at once, all or nothing.
        
        Needs `products:update` and variants on the plan. A SKU must be free among the organisation's product numbers and SKUs (409 `productSkuTaken`); a GTIN valid (422 `productInvalidGtin`).
        
        `PATCH /api/products/{productId}/variants` — Token permission: `write:products`.
        """
        return self._request("PATCH", f"/api/products/{_seg(product_id)}/variants", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class ProductsResource(_Resource):
    """Products — The organisation's product catalogue — products, categories, variants, price lists, the CSV import and export — its stock, and its offers in the marketplace. Every operation works in one organisation (`organizationId`) and needs the role's `products:*` permissions held at organisation level.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.categories = ProductsCategoriesResource(request)
        self.customer_groups = ProductsCustomerGroupsResource(request)
        self.inventory = ProductsInventoryResource(request)
        self.marketplace = ProductsMarketplaceResource(request)
        self.price_lists = ProductsPriceListsResource(request)
        self.settings = ProductsSettingsResource(request)
        self.variants = ProductsVariantsResource(request)

    def create(self, body: ProductInput, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Product:
        """Creates a product.
        
        Needs `products:create`. Counts against the plan's product limit (archived ones do not).
        
        `POST /api/products` — Token permission: `write:products`.
        """
        return _pick(self._request("POST", f"/api/products", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "product")  # type: ignore[no-any-return]

    def delete(self, product_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsDeleteResponse:
        """Moves a product to the trash.
        
        Needs `products:delete`. Allowed while documents name the product: an invoicing line keeps its own copy and only loses the link. Its marketplace offer pauses at once; its number stays reserved.
        
        `DELETE /api/products/{productId}` — Token permission: `write:products`.
        """
        return self._request("DELETE", f"/api/products/{_seg(product_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def export(self, *, organization_id: Optional[str] = None, archived: Optional[Literal["active", "archived", "all"]] = None, q: Optional[str] = None, kind: Optional[Literal["goods", "service", "digital"]] = None, category_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the products the caller sees as a CSV file, filtered like the list.
        
        Needs `products:export`. Semicolon-separated with a BOM; the category as its path; at most 20,000 rows, by name.
        
        `GET /api/products/export` — Token permission: `read:products`.
        """
        return self._request("GET", f"/api/products/export", query={"organizationId": organization_id, "archived": archived, "q": q, "kind": kind, "categoryId": category_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, product_id: str, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Product:
        """One product.
        
        `GET /api/products/{productId}` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/{_seg(product_id)}", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "product")  # type: ignore[no-any-return]

    def import_(self, body: ProductsImportBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProductsImportResponse:
        """Imports products from a CSV file: a preview first, then the write with `apply`.
        
        Needs `products:create`; a file that updates existing products (matched by number) also needs `products:update`. With `apply`, 422 `productImportInvalid` while rows have errors unless `skipInvalid`, and the plan's product limit applies.
        
        `POST /api/products/import` — Token permission: `write:products`.
        """
        return self._request("POST", f"/api/products/import", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, q: Optional[str] = None, kind: Optional[Literal["goods", "service", "digital"]] = None, category_id: Optional[str] = None, archived: Optional[Literal["active", "archived", "all"]] = None, sort: Optional[Literal["name", "number", "price", "updated"]] = None, group: Optional[Literal["category"]] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Product]:
        """Lists one page of the products the caller sees, with the total and how many sit in each category.
        
        Needs `products:read`.
        
        `GET /api/products` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products", query={"organizationId": organization_id, "q": q, "kind": kind, "categoryId": category_id, "archived": archived, "sort": sort, "group": group, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "products")  # type: ignore[no-any-return]

    def next_number(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> str:
        """Suggests a number for a new product: the highest in use with Settings → Products' prefix, plus one.
        
        Needs `products:create`. Not a reservation — creating with a number already taken answers 409 `productNumberTaken`.
        
        `GET /api/products/next-number` — Token permission: `read:products`.
        """
        return _pick(self._request("GET", f"/api/products/next-number", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "number")  # type: ignore[no-any-return]

    def update(self, product_id: str, body: ProductsUpdateBody, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Product:
        """Changes a product, or archives and restores it with `archived`.
        
        Needs `products:update`. Restoring counts against the plan's product limit again. Who sees it (`visibility`, `workspaceId`) is changed only by its creator or a holder of `products:delete`.
        
        `PATCH /api/products/{productId}` — Token permission: `write:products`.
        """
        return _pick(self._request("PATCH", f"/api/products/{_seg(product_id)}", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "product")  # type: ignore[no-any-return]


class ProjectsContentGapsResource(_Resource):

    def faq(self, project_id: str, topic_id: str, body: ProjectsContentGapsFaqBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Suggests an FAQ entry for a content-gap topic, or adds one to the page's draft.
        
        Without `apply` the AI drafts a question and answer (rate-limited). With `apply: true` the given `question` and `answer` are added to the page's draft and the topic is marked `faq_added`.
        
        `POST /api/projects/{projectId}/content-gaps/{topicId}/faq` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/content-gaps/{_seg(topic_id)}/faq", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, project_id: str, *, page_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProjectsContentGapsListResponseData:
        """Lists the questions visitors ask that the site does not answer yet.
        
        `GET /api/projects/{projectId}/content-gaps` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/content-gaps", query={"pageId": page_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, project_id: str, topic_id: str, body: ProjectsContentGapsUpdateBody, *, options: Optional[RequestOptions] = None) -> ProjectsContentGapsUpdateResponseData:
        """Dismisses a content-gap topic, marks it answered, or reopens it.
        
        `POST /api/projects/{projectId}/content-gaps/{topicId}` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/content-gaps/{_seg(topic_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ProjectsCookiesResource(_Resource):

    def create(self, project_id: str, body: ProjectCookieInput, *, options: Optional[RequestOptions] = None) -> ProjectCookie:
        """Declares a cookie on the project's banner.
        
        `POST /api/projects/{projectId}/cookies/cookies` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/cookies/cookies", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_category(self, project_id: str, body: CookieCategoryInput, *, options: Optional[RequestOptions] = None) -> CookieCategory:
        """Adds a cookie category to the project's banner.
        
        `POST /api/projects/{projectId}/cookies/categories` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/cookies/categories", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, project_id: str, cookie_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsCookiesDeleteResponseData:
        """Removes a declared cookie.
        
        `DELETE /api/projects/{projectId}/cookies/cookies/{cookieId}` — Token permission: `delete:projects`.
        """
        return _pick(self._request("DELETE", f"/api/projects/{_seg(project_id)}/cookies/cookies/{_seg(cookie_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_category(self, project_id: str, category_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsCookiesDeleteCategoryResponseData:
        """Removes a cookie category.
        
        `DELETE /api/projects/{projectId}/cookies/categories/{categoryId}` — Token permission: `delete:projects`.
        """
        return _pick(self._request("DELETE", f"/api/projects/{_seg(project_id)}/cookies/categories/{_seg(category_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_scan(self, project_id: str, job_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsCookiesGetScanResponseData:
        """Returns how a cookie scan is going, and its findings when done.
        
        `GET /api/projects/{projectId}/cookies/scan/{jobId}` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/cookies/scan/{_seg(job_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_settings(self, project_id: str, *, options: Optional[RequestOptions] = None) -> CookieBannerSettings:
        """Returns the project's cookie banner settings.
        
        `GET /api/projects/{projectId}/cookies/settings` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/cookies/settings", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[ProjectCookie]:
        """Lists the cookies and storage the project's banner declares.
        
        `GET /api/projects/{projectId}/cookies/cookies` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/cookies/cookies", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_categories(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[CookieCategory]:
        """Lists the cookie categories visitors consent to on the project's banner.
        
        `GET /api/projects/{projectId}/cookies/categories` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/cookies/categories", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_consents(self, project_id: str, *, page: Optional[int] = None, page_size: Optional[int] = None, country: Optional[str] = None, since_days: Optional[int] = None, options: Optional[RequestOptions] = None) -> ProjectsCookiesListConsentsResponseData:
        """Lists the consent records visitors left on the project's banner, with totals.
        
        `GET /api/projects/{projectId}/cookies/consents` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/cookies/consents", query={"page": page, "pageSize": page_size, "country": country, "sinceDays": since_days}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def scan(self, project_id: str, body: ProjectsCookiesScanBody, *, options: Optional[RequestOptions] = None) -> ProjectsCookiesScanResponseData:
        """Starts a scan of the live site's pages for the cookies and storage they set.
        
        Runs in the background; poll `projects.cookies.getScan` with the `jobId`.
        
        `POST /api/projects/{projectId}/cookies/scan` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/cookies/scan", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def seed(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsCookiesSeedResponseData:
        """Adds the standard cookie categories and the platform's own cookies where they are missing.
        
        `POST /api/projects/{projectId}/cookies/seed` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/cookies/seed", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, project_id: str, cookie_id: str, body: ProjectsCookiesUpdateBody, *, options: Optional[RequestOptions] = None) -> ProjectCookie:
        """Changes a declared cookie; only the fields sent change.
        
        `PUT /api/projects/{projectId}/cookies/cookies/{cookieId}` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/cookies/cookies/{_seg(cookie_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_category(self, project_id: str, category_id: str, body: ProjectsCookiesUpdateCategoryBody, *, options: Optional[RequestOptions] = None) -> CookieCategory:
        """Changes a cookie category; only the fields sent change.
        
        `PUT /api/projects/{projectId}/cookies/categories/{categoryId}` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/cookies/categories/{_seg(category_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_settings(self, project_id: str, body: ProjectsCookiesUpdateSettingsBody, *, options: Optional[RequestOptions] = None) -> CookieBannerSettings:
        """Changes the project's cookie banner settings; only the fields sent change.
        
        Raise `consentVersion` to ask every visitor again.
        
        `PUT /api/projects/{projectId}/cookies/settings` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/cookies/settings", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ProjectsEmailTemplatesResource(_Resource):

    def list(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsEmailTemplatesListResponseData:
        """Lists the visitor emails the project may word itself, in each of its languages, with the wording that is sent.
        
        `GET /api/projects/{projectId}/email-templates` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/email-templates", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def reset(self, project_id: str, type_: str, *, locale: str, options: Optional[RequestOptions] = None) -> ProjectsEmailTemplatesResetResponse:
        """Goes back to the platform's wording of a visitor email in one language.
        
        `DELETE /api/projects/{projectId}/email-templates/{type}` — Token permission: `delete:projects`.
        """
        return self._request("DELETE", f"/api/projects/{_seg(project_id)}/email-templates/{_seg(type_)}", query={"locale": locale}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set(self, project_id: str, type_: str, body: EmailTemplateInput, *, options: Optional[RequestOptions] = None) -> ProjectsEmailTemplatesSetResponse:
        """Saves the project's own wording of a visitor email in one language.
        
        Needs the plan's custom email templates. The HTML is cleaned: no scripts, no event handlers, only http(s) and mailto links.
        
        `PUT /api/projects/{projectId}/email-templates/{type}` — Token permission: `write:projects`.
        """
        return self._request("PUT", f"/api/projects/{_seg(project_id)}/email-templates/{_seg(type_)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class ProjectsJourneysResource(_Resource):

    def get_settings(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsJourneysGetSettingsResponseData:
        """Returns the project's visitor-journey settings, what applies in each region, and the platform's limits.
        
        Needs `project.tracking`.
        
        `GET /api/projects/{projectId}/journeys/settings` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/journeys/settings", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_visitor(self, project_id: str, visitor_id: str, *, options: Optional[RequestOptions] = None) -> JourneyVisitor:
        """Returns one visitor's journey: visits, touches, consent and conversions.
        
        `GET /api/projects/{projectId}/journeys/visitors/{visitorId}` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/journeys/visitors/{_seg(visitor_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_deliveries(self, project_id: str, *, status: Optional[Literal["queued", "sent", "failed", "skipped"]] = None, network: Optional[Literal["meta", "google_ads", "tiktok", "linkedin"]] = None, source: Optional[Literal["web", "offline"]] = None, page: Optional[int] = None, options: Optional[RequestOptions] = None) -> ProjectsJourneysListDeliveriesResponseData:
        """Lists the conversions sent, or due to be sent, to ad networks, with each network's answer.
        
        `GET /api/projects/{projectId}/journeys/deliveries` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/journeys/deliveries", query={"status": status, "network": network, "source": source, "page": page}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_visitors(self, project_id: str, *, from_: str, to: str, q: Optional[str] = None, linked: Optional[Literal["all", "linked", "unlinked"]] = None, source: Optional[str] = None, page: Optional[int] = None, page_size: Optional[int] = None, options: Optional[RequestOptions] = None) -> ProjectsJourneysListVisitorsResponseData:
        """Lists the visitors of a period with their first and last touch and conversions.
        
        `GET /api/projects/{projectId}/journeys/visitors` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/journeys/visitors", query={"from": from_, "to": to, "q": q, "linked": linked, "source": source, "page": page, "pageSize": page_size}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def report(self, project_id: str, *, from_: str, to: str, model: Optional[Literal["first", "last", "linear"]] = None, group: Optional[Literal["channel", "campaign"]] = None, options: Optional[RequestOptions] = None) -> JourneyReport:
        """Returns visitors, conversions and revenue of a period, credited to channels or campaigns by an attribution model.
        
        `GET /api/projects/{projectId}/journeys/report` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/journeys/report", query={"from": from_, "to": to, "model": model, "group": group}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_settings(self, project_id: str, body: Dict[str, Any], *, options: Optional[RequestOptions] = None) -> ProjectsJourneysUpdateSettingsResponseData:
        """Changes the project's visitor-journey settings.
        
        Needs `project.tracking`. Send only the keys to change, in the shape of `settings` as read; the platform's locks still apply. `changed` lists what moved.
        
        `PUT /api/projects/{projectId}/journeys/settings` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/journeys/settings", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ProjectsPageFoldersResource(_Resource):

    def create(self, project_id: str, body: ProjectsPageFoldersCreateBody, *, options: Optional[RequestOptions] = None) -> PageFolder:
        """Creates a folder in a project's pages list; no URL changes.
        
        `POST /api/projects/{projectId}/page-folders` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/page-folders", query=None, body=body, multipart=False, options=options), "data.folder")  # type: ignore[no-any-return]

    def delete(self, project_id: str, folder_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsPageFoldersDeleteResponse:
        """Deletes a folder of a project's pages list; its pages move to no folder and nothing else changes.
        
        `DELETE /api/projects/{projectId}/page-folders/{folderId}` — Token permission: `delete:projects`.
        """
        return self._request("DELETE", f"/api/projects/{_seg(project_id)}/page-folders/{_seg(folder_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[PageFolder]:
        """Lists the folders of a project's pages list.
        
        `GET /api/projects/{projectId}/page-folders` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/page-folders", query=None, body=None, multipart=False, options=options), "data.folders")  # type: ignore[no-any-return]

    def move(self, project_id: str, body: ProjectsPageFoldersMoveBody, *, options: Optional[RequestOptions] = None) -> float:
        """Files up to 500 pages, with their language versions, in a folder — or in none.
        
        `POST /api/projects/{projectId}/page-folders/move` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/page-folders/move", query=None, body=body, multipart=False, options=options), "data.moved")  # type: ignore[no-any-return]

    def update(self, project_id: str, folder_id: str, body: ProjectsPageFoldersUpdateBody, *, options: Optional[RequestOptions] = None) -> PageFolder:
        """Renames or moves a folder of a project's pages list.
        
        `PATCH /api/projects/{projectId}/page-folders/{folderId}` — Token permission: `write:projects`.
        """
        return _pick(self._request("PATCH", f"/api/projects/{_seg(project_id)}/page-folders/{_seg(folder_id)}", query=None, body=body, multipart=False, options=options), "data.folder")  # type: ignore[no-any-return]


class ProjectsRedirectsResource(_Resource):

    def create(self, project_id: str, body: ProjectRedirectInput, *, options: Optional[RequestOptions] = None) -> ProjectRedirect:
        """Adds a redirect from an old path to a page, a path or another site.
        
        `POST /api/projects/{projectId}/redirects` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/redirects", query=None, body=body, multipart=False, options=options), "data.redirect")  # type: ignore[no-any-return]

    def delete(self, project_id: str, redirect_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsRedirectsDeleteResponseData:
        """Removes a redirect.
        
        `DELETE /api/projects/{projectId}/redirects/{redirectId}` — Token permission: `delete:projects`.
        """
        return _pick(self._request("DELETE", f"/api/projects/{_seg(project_id)}/redirects/{_seg(redirect_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[ProjectRedirect]:
        """Lists a project's redirects with their hits, and the pages one can point at.
        
        Redirects answer only where no live page does; at most 1000 per project.
        
        `GET /api/projects/{projectId}/redirects` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/redirects", query=None, body=None, multipart=False, options=options), "data.redirects")  # type: ignore[no-any-return]

    def update(self, project_id: str, redirect_id: str, body: ProjectsRedirectsUpdateBody, *, options: Optional[RequestOptions] = None) -> ProjectRedirect:
        """Changes a redirect; an automatic one given a new target or old path becomes a manual one.
        
        `PATCH /api/projects/{projectId}/redirects/{redirectId}` — Token permission: `write:projects`.
        """
        return _pick(self._request("PATCH", f"/api/projects/{_seg(project_id)}/redirects/{_seg(redirect_id)}", query=None, body=body, multipart=False, options=options), "data.redirect")  # type: ignore[no-any-return]


class ProjectsResultsResource(_Resource):

    def audiences(self, project_id: str, *, range: Optional[Literal["7d", "30d", "90d", "custom"]] = None, from_: Optional[str] = None, to: Optional[str] = None, page_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProjectsResultsAudiencesResponseData:
        """Returns the site results split by audience (new or returning, device, source), for every page or one.
        
        `GET /api/projects/{projectId}/results/audiences` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/results/audiences", query={"range": range, "from": from_, "to": to, "pageId": page_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def engagement(self, project_id: str, *, range: Optional[Literal["7d", "30d", "90d", "custom"]] = None, from_: Optional[str] = None, to: Optional[str] = None, page_id: str, options: Optional[RequestOptions] = None) -> ProjectsResultsEngagementResponseData:
        """Returns how long visitors stayed on a page and how far they scrolled.
        
        `GET /api/projects/{projectId}/results/engagement` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/results/engagement", query={"range": range, "from": from_, "to": to, "pageId": page_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, project_id: str, *, range: Optional[Literal["7d", "30d", "90d", "custom"]] = None, from_: Optional[str] = None, to: Optional[str] = None, page_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProjectsResultsGetResponseData:
        """Returns the site results — views, blocks seen, clicks and outcomes — of every page, or of one page's blocks.
        
        `GET /api/projects/{projectId}/results` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/results", query={"range": range, "from": from_, "to": to, "pageId": page_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def impact(self, project_id: str, *, page_id: str, change_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ProjectsResultsImpactResponseData:
        """Returns how a page's results changed after each of its last publishes, or after one.
        
        `GET /api/projects/{projectId}/results/impact` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/results/impact", query={"pageId": page_id, "changeId": change_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_settings(self, project_id: str, body: ProjectsResultsUpdateSettingsBody, *, options: Optional[RequestOptions] = None) -> ProjectsResultsUpdateSettingsResponseData:
        """Turns audience results on or off for every page of the project.
        
        `PUT /api/projects/{projectId}/site-results-settings` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/site-results-settings", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ProjectsSharedBlocksResource(_Resource):

    def create(self, project_id: str, body: ProjectsSharedBlocksCreateBody, *, options: Optional[RequestOptions] = None) -> SharedBlock:
        """Creates a shared block from a component tree.
        
        Needs `component.create`. The block is a draft until published with `projects.sharedBlocks.publish`.
        
        `POST /api/projects/{projectId}/shared-blocks` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/shared-blocks", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, project_id: str, block_id: str, *, force: Optional[Literal["true"]] = None, options: Optional[RequestOptions] = None) -> ProjectsSharedBlocksDeleteResponseData:
        """Moves a shared block to the trash.
        
        Refused with 409 while pages still use it, unless `force=true` — then those pages lose the block.
        
        `DELETE /api/projects/{projectId}/shared-blocks/{blockId}` — Token permission: `delete:projects`.
        """
        return _pick(self._request("DELETE", f"/api/projects/{_seg(project_id)}/shared-blocks/{_seg(block_id)}", query={"force": force}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, project_id: str, block_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsSharedBlocksGetResponseData:
        """Returns a shared block with its published versions and how many pages use it.
        
        `GET /api/projects/{projectId}/shared-blocks/{blockId}` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/shared-blocks/{_seg(block_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_version(self, project_id: str, block_id: str, version_id: str, *, options: Optional[RequestOptions] = None) -> SharedBlockVersion:
        """Returns one published version of a shared block, with its tree.
        
        `GET /api/projects/{projectId}/shared-blocks/{blockId}/versions/{versionId}` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/shared-blocks/{_seg(block_id)}/versions/{_seg(version_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, project_id: str, *, include: Optional[Literal["trees"]] = None, options: Optional[RequestOptions] = None) -> List[SharedBlockSummary]:
        """Lists a project's shared blocks — a header, footer or section used on many pages.
        
        `GET /api/projects/{projectId}/shared-blocks` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/shared-blocks", query={"include": include}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def publish(self, project_id: str, block_id: str, body: ProjectsSharedBlocksPublishBody, *, options: Optional[RequestOptions] = None) -> ProjectsSharedBlocksPublishResponseData:
        """Publishes a shared block's draft as a new version, which the pages using it then show.
        
        `POST /api/projects/{projectId}/shared-blocks/{blockId}/publish` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/shared-blocks/{_seg(block_id)}/publish", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, project_id: str, block_id: str, body: ProjectsSharedBlocksUpdateBody, *, options: Optional[RequestOptions] = None) -> SharedBlock:
        """Changes a shared block's name, description or draft tree.
        
        Nothing live changes until the block is published.
        
        `PATCH /api/projects/{projectId}/shared-blocks/{blockId}` — Token permission: `write:projects`.
        """
        return _pick(self._request("PATCH", f"/api/projects/{_seg(project_id)}/shared-blocks/{_seg(block_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ProjectsSiteHealthResource(_Resource):

    def check(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsSiteHealthCheckResponseData:
        """Checks the project's site now and returns the findings.
        
        Needs `page.update`; rate-limited.
        
        `POST /api/projects/{projectId}/site-health/check` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/site-health/check", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def dismiss(self, project_id: str, finding_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsSiteHealthDismissResponseData:
        """Dismisses a site-health finding.
        
        `POST /api/projects/{projectId}/site-health/{findingId}/dismiss` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/site-health/{_seg(finding_id)}/dismiss", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, project_id: str, *, page_id: Optional[str] = None, dismissed: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> ProjectsSiteHealthGetResponseData:
        """Returns the problems found on the project's live site — broken links, missing texts and the like.
        
        `GET /api/projects/{projectId}/site-health` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/site-health", query={"pageId": page_id, "dismissed": dismissed}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ProjectsSpamProtectionResource(_Resource):

    def get(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsSpamProtectionGetResponseData:
        """Returns how the project's forms are protected from spam, what applies, and what the platform allows.
        
        A provider's secret is never answered, only whether one is stored.
        
        `GET /api/projects/{projectId}/spam-protection` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/spam-protection", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, project_id: str, body: ProjectsSpamProtectionUpdateBody, *, options: Optional[RequestOptions] = None) -> ProjectsSpamProtectionUpdateResponseData:
        """Changes how the project's forms are protected from spam; only the fields sent change.
        
        `PUT /api/projects/{projectId}/spam-protection` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/spam-protection", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ProjectsWaitlistResource(_Resource):

    def delete_signup(self, project_id: str, signup_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsWaitlistDeleteSignupResponse:
        """Erases a waitlist sign-up with its consent record.
        
        `DELETE /api/projects/{projectId}/waitlist/{signupId}` — Token permission: `delete:projects`.
        """
        return self._request("DELETE", f"/api/projects/{_seg(project_id)}/waitlist/{_seg(signup_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def export(self, project_id: str, *, page_id: Optional[str] = None, block_id: Optional[str] = None, status: Optional[Literal["pending", "confirmed", "withdrawn"]] = None, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the project's waitlist sign-ups, with their consent records, as a CSV file.
        
        Needs `project.update`; at most 50,000 rows; written to the audit log. Answers the file itself (`text/csv`).
        
        `GET /api/projects/{projectId}/waitlist/export` — Token permission: `read:projects`.
        """
        return self._request("GET", f"/api/projects/{_seg(project_id)}/waitlist/export", query={"pageId": page_id, "blockId": block_id, "status": status, "q": q}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, project_id: str, *, page_id: Optional[str] = None, block_id: Optional[str] = None, status: Optional[Literal["pending", "confirmed", "withdrawn"]] = None, q: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> ProjectsWaitlistListResponseData:
        """Lists the project's waitlist blocks with their counts, and one page of sign-ups.
        
        `GET /api/projects/{projectId}/waitlist` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/waitlist", query={"pageId": page_id, "blockId": block_id, "status": status, "q": q, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ProjectsResource(_Resource):
    """Projects
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.content_gaps = ProjectsContentGapsResource(request)
        self.cookies = ProjectsCookiesResource(request)
        self.email_templates = ProjectsEmailTemplatesResource(request)
        self.journeys = ProjectsJourneysResource(request)
        self.page_folders = ProjectsPageFoldersResource(request)
        self.redirects = ProjectsRedirectsResource(request)
        self.results = ProjectsResultsResource(request)
        self.shared_blocks = ProjectsSharedBlocksResource(request)
        self.site_health = ProjectsSiteHealthResource(request)
        self.spam_protection = ProjectsSpamProtectionResource(request)
        self.waitlist = ProjectsWaitlistResource(request)

    def add_domain(self, project_id: str, body: AddDomainInput, *, options: Optional[RequestOptions] = None) -> ProjectDomain:
        """Claims a custom hostname for a project.
        
        The hostname is served only after verification (`projects.verifyDomain`): the answer's `dnsRecords` say what to create at the DNS provider. Refused for a hostname another project holds or one under the platform's own domains; needs a verified email.
        
        `POST /api/projects/{projectId}/domains` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/domains", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def add_language(self, project_id: str, body: ProjectsAddLanguageBody, *, options: Optional[RequestOptions] = None) -> ProjectLanguage:
        """Adds a language to a project.
        
        `POST /api/projects/{projectId}/languages` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/languages", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def analytics(self, project_id: str, *, days: Optional[int] = None, options: Optional[RequestOptions] = None) -> ProjectAnalytics:
        """Returns a project's page views, clicks, conversions and per-page figures for a period.
        
        `GET /api/projects/{projectId}/analytics` — Token permission: `read:projects`.
        """
        return self._request("GET", f"/api/projects/{_seg(project_id)}/analytics", query={"days": days}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def claim_platform_domain(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectDomain:
        """Gives the project its free platform subdomain, if it has none yet.
        
        `POST /api/projects/{projectId}/domains/platform` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/domains/platform", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: CreateProjectInput, *, options: Optional[RequestOptions] = None) -> Project:
        """Creates a project in a workspace.
        
        Needs `project.create` and access to the workspace; counts against the plan's `max_projects`. The project gets its free platform subdomain and the default cookie categories.
        
        `POST /api/projects` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create_comment(self, project_id: str, body: ProjectsCreateCommentBody, *, options: Optional[RequestOptions] = None) -> ProjectComment:
        """Adds a comment or a reply to a project.
        
        People mentioned as `@[Name](userId)` or `@name` who can open the project are notified.
        
        `POST /api/projects/{projectId}/comments` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/comments", query=None, body=body, multipart=False, options=options), "comment")  # type: ignore[no-any-return]

    def create_preview(self, project_id: str, body: ProjectsCreatePreviewBody, *, options: Optional[RequestOptions] = None) -> ProjectPreviewLink:
        """Creates a seven-day preview link to the project's draft.
        
        Replaces any earlier preview link of the project.
        
        `POST /api/projects/{projectId}/preview` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/preview", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsDeleteResponseData:
        """Moves a project to the trash.
        
        Needs `project.delete`. The project can be restored from the trash until it is deleted for good.
        
        `DELETE /api/projects/{projectId}` — Token permission: `delete:projects`.
        """
        return _pick(self._request("DELETE", f"/api/projects/{_seg(project_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_comment(self, project_id: str, comment_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsDeleteCommentResponse:
        """Deletes a comment.
        
        `DELETE /api/projects/{projectId}/comments/{commentId}` — Token permission: `delete:projects`.
        """
        return self._request("DELETE", f"/api/projects/{_seg(project_id)}/comments/{_seg(comment_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def download_export(self, project_id: str, export_id: str, *, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a finished export as a ZIP file.
        
        Answers the file itself (`application/zip`), not JSON. Only the person who started the export can download it.
        
        `GET /api/projects/{projectId}/export/{exportId}/download` — Token permission: `read:projects`.
        """
        return self._request("GET", f"/api/projects/{_seg(project_id)}/export/{_seg(export_id)}/download", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def export(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsExportResponseDataExport:
        """Starts an export of the project as a ZIP file that another installation can import.
        
        Needs `project.export`. The export runs in the background (202); poll `projects.listExports` and download it when `downloadable`.
        
        `POST /api/projects/{projectId}/export` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/export", query=None, body=None, multipart=False, options=options), "data.export")  # type: ignore[no-any-return]

    def get(self, project_id: str, *, options: Optional[RequestOptions] = None) -> Project:
        """Returns one project.
        
        `GET /api/projects/{projectId}` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_brain(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectBrainRecord:
        """Returns what the AI knows about the project: its business, audience, goals, tone and facts.
        
        `GET /api/projects/{projectId}/brain` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/brain", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_coming_soon(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsGetComingSoonResponseData:
        """Returns the project's coming-soon mode: whether it is on, the teaser page and the paths that stay reachable.
        
        `GET /api/projects/{projectId}/coming-soon` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/coming-soon", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_not_found_page(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsGetNotFoundPageResponseData:
        """Returns which page the live site shows for a URL that does not exist.
        
        `GET /api/projects/{projectId}/not-found-page` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/not-found-page", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_styles(self, project_id: str, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Returns a project's global styles (colors, fonts, spacing, radii).
        
        `GET /api/projects/{projectId}/styles` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/styles", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, workspace_id: Optional[str] = None, organization_id: Optional[str] = None, search: Optional[str] = None, status: Optional[Literal["active", "archived", "suspended"]] = None, folder: Optional[str] = None, folder_workspace_id: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Project]:
        """Lists the projects the caller can open, optionally of one workspace or organization.
        
        Without `workspaceId` or `organizationId` it lists the projects of every organization the caller belongs to. A private project is listed only to its creator.
        
        `GET /api/projects` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects", query={"workspaceId": workspace_id, "organizationId": organization_id, "search": search, "status": status, "folder": folder, "folderWorkspaceId": folder_workspace_id, "page": page, "limit": limit}, body=None, multipart=False, options=options), "projects")  # type: ignore[no-any-return]

    def list_collaborators(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[ProjectCollaborator]:
        """Lists the people of the project's organization, for mentioning them in comments.
        
        `GET /api/projects/{projectId}/collaborators` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/collaborators", query=None, body=None, multipart=False, options=options), "members")  # type: ignore[no-any-return]

    def list_comments(self, project_id: str, *, component_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[ProjectCommentThread]:
        """Lists a project's top-level comments with their replies.
        
        `GET /api/projects/{projectId}/comments` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/comments", query={"componentId": component_id}, body=None, multipart=False, options=options), "comments")  # type: ignore[no-any-return]

    def list_domains(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[ProjectDomain]:
        """Lists the hostnames of a project, with their verification status.
        
        `GET /api/projects/{projectId}/domains` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/domains", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_exports(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[ProjectExport]:
        """Lists the caller's last ten exports of the project.
        
        `GET /api/projects/{projectId}/export` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/export", query=None, body=None, multipart=False, options=options), "data.exports")  # type: ignore[no-any-return]

    def list_languages(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[ProjectLanguage]:
        """Lists the languages of a project.
        
        `GET /api/projects/{projectId}/languages` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/languages", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_pages(self, project_id: str, *, include: Optional[Literal["components"]] = None, options: Optional[RequestOptions] = None) -> List[PageListItem]:
        """Lists a project's pages.
        
        Without `include=components` the pages come without their component trees.
        
        `GET /api/projects/{projectId}/pages` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/pages", query={"include": include}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def publish(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectPublishResult:
        """Publishes every draft page and every live page with unpublished changes.
        
        Needs `page.update` and a verified email. Each page goes through the publish rules — freeze windows and the organization's approval requirement — so a page may be sent for approval or refused instead. At most 6 calls an hour per project.
        
        `POST /api/projects/{projectId}/publish` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/publish", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_domain(self, project_id: str, domain_id: str, *, options: Optional[RequestOptions] = None) -> List[ProjectDomain]:
        """Releases a hostname from a project.
        
        `DELETE /api/projects/{projectId}/domains/{domainId}` — Token permission: `delete:projects`.
        """
        return _pick(self._request("DELETE", f"/api/projects/{_seg(project_id)}/domains/{_seg(domain_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_language(self, project_id: str, *, language_code: str, options: Optional[RequestOptions] = None) -> ProjectsRemoveLanguageResponseData:
        """Removes a language from a project.
        
        `DELETE /api/projects/{projectId}/languages` — Token permission: `delete:projects`.
        """
        return _pick(self._request("DELETE", f"/api/projects/{_seg(project_id)}/languages", query={"languageCode": language_code}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def request_approval(self, project_id: str, body: ProjectsRequestApprovalBody, *, options: Optional[RequestOptions] = None) -> Approval:
        """Starts an approval of the project with the given steps and approvers.
        
        The approvers of the first step are notified.
        
        `POST /api/projects/{projectId}/request-approval` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/request-approval", query=None, body=body, multipart=False, options=options), "data.workflow")  # type: ignore[no-any-return]

    def revoke_preview(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsRevokePreviewResponse:
        """Revokes the project's preview link.
        
        `DELETE /api/projects/{projectId}/preview` — Token permission: `delete:projects`.
        """
        return self._request("DELETE", f"/api/projects/{_seg(project_id)}/preview", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set_default_language(self, project_id: str, body: ProjectsSetDefaultLanguageBody, *, options: Optional[RequestOptions] = None) -> ProjectsSetDefaultLanguageResponseData:
        """Makes one of the project's languages its default.
        
        Pages without a language of their own are tagged with it; `retagged` says how many.
        
        `PATCH /api/projects/{projectId}/languages` — Token permission: `write:projects`.
        """
        return _pick(self._request("PATCH", f"/api/projects/{_seg(project_id)}/languages", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def set_home_page(self, project_id: str, page_id: str, *, options: Optional[RequestOptions] = None) -> Page:
        """Makes a page the project's home page.
        
        `PUT /api/projects/{projectId}/pages/{pageId}/set-home` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/pages/{_seg(page_id)}/set-home", query=None, body=None, multipart=False, options=options), "page")  # type: ignore[no-any-return]

    def set_primary_domain(self, project_id: str, domain_id: str, *, options: Optional[RequestOptions] = None) -> List[ProjectDomain]:
        """Makes a hostname the project's primary one.
        
        `PUT /api/projects/{projectId}/domains/{domainId}/primary` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/domains/{_seg(domain_id)}/primary", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def suggest_brain(self, project_id: str, *, options: Optional[RequestOptions] = None) -> ProjectsSuggestBrainResponseData:
        """Drafts the project's brain from its pages with AI, without saving it.
        
        Counts against the organization's AI budget; save the draft with `projects.updateBrain`.
        
        `POST /api/projects/{projectId}/brain/suggest` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/brain/suggest", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def traffic(self, project_id: str, *, days: Optional[int] = None, options: Optional[RequestOptions] = None) -> ProjectTraffic:
        """Returns where the live site's visitors came from, per day and by source, referrer, campaign, country, device and browser.
        
        `GET /api/projects/{projectId}/traffic` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/traffic", query={"days": days}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def unset_home_page(self, project_id: str, page_id: str, *, options: Optional[RequestOptions] = None) -> Page:
        """Removes a page's home-page designation.
        
        `DELETE /api/projects/{projectId}/pages/{pageId}/set-home` — Token permission: `delete:projects`.
        """
        return _pick(self._request("DELETE", f"/api/projects/{_seg(project_id)}/pages/{_seg(page_id)}/set-home", query=None, body=None, multipart=False, options=options), "page")  # type: ignore[no-any-return]

    def update(self, project_id: str, body: UpdateProjectInput, *, options: Optional[RequestOptions] = None) -> Project:
        """Changes a project's name, description, status, visibility or settings.
        
        `PUT /api/projects/{projectId}` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_brain(self, project_id: str, body: ProjectsUpdateBrainBody, *, options: Optional[RequestOptions] = None) -> ProjectBrainRecord:
        """Saves what the AI knows about the project.
        
        `PUT /api/projects/{projectId}/brain` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/brain", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_coming_soon(self, project_id: str, body: ProjectsUpdateComingSoonBody, *, options: Optional[RequestOptions] = None) -> ProjectsUpdateComingSoonResponseData:
        """Turns coming-soon mode on or off, or changes its teaser page and reachable paths.
        
        Needs `page.update`. Turning it on needs a published teaser page of this project. Keys left out keep their value.
        
        `PUT /api/projects/{projectId}/coming-soon` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/coming-soon", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_comment(self, project_id: str, comment_id: str, body: ProjectsUpdateCommentBody, *, options: Optional[RequestOptions] = None) -> ProjectComment:
        """Edits a comment's text or resolves it.
        
        Only its author changes the text; anyone who can open the project changes the status.
        
        `PATCH /api/projects/{projectId}/comments/{commentId}` — Token permission: `write:projects`.
        """
        return _pick(self._request("PATCH", f"/api/projects/{_seg(project_id)}/comments/{_seg(comment_id)}", query=None, body=body, multipart=False, options=options), "comment")  # type: ignore[no-any-return]

    def update_not_found_page(self, project_id: str, body: ProjectsUpdateNotFoundPageBody, *, options: Optional[RequestOptions] = None) -> ProjectsUpdateNotFoundPageResponseData:
        """Chooses the page the live site shows for a URL that does not exist.
        
        Needs `page.update`. A null `pageId` goes back to the platform's own not-found page.
        
        `PUT /api/projects/{projectId}/not-found-page` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/not-found-page", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_styles(self, project_id: str, body: Dict[str, Any], *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Replaces a project's global styles.
        
        `PUT /api/projects/{projectId}/styles` — Token permission: `write:projects`.
        """
        return _pick(self._request("PUT", f"/api/projects/{_seg(project_id)}/styles", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def verify_domain(self, project_id: str, domain_id: str, *, options: Optional[RequestOptions] = None) -> ProjectDomain:
        """Checks a hostname's DNS records and marks it verified when they are right.
        
        `POST /api/projects/{projectId}/domains/{domainId}/verify` — Token permission: `write:projects`.
        """
        return _pick(self._request("POST", f"/api/projects/{_seg(project_id)}/domains/{_seg(domain_id)}/verify", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def video_analytics(self, project_id: str, *, options: Optional[RequestOptions] = None) -> List[VideoStats]:
        """Returns plays, viewers and completion of each video on the project's pages.
        
        `GET /api/projects/{projectId}/video-analytics` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/projects/{_seg(project_id)}/video-analytics", query=None, body=None, multipart=False, options=options), "data.videos")  # type: ignore[no-any-return]


class PushResource(_Resource):
    """Push
    """

    def get_public_key(self, *, options: Optional[RequestOptions] = None) -> str:
        """Returns the platform's public VAPID key, which a browser needs to subscribe to its push notifications.
        
        Null when push notifications are not set up on this platform.
        
        `GET /api/push/send` — No token needed.
        """
        return _pick(self._request("GET", f"/api/push/send", query=None, body=None, multipart=False, options=options), "publicKey")  # type: ignore[no-any-return]

    def subscribe(self, body: PushSubscribeBody, *, options: Optional[RequestOptions] = None) -> PushSubscribeResponse:
        """Registers a browser's push subscription, so the caller's notifications reach that device.
        
        Pass the browser's `PushSubscription` as JSON, made with the key from `push.getPublicKey`. Registering the same endpoint again updates its keys; an endpoint already registered by somebody else is left as it is. At most 30 calls in five minutes.
        
        `POST /api/push/subscribe`
        """
        return self._request("POST", f"/api/push/subscribe", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def unsubscribe(self, *, endpoint: str, options: Optional[RequestOptions] = None) -> PushUnsubscribeResponse:
        """Removes a device's push subscription of the caller.
        
        `DELETE /api/push/subscribe`
        """
        return self._request("DELETE", f"/api/push/subscribe", query={"endpoint": endpoint}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class ReferralsResource(_Resource):
    """Referrals — The platform's referral programme as one organisation takes part in it: each member with `referrals:share` has a personal link; a referred organisation that pays and stays past the refund window qualifies, and the referrer's organisation earns the programme's rewards and tiers. The platform sets the programme; everything here needs Referrals on the plan and membership of the organisation.
    """

    def get(self, *, organization_id: Optional[str] = None, lang: Optional[Literal["en", "de", "es", "fr"]] = None, options: Optional[RequestOptions] = None) -> ReferralOverview:
        """Returns the programme as the caller's organisation takes part in it: the caller's link, the rewards, the tiers and, with `referrals:read`, the organisation's referrals.
        
        Calling it gives the caller a code in this organisation when they hold `referrals:share` and have none yet. A referral is masked: its initial and dates, never a name or an address.
        
        `GET /api/referrals`
        """
        return _pick(self._request("GET", f"/api/referrals", query={"organizationId": organization_id, "lang": lang}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def regenerate_code(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> ReferralsRegenerateCodeResponseData:
        """Gives the caller a new personal referral code in the organisation; the old link stops working at once.
        
        Needs `referrals:share`. The referrals made through the old link keep their history. 409 while the programme is not running.
        
        `POST /api/referrals/code`
        """
        return _pick(self._request("POST", f"/api/referrals/code", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class RegionalSettingsResource(_Resource):
    """Regional settings
    """

    def get(self, *, options: Optional[RequestOptions] = None) -> RegionalSettings:
        """Returns the platform's default regional settings: time zone, date, time and number formats, first day of the week, currency and measurement system.
        
        These are the platform-wide defaults a person's own regional settings fall back to, not the caller's own choices.
        
        `GET /api/regional-settings`
        """
        return self._request("GET", f"/api/regional-settings", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class ReportsPublicLinksResource(_Resource):

    def create(self, report_id: str, body: ReportsPublicLinksCreateBody, *, options: Optional[RequestOptions] = None) -> ReportsPublicLinksCreateResponse:
        """Makes a read-only public link to a report and answers its URL, once.
        
        Needs `report.read`, and only the report's owner may — a link shows the owner's view of the data. Only the token's hash is kept: `url` cannot be shown again. Whoever opens it sees the report as its owner would; the hubs' figures only with `includeHubData`.
        
        `POST /api/reports/{reportId}/public-links`
        """
        return self._request("POST", f"/api/reports/{_seg(report_id)}/public-links", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, report_id: str, *, options: Optional[RequestOptions] = None) -> List[ReportPublicLink]:
        """Lists a report's read-only public links, without their tokens.
        
        Needs `report.read`, and only the report's owner may — a link shows the owner's view of the data.
        
        `GET /api/reports/{reportId}/public-links`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/public-links", query=None, body=None, multipart=False, options=options), "links")  # type: ignore[no-any-return]

    def revoke(self, report_id: str, link_id: str, *, options: Optional[RequestOptions] = None) -> ReportsPublicLinksRevokeResponse:
        """Revokes a public link; it answers 404 from then on.
        
        Needs `report.read`, and only the report's owner may — a link shows the owner's view of the data.
        
        `DELETE /api/reports/{reportId}/public-links/{linkId}`
        """
        return self._request("DELETE", f"/api/reports/{_seg(report_id)}/public-links/{_seg(link_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class ReportsSchedulesResource(_Resource):

    def create(self, report_id: str, body: ReportScheduleInput, *, options: Optional[RequestOptions] = None) -> ReportSchedule:
        """Mails a report on a schedule — daily, weekly or monthly — to members and, where allowed, external addresses.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin. Sent on the caller's clock and in their name; each member gets the report as they may see it at that moment, and who lost access is left out. At most 10 schedules per report (409 `reportScheduleLimit`).
        
        `POST /api/reports/{reportId}/schedules`
        """
        return _pick(self._request("POST", f"/api/reports/{_seg(report_id)}/schedules", query=None, body=body, multipart=False, options=options), "schedule")  # type: ignore[no-any-return]

    def delete(self, report_id: str, schedule_id: str, *, options: Optional[RequestOptions] = None) -> ReportsSchedulesDeleteResponse:
        """Deletes a schedule.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin.
        
        `DELETE /api/reports/{reportId}/schedules/{scheduleId}`
        """
        return self._request("DELETE", f"/api/reports/{_seg(report_id)}/schedules/{_seg(schedule_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, report_id: str, *, options: Optional[RequestOptions] = None) -> ReportsSchedulesListResponse:
        """Lists a report's mail schedules, with the organization's members to send to and whether external addresses are allowed.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin.
        
        `GET /api/reports/{reportId}/schedules`
        """
        return self._request("GET", f"/api/reports/{_seg(report_id)}/schedules", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def send_now(self, report_id: str, schedule_id: str, *, options: Optional[RequestOptions] = None) -> ReportsSchedulesSendNowResponse:
        """Sends a schedule's report now, to its recipients as they may read it at this moment.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin. Does not count as the day's scheduled send. Usually queued (202, `queued: true`); without a queue it is sent at once and `result` says what happened. 3 per schedule in 10 minutes.
        
        `POST /api/reports/{reportId}/schedules/{scheduleId}/send`
        """
        return self._request("POST", f"/api/reports/{_seg(report_id)}/schedules/{_seg(schedule_id)}/send", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, report_id: str, schedule_id: str, body: ReportsSchedulesUpdateBody, *, options: Optional[RequestOptions] = None) -> ReportSchedule:
        """Changes a schedule; `enabled` alone pauses or resumes it.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin. Only the fields sent change; the time stays on the clock of whoever made it.
        
        `PATCH /api/reports/{reportId}/schedules/{scheduleId}`
        """
        return _pick(self._request("PATCH", f"/api/reports/{_seg(report_id)}/schedules/{_seg(schedule_id)}", query=None, body=body, multipart=False, options=options), "schedule")  # type: ignore[no-any-return]


class ReportsSharesResource(_Resource):

    def create(self, report_id: str, body: ReportsSharesCreateBody, *, options: Optional[RequestOptions] = None) -> ReportShare:
        """Shares a report with a member or a team of its organization, to view or to edit.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin. Exactly one of `userId` and `teamId`. Sharing again with the same person or team changes the permission (200 instead of 201). Shares are read on every open: who leaves the organization loses it.
        
        `POST /api/reports/{reportId}/shares`
        """
        return _pick(self._request("POST", f"/api/reports/{_seg(report_id)}/shares", query=None, body=body, multipart=False, options=options), "share")  # type: ignore[no-any-return]

    def delete(self, report_id: str, share_id: str, *, options: Optional[RequestOptions] = None) -> ReportsSharesDeleteResponse:
        """Ends a share.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin.
        
        `DELETE /api/reports/{reportId}/shares/{shareId}`
        """
        return self._request("DELETE", f"/api/reports/{_seg(report_id)}/shares/{_seg(share_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, report_id: str, *, options: Optional[RequestOptions] = None) -> ReportsSharesListResponse:
        """Lists who a report is shared with, and the organization's members and teams to choose from.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin.
        
        `GET /api/reports/{reportId}/shares`
        """
        return self._request("GET", f"/api/reports/{_seg(report_id)}/shares", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, report_id: str, share_id: str, body: ReportsSharesUpdateBody, *, options: Optional[RequestOptions] = None) -> ReportShare:
        """Changes a share's permission.
        
        Needs `report.read` and the right to share the report: its owner or a platform admin.
        
        `PATCH /api/reports/{reportId}/shares/{shareId}`
        """
        return _pick(self._request("PATCH", f"/api/reports/{_seg(report_id)}/shares/{_seg(share_id)}", query=None, body=body, multipart=False, options=options), "share")  # type: ignore[no-any-return]


class ReportsSnapshotsResource(_Resource):

    def create(self, report_id: str, body: ReportsSnapshotsCreateBody, *, options: Optional[RequestOptions] = None) -> ReportsSnapshotsCreateResponseData:
        """Freezes every widget's current data as a snapshot, to compare against later.
        
        Needs `report.read` and edit access. Widgets whose source is read as the viewer (CRM, Invoicing, Products, Banking) are recorded without data. 6 an hour per person and report.
        
        `POST /api/reports/{reportId}/snapshots`
        """
        return _pick(self._request("POST", f"/api/reports/{_seg(report_id)}/snapshots", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, report_id: str, snapshot_id: str, *, options: Optional[RequestOptions] = None) -> ReportSnapshot:
        """Returns a snapshot with each widget's captured data.
        
        Needs `report.read`. Data read as the person who captured it is shown to them alone.
        
        `GET /api/reports/{reportId}/snapshots/{snapshotId}`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/snapshots/{_seg(snapshot_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, report_id: str, *, options: Optional[RequestOptions] = None) -> List[ReportSnapshotSummary]:
        """Lists a report's last 50 snapshots, newest first.
        
        Needs `report.read`.
        
        `GET /api/reports/{reportId}/snapshots`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/snapshots", query=None, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def sign(self, report_id: str, snapshot_id: str, *, options: Optional[RequestOptions] = None) -> ReportsSnapshotsSignResponseData:
        """Signs a snapshot, so later changes to its captured data can be detected.
        
        Needs `report.read`, edit access and `analytics:report_signed_snapshots` on the plan. Once per snapshot (409 `snapshotAlreadySigned`).
        
        `POST /api/reports/{reportId}/snapshots/{snapshotId}/sign`
        """
        return _pick(self._request("POST", f"/api/reports/{_seg(report_id)}/snapshots/{_seg(snapshot_id)}/sign", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def verify(self, report_id: str, snapshot_id: str, *, options: Optional[RequestOptions] = None) -> ReportsSnapshotsVerifyResponseData:
        """Checks a snapshot's signature against its captured data.
        
        Needs `report.read`.
        
        `GET /api/reports/{reportId}/snapshots/{snapshotId}/sign`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/snapshots/{_seg(snapshot_id)}/sign", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ReportsWidgetsResource(_Resource):

    def create(self, report_id: str, body: CreateReportWidgetInput, *, options: Optional[RequestOptions] = None) -> ReportWidget:
        """Adds a widget to a report.
        
        Needs `report.update` and edit access. The position is clamped to the 12-column grid. 60 a minute per person.
        
        `POST /api/reports/{reportId}/widgets`
        """
        return _pick(self._request("POST", f"/api/reports/{_seg(report_id)}/widgets", query=None, body=body, multipart=False, options=options), "widget")  # type: ignore[no-any-return]

    def delete(self, report_id: str, widget_id: str, *, options: Optional[RequestOptions] = None) -> ReportsWidgetsDeleteResponse:
        """Removes a widget from a report.
        
        Needs `report.update` and edit access.
        
        `DELETE /api/reports/{reportId}/widgets/{widgetId}`
        """
        return self._request("DELETE", f"/api/reports/{_seg(report_id)}/widgets/{_seg(widget_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def history(self, report_id: str, widget_id: str, *, options: Optional[RequestOptions] = None) -> List[ReportsWidgetsHistoryResponseDataItemsItem]:
        """Lists the last 50 changes to a widget's settings, newest first, field by field.
        
        Needs `report.read` and edit access.
        
        `GET /api/reports/{reportId}/widgets/{widgetId}/history`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/widgets/{_seg(widget_id)}/history", query=None, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def list(self, report_id: str, *, options: Optional[RequestOptions] = None) -> List[ReportWidget]:
        """Lists a report's widgets in grid order.
        
        Needs `report.read`.
        
        `GET /api/reports/{reportId}/widgets`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/widgets", query=None, body=None, multipart=False, options=options), "widgets")  # type: ignore[no-any-return]

    def observe(self, report_id: str, widget_id: str, body: ReportsWidgetsObserveBody, *, options: Optional[RequestOptions] = None) -> ReportsWidgetsObserveResponseData:
        """Has the platform's AI read a widget's data against its prompt and keeps the one-line observation on the widget.
        
        Needs `report.read`, a `prompt` on the widget and `analytics:report_ai_insights` on the plan; counts against the organization's AI quota (402 `aiQuotaExceeded`). Send the rows the widget shows. 10 a minute per person and widget.
        
        `POST /api/reports/{reportId}/widgets/{widgetId}/observe`
        """
        return _pick(self._request("POST", f"/api/reports/{_seg(report_id)}/widgets/{_seg(widget_id)}/observe", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, report_id: str, widget_id: str, body: UpdateReportWidgetInput, *, options: Optional[RequestOptions] = None) -> ReportWidget:
        """Changes a widget's title, type, data source, options, position or AI prompt.
        
        Needs `report.update` and edit access. Each change is kept in the widget's history.
        
        `PATCH /api/reports/{reportId}/widgets/{widgetId}`
        """
        return _pick(self._request("PATCH", f"/api/reports/{_seg(report_id)}/widgets/{_seg(widget_id)}", query=None, body=body, multipart=False, options=options), "widget")  # type: ignore[no-any-return]

    def update_layout(self, report_id: str, body: ReportsWidgetsUpdateLayoutBody, *, options: Optional[RequestOptions] = None) -> ReportsWidgetsUpdateLayoutResponse:
        """Moves and resizes several widgets at once, all or none.
        
        Needs `report.update` and edit access. Widgets not of this report are left alone.
        
        `PUT /api/reports/{reportId}/widgets`
        """
        return self._request("PUT", f"/api/reports/{_seg(report_id)}/widgets", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class ReportsResource(_Resource):
    """Reports — Reports of widgets — charts, tables and figures over databases, endpoints and the hubs' numbers — with their shares, mail schedules, public links and snapshots. Reports need `analytics:reports` on the organization's plan. A report the caller may not open answers 404, like one that does not exist.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.public_links = ReportsPublicLinksResource(request)
        self.schedules = ReportsSchedulesResource(request)
        self.shares = ReportsSharesResource(request)
        self.snapshots = ReportsSnapshotsResource(request)
        self.widgets = ReportsWidgetsResource(request)

    def annotations(self, report_id: str, *, from_: Optional[str] = None, to: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[ReportsAnnotationsResponseDataItemsItem]:
        """Lists the organization's events in a period — page publishes, deploys, notable audit events, calendar events — to mark on a time chart.
        
        Needs `report.read` and `analytics:report_annotations` on the plan. Calendar events only from calendars the caller may open, and a private one only when they may see its content. At most 400, oldest first.
        
        `GET /api/reports/{reportId}/annotations`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/annotations", query={"from": from_, "to": to}, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def consumers(self, report_id: str, *, options: Optional[RequestOptions] = None) -> List[ReportsConsumersResponseDataItemsItem]:
        """Lists the dashboards that show a widget of this report, to know what a change would affect.
        
        Needs `report.read` and edit access. Dashboards are named by id and owner only.
        
        `GET /api/reports/{reportId}/consumers`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/consumers", query=None, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def create(self, body: ReportsCreateBody, *, options: Optional[RequestOptions] = None) -> Report:
        """Creates a report, empty or from a template.
        
        Needs `report.create` in the organization (and access to the workspace, which must be the organization's). `crm_sales` makes the CRM's Sales report (needs the CRM forecast on the plan; over `crmSpaceId`, or every deals space of `workspaceId`); `invoicing` makes the Invoicing overview (needs Invoicing access). 30 a minute per person.
        
        `POST /api/reports`
        """
        return _pick(self._request("POST", f"/api/reports", query=None, body=body, multipart=False, options=options), "report")  # type: ignore[no-any-return]

    def data(self, report_id: str, body: ReportsDataBody, *, options: Optional[RequestOptions] = None) -> ReportsDataResponseData:
        """Reads the rows of a widget's data source, as the caller.
        
        Needs `report.read`. Name a stored widget (`widgetId`) to run its saved source, or send a `dataSource` to try one. Sources of the hubs are read with the caller's access. 120 a minute per person.
        
        `POST /api/reports/{reportId}/data`
        """
        return _pick(self._request("POST", f"/api/reports/{_seg(report_id)}/data", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, report_id: str, *, options: Optional[RequestOptions] = None) -> ReportsDeleteResponse:
        """Deletes a report with its widgets.
        
        Needs `report.delete` and the right to delete it. Permanent.
        
        `DELETE /api/reports/{reportId}`
        """
        return self._request("DELETE", f"/api/reports/{_seg(report_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def export(self, report_id: str, *, format: Optional[Literal["pdf", "csv"]] = None, separator: Optional[Literal["semicolon", "comma"]] = None, widget_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads a report as a PDF, or its tables as a CSV file, made with the caller's data, language and regional settings.
        
        Needs `report.read`. Answers the file itself (`application/pdf` or `text/csv`). 20 a minute per person.
        
        `GET /api/reports/{reportId}/export`
        """
        return self._request("GET", f"/api/reports/{_seg(report_id)}/export", query={"format": format, "separator": separator, "widgetId": widget_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, report_id: str, *, options: Optional[RequestOptions] = None) -> ReportsGetResponse:
        """Returns a report with its widgets and what the caller may do with it.
        
        Needs `report.read`.
        
        `GET /api/reports/{reportId}`
        """
        return self._request("GET", f"/api/reports/{_seg(report_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, workspace_id: Optional[str] = None, search: Optional[str] = None, folder: Optional[str] = None, folder_workspace_id: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Report]:
        """Lists the reports of an organization the caller may open, most recently changed first.
        
        Needs `report.read`. The caller's private reports, the workspace reports of workspaces they can open, the organization's reports, and those shared with them or their teams.
        
        `GET /api/reports`
        """
        return _pick(self._request("GET", f"/api/reports", query={"organizationId": organization_id, "workspaceId": workspace_id, "search": search, "folder": folder, "folderWorkspaceId": folder_workspace_id, "page": page, "limit": limit}, body=None, multipart=False, options=options), "reports")  # type: ignore[no-any-return]

    def source_health(self, report_id: str, *, options: Optional[RequestOptions] = None) -> List[ReportsSourceHealthResponseDataItemsItem]:
        """Returns each widget's data-source health — green, amber or red as last read.
        
        Needs `report.read`. Only database, endpoint and URL sources are tracked; the others are `unknown`.
        
        `GET /api/reports/{reportId}/source-health`
        """
        return _pick(self._request("GET", f"/api/reports/{_seg(report_id)}/source-health", query=None, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]

    def source_health_rollup(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> ReportsSourceHealthRollupResponseData:
        """Counts the data sources of an organization's reports by health and lists up to 20 that need attention.
        
        Needs `report.read`, membership and `analytics:report_sources_dashboard` on the plan. Only reports the caller may open count.
        
        `GET /api/reports/source-health-rollup`
        """
        return _pick(self._request("GET", f"/api/reports/source-health-rollup", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, report_id: str, body: ReportsUpdateBody, *, options: Optional[RequestOptions] = None) -> Report:
        """Changes a report's name, description, visibility, workspace, tags or favourite mark.
        
        Needs `report.update` and edit access. Send `expectedUpdatedAt` (or an `If-Unmodified-Since` header) with the `updatedAt` you read: a report saved meanwhile answers 409 `conflictReload` with `currentUpdatedAt`.
        
        `PATCH /api/reports/{reportId}`
        """
        return _pick(self._request("PATCH", f"/api/reports/{_seg(report_id)}", query=None, body=body, multipart=False, options=options), "report")  # type: ignore[no-any-return]


class RetentionPoliciesResource(_Resource):
    """Retention policies — How long an organisation keeps each kind of record: after `durationDays` from its creation or last change a record is either deleted by the nightly sweep (`autoDelete`) or locked until then. A workspace policy overrides the organisation-wide one for its type. Business records (content entries, bookings, booking pages, webhooks) are only counted until somebody confirms the count.
    """

    def check(self, *, organization_id: str, workspace_id: Optional[str] = None, resource_type: str, created_at: str, updated_at: str, options: Optional[RequestOptions] = None) -> RetentionPoliciesCheckResponseData:
        """Tells whether a retention policy applies to a record with the given dates, and its deadline.
        
        Needs membership of the organisation. The workspace's policy wins over the organisation-wide one.
        
        `GET /api/retention-policies/check`
        """
        return _pick(self._request("GET", f"/api/retention-policies/check", query={"organizationId": organization_id, "workspaceId": workspace_id, "resourceType": resource_type, "createdAt": created_at, "updatedAt": updated_at}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def check_cascade(self, *, parent_type: str, parent_id: str, organization_id: str, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> RetentionPoliciesCheckCascadeResponseData:
        """Tells whether deleting a record is blocked because records under it are still locked by a policy.
        
        Covers an endpoint's API keys and webhooks and a workflow's executions. Needs membership of the organisation.
        
        `GET /api/retention-policies/check-cascade`
        """
        return _pick(self._request("GET", f"/api/retention-policies/check-cascade", query={"parentType": parent_type, "parentId": parent_id, "organizationId": organization_id, "workspaceId": workspace_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def confirm(self, id: str, *, options: Optional[RequestOptions] = None) -> RetentionPolicy:
        """Confirms a business-record policy's count, so the nightly sweep starts deleting.
        
        Needs `retention_policies:manage` in the policy's organisation (and workspace, for a workspace policy). Answers 409 while the policy has no count yet or is not waiting for confirmation. Written to the audit log.
        
        `POST /api/retention-policies/{id}/confirm`
        """
        return _pick(self._request("POST", f"/api/retention-policies/{_seg(id)}/confirm", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: RetentionPoliciesCreateBody, *, options: Optional[RequestOptions] = None) -> RetentionPolicy:
        """Creates a retention policy for one kind of record.
        
        Needs `retention_policies:manage` in the policy's organisation (and workspace, for a workspace policy). A policy for a business-record type starts counting (`deletionGate: "preview"`) and deletes nothing until `retentionPolicies.confirm`. Pages are never deleted by a policy.
        
        `POST /api/retention-policies`
        """
        return _pick(self._request("POST", f"/api/retention-policies", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, id: str, *, options: Optional[RequestOptions] = None) -> RetentionPoliciesDeleteResponseData:
        """Deletes a retention policy.
        
        Needs `retention_policies:manage` in the policy's organisation (and workspace, for a workspace policy).
        
        `DELETE /api/retention-policies/{id}`
        """
        return _pick(self._request("DELETE", f"/api/retention-policies/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def dry_run(self, id: str, body: RetentionPoliciesDryRunBody, *, options: Optional[RequestOptions] = None) -> RetentionPoliciesDryRunResponseData:
        """Counts what a policy would delete now, without deleting, and keeps the result.
        
        Needs `retention_policies:manage` and the platform's `retention_dry_run` feature.
        
        `POST /api/retention-policies/{id}/dry-run`
        """
        return _pick(self._request("POST", f"/api/retention-policies/{_seg(id)}/dry-run", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, id: str, *, options: Optional[RequestOptions] = None) -> RetentionPolicy:
        """Returns one retention policy.
        
        Needs `retention_policies:manage` in the policy's organisation (and workspace, for a workspace policy).
        
        `GET /api/retention-policies/{id}`
        """
        return _pick(self._request("GET", f"/api/retention-policies/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, workspace_id: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[RetentionPolicy]:
        """Lists one page of an organisation's retention policies.
        
        Needs `retention_policies:manage`. With `workspaceId`, the workspace's policies and the organisation-wide ones.
        
        `GET /api/retention-policies`
        """
        return _pick(self._request("GET", f"/api/retention-policies", query={"organizationId": organization_id, "workspaceId": workspace_id, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data.data")  # type: ignore[no-any-return]

    def list_dry_runs(self, id: str, *, options: Optional[RequestOptions] = None) -> List[RetentionPoliciesListDryRunsResponseDataDryRunsItem]:
        """Lists a policy's last 20 dry runs.
        
        Needs `retention_policies:manage` and the platform's `retention_dry_run` feature.
        
        `GET /api/retention-policies/{id}/dry-run`
        """
        return _pick(self._request("GET", f"/api/retention-policies/{_seg(id)}/dry-run", query=None, body=None, multipart=False, options=options), "data.dryRuns")  # type: ignore[no-any-return]

    def update(self, id: str, body: RetentionPoliciesUpdateBody, *, options: Optional[RequestOptions] = None) -> RetentionPolicy:
        """Changes a retention policy's period, basis, mode, state or description.
        
        Needs `retention_policies:manage` in the policy's organisation (and workspace, for a workspace policy). Changing the period, basis or mode of a business-record policy resets its confirmation and counts again.
        
        `PUT /api/retention-policies/{id}`
        """
        return _pick(self._request("PUT", f"/api/retention-policies/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class RolesAssignmentsResource(_Resource):

    def create(self, body: RolesAssignmentsCreateBody, *, options: Optional[RequestOptions] = None) -> RoleAssignment:
        """Gives a person a role in an organization, workspace or team.
        
        Needs `role.assign`; only roles within the caller's own permissions.
        
        `POST /api/role-assignments`
        """
        return _pick(self._request("POST", f"/api/role-assignments", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, assignment_id: str, *, options: Optional[RequestOptions] = None) -> RolesAssignmentsDeleteResponse:
        """Takes a role assignment away.
        
        `DELETE /api/role-assignments/{assignmentId}`
        """
        return self._request("DELETE", f"/api/role-assignments/{_seg(assignment_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, workspace_id: Optional[str] = None, user_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[RoleAssignment]:
        """Lists role assignments — who holds which role where — in an organization or workspace, or of one person.
        
        `GET /api/role-assignments`
        """
        return _pick(self._request("GET", f"/api/role-assignments", query={"organizationId": organization_id, "workspaceId": workspace_id, "userId": user_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class RolesResource(_Resource):
    """Roles
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.assignments = RolesAssignmentsResource(request)

    def create(self, body: CreateRoleInput, *, options: Optional[RequestOptions] = None) -> Role:
        """Creates a role in an organization.
        
        Needs `role.create`. Permissions the organization's plan does not include, or the caller does not hold, are refused.
        
        `POST /api/roles`
        """
        return _pick(self._request("POST", f"/api/roles", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, role_id: str, *, options: Optional[RequestOptions] = None) -> RolesDeleteResponse:
        """Deletes a role.
        
        `DELETE /api/roles/{roleId}`
        """
        return self._request("DELETE", f"/api/roles/{_seg(role_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, role_id: str, *, options: Optional[RequestOptions] = None) -> Role:
        """Returns one role with its permissions.
        
        `GET /api/roles/{roleId}`
        """
        return _pick(self._request("GET", f"/api/roles/{_seg(role_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def grantable(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> RolesGrantableResponseData:
        """Lists the permissions the caller may put on a role in an organization.
        
        What the organization's plan includes and, unless the caller is a platform admin, what the caller holds.
        
        `GET /api/roles/grantable`
        """
        return _pick(self._request("GET", f"/api/roles/grantable", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Role]:
        """Lists an organization's roles, or the platform's system roles without `organizationId`.
        
        `GET /api/roles`
        """
        return _pick(self._request("GET", f"/api/roles", query={"organizationId": organization_id, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data.roles")  # type: ignore[no-any-return]

    def update(self, role_id: str, body: UpdateRoleInput, *, options: Optional[RequestOptions] = None) -> Role:
        """Changes a role's name, description or permissions.
        
        Needs `role.update`; the same limits on permissions as when creating.
        
        `PUT /api/roles/{roleId}`
        """
        return _pick(self._request("PUT", f"/api/roles/{_seg(role_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class ShareResource(_Resource):
    """Share links
    """

    def get_asset(self, token: str, *, options: Optional[RequestOptions] = None) -> ShareGetAssetResponse:
        """Opens a share link of a file or folder and returns what it shares.
        
        Needs no token. A password-protected link answers 401 with `passwordRequired: true` until the password is sent in the `X-Share-Password` header; a revoked or expired link answers 410.
        
        `GET /api/share/asset/{token}` — No token needed.
        """
        return self._request("GET", f"/api/share/asset/{_seg(token)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class SocialResource(_Resource):
    """Social — The Social hub: connected accounts, posts to one or more networks (drafted, scheduled or published now), their comments, assignments and repeats, the inbox of replies and mentions, analytics and the AI writing helps. Everything needs the `social` permission named on each operation and the Social hub on the plan. A row is seen by whom its visibility says: `private` its creator only, `workspace` that workspace's members, `organization` everyone in it.
    """

    def account_insights(self, account_id: str, *, refresh: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> SocialAccountInsightsResponse:
        """Returns a connected account's insights from its network: followers, reach and the like.
        
        Needs `social:view_analytics`. Instagram, Threads, Bluesky, Pinterest and YouTube; other networks answer `supported: false`. Cached for 15 minutes.
        
        `GET /api/social/insights/account/{accountId}`
        """
        return self._request("GET", f"/api/social/insights/account/{_seg(account_id)}", query={"refresh": refresh}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def add_comment(self, post_id: str, body: SocialAddCommentBody, *, options: Optional[RequestOptions] = None) -> SocialPostComment:
        """Adds an internal comment to a post; @-mentioned colleagues are notified.
        
        Needs `social:read`.
        
        `POST /api/social/posts/{postId}/comments`
        """
        return _pick(self._request("POST", f"/api/social/posts/{_seg(post_id)}/comments", query=None, body=body, multipart=False, options=options), "comment")  # type: ignore[no-any-return]

    def ai_caption(self, body: SocialAiCaptionBody, *, options: Optional[RequestOptions] = None) -> SocialAiCaptionResponse:
        """Writes a caption for a topic with the platform AI, fitted to the strictest network's length.
        
        Needs `social:create` and AI captions on the plan; refused when the person opted out of AI. Counts against the AI tokens.
        
        `POST /api/social/ai/caption`
        """
        return self._request("POST", f"/api/social/ai/caption", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def ai_hashtags(self, body: SocialAiHashtagsBody, *, options: Optional[RequestOptions] = None) -> List[str]:
        """Suggests hashtags for a caption or topic with the platform AI.
        
        Needs `social:create` and AI captions on the plan; counts against the AI tokens.
        
        `POST /api/social/ai/hashtags`
        """
        return _pick(self._request("POST", f"/api/social/ai/hashtags", query=None, body=body, multipart=False, options=options), "hashtags")  # type: ignore[no-any-return]

    def ai_variations(self, body: SocialAiVariationsBody, *, options: Optional[RequestOptions] = None) -> SocialAiVariationsResponse:
        """Writes one caption per network with the platform AI, each in that network's voice and length.
        
        Needs `social:create` and AI captions on the plan; counts against the AI tokens. Use each as the network's `perNetwork.textOverride`.
        
        `POST /api/social/ai/variations`
        """
        return self._request("POST", f"/api/social/ai/variations", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def analytics_summary(self, *, organization_id: str, window_days: Optional[int] = None, time_zone: Optional[str] = None, workspace_id: Optional[str] = None, campaign_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> SocialAnalyticsSummaryResponse:
        """Returns an organization's posting figures for a period: outcomes per network, the busiest hours and weekdays, and the networks' reach and engagement.
        
        Needs `social:view_analytics` and analytics on the plan. Hours and weekdays are counted in the caller's time zone (their profile's, else `timeZone`). `provider` comes from the insights last fetched for each post.
        
        `GET /api/social/analytics/summary`
        """
        return self._request("GET", f"/api/social/analytics/summary", query={"organizationId": organization_id, "windowDays": window_days, "timeZone": time_zone, "workspaceId": workspace_id, "campaignId": campaign_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def assign(self, post_id: str, body: SocialAssignBody, *, options: Optional[RequestOptions] = None) -> SocialPostAssignment:
        """Assigns a post to a member of its organization, replacing the current assignment.
        
        Needs `social:read`. The assignee is notified in the app and by email.
        
        `POST /api/social/posts/{postId}/assignment`
        """
        return _pick(self._request("POST", f"/api/social/posts/{_seg(post_id)}/assignment", query=None, body=body, multipart=False, options=options), "assignment")  # type: ignore[no-any-return]

    def best_time(self, body: SocialBestTimeBody, *, options: Optional[RequestOptions] = None) -> SocialBestTimeResponse:
        """Suggests three good times to post on a network, from the organization's history, with the platform AI.
        
        Needs `social:view_analytics`; counts against the organization's AI tokens. Without history the suggestion rests on the network's usual audience.
        
        `POST /api/social/analytics/best-time`
        """
        return self._request("POST", f"/api/social/analytics/best-time", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def bulk_create(self, body: SocialBulkCreateBody, *, options: Optional[RequestOptions] = None) -> SocialBulkCreateResponse:
        """Creates up to 200 posts at once, each a draft or scheduled, through the same accounts.
        
        Needs `social:create`, and `social:schedule` for rows with `scheduledAt`. Each row succeeds or fails on its own; `results` follow the order of `rows`.
        
        `POST /api/social/posts/bulk`
        """
        return self._request("POST", f"/api/social/posts/bulk", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def bulk_delete(self, body: SocialBulkDeleteBody, *, options: Optional[RequestOptions] = None) -> SocialBulkDeleteResponse:
        """Moves up to 200 posts to the trash.
        
        Needs `social:delete`. A post the caller cannot see, or one being published, is skipped.
        
        `POST /api/social/posts/bulk-delete`
        """
        return self._request("POST", f"/api/social/posts/bulk-delete", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def bulk_update(self, body: SocialBulkUpdateBody, *, options: Optional[RequestOptions] = None) -> SocialBulkUpdateResponse:
        """Sets the campaign or the assignee of up to 200 posts.
        
        Needs `social:update`. A post the caller cannot see is skipped; the rest go on.
        
        `POST /api/social/posts/bulk-update`
        """
        return self._request("POST", f"/api/social/posts/bulk-update", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def cancel(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialPost:
        """Cancels a scheduled post before it is published.
        
        Needs `social:schedule`.
        
        `POST /api/social/posts/{postId}/cancel`
        """
        return _pick(self._request("POST", f"/api/social/posts/{_seg(post_id)}/cancel", query=None, body=None, multipart=False, options=options), "post")  # type: ignore[no-any-return]

    def clone_post(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialPost:
        """Copies a post into a new draft with the same text, media, options and accounts.
        
        Needs `social:create`. The copy is not scheduled.
        
        `POST /api/social/posts/{postId}/clone`
        """
        return _pick(self._request("POST", f"/api/social/posts/{_seg(post_id)}/clone", query=None, body=None, multipart=False, options=options), "post")  # type: ignore[no-any-return]

    def connect_bluesky(self, body: SocialConnectBlueskyBody, *, options: Optional[RequestOptions] = None) -> SocialConnectBlueskyResponse:
        """Connects a Bluesky account with an app password.
        
        Needs `social:connect_account` and counts against the plan's social accounts. The app password is used once to sign in and never stored; connecting the same account again updates it. The other networks are connected by signing in, in the dashboard.
        
        `POST /api/social/accounts/connect/bluesky`
        """
        return self._request("POST", f"/api/social/accounts/connect/bluesky", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create_ab_test(self, body: SocialCreateAbTestBody, *, organization_id: str, options: Optional[RequestOptions] = None) -> SocialCreateAbTestResponse:
        """Creates two posts that differ only in their text, and a test that picks the better one after a while.
        
        Needs `social:create`. Both variants share accounts, media and campaign and publish like any post; the winner is decided by `metric` once `evaluateAfterHours` have passed.
        
        `POST /api/social/posts/ab-test`
        """
        return self._request("POST", f"/api/social/posts/ab-test", query={"organizationId": organization_id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create_campaign(self, body: SocialCreateCampaignBody, *, options: Optional[RequestOptions] = None) -> SocialCampaign:
        """Creates a campaign to tag posts with.
        
        Needs `social:create`.
        
        `POST /api/social/campaigns`
        """
        return _pick(self._request("POST", f"/api/social/campaigns", query=None, body=body, multipart=False, options=options), "campaign")  # type: ignore[no-any-return]

    def create_hashtag_set(self, body: SocialCreateHashtagSetBody, *, options: Optional[RequestOptions] = None) -> SocialHashtagSet:
        """Saves a set of hashtags.
        
        Needs `social:create`. Each tag gets a leading `#`; empty and repeated ones are dropped.
        
        `POST /api/social/hashtag-sets`
        """
        return _pick(self._request("POST", f"/api/social/hashtag-sets", query=None, body=body, multipart=False, options=options), "hashtagSet")  # type: ignore[no-any-return]

    def create_post(self, body: CreateSocialPostInput, *, organization_id: str, options: Optional[RequestOptions] = None) -> SocialPost:
        """Creates a social post as a draft, or scheduled when `scheduledAt` is given.
        
        Needs `social:create`, and `social:schedule` to schedule. A `private` account is posted through only by the person who connected it. Publishing now is POST /api/social/posts/{postId}/publish. `warnings` names networks whose length limit the text exceeds; it is not refused.
        
        `POST /api/social/posts`
        """
        return _pick(self._request("POST", f"/api/social/posts", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "post")  # type: ignore[no-any-return]

    def create_snippet(self, body: SocialCreateSnippetBody, *, organization_id: str, options: Optional[RequestOptions] = None) -> SocialSnippet:
        """Saves a reusable text snippet.
        
        Needs `social:create`.
        
        `POST /api/social/content-library`
        """
        return _pick(self._request("POST", f"/api/social/content-library", query={"organizationId": organization_id}, body=body, multipart=False, options=options), "snippet")  # type: ignore[no-any-return]

    def create_template(self, body: SocialCreateTemplateBody, *, options: Optional[RequestOptions] = None) -> SocialPostTemplate:
        """Saves a post template.
        
        Needs `social:create`.
        
        `POST /api/social/templates`
        """
        return _pick(self._request("POST", f"/api/social/templates", query=None, body=body, multipart=False, options=options), "template")  # type: ignore[no-any-return]

    def delete_auto_repost(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialDeleteAutoRepostResponse:
        """Stops repeating a post.
        
        Needs `social:update`.
        
        `DELETE /api/social/posts/{postId}/auto-repost`
        """
        return self._request("DELETE", f"/api/social/posts/{_seg(post_id)}/auto-repost", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_campaign(self, campaign_id: str, *, options: Optional[RequestOptions] = None) -> SocialDeleteCampaignResponse:
        """Deletes a campaign; its posts keep existing without it.
        
        Needs `social:delete`.
        
        `DELETE /api/social/campaigns/{campaignId}`
        """
        return self._request("DELETE", f"/api/social/campaigns/{_seg(campaign_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_comment(self, post_id: str, comment_id: str, *, options: Optional[RequestOptions] = None) -> SocialDeleteCommentResponse:
        """Deletes an internal comment.
        
        Needs `social:delete`; only the comment's author or an organization owner or admin.
        
        `DELETE /api/social/posts/{postId}/comments/{commentId}`
        """
        return self._request("DELETE", f"/api/social/posts/{_seg(post_id)}/comments/{_seg(comment_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_hashtag_set(self, hashtag_set_id: str, *, options: Optional[RequestOptions] = None) -> SocialDeleteHashtagSetResponse:
        """Deletes a saved hashtag set.
        
        Needs `social:delete`.
        
        `DELETE /api/social/hashtag-sets/{hashtagSetId}`
        """
        return self._request("DELETE", f"/api/social/hashtag-sets/{_seg(hashtag_set_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_post(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialDeletePostResponse:
        """Moves a social post to the trash.
        
        Needs `social:delete`. A scheduled post is taken off the schedule at once.
        
        `DELETE /api/social/posts/{postId}`
        """
        return self._request("DELETE", f"/api/social/posts/{_seg(post_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_snippet(self, snippet_id: str, *, options: Optional[RequestOptions] = None) -> SocialDeleteSnippetResponse:
        """Deletes a text snippet.
        
        Needs `social:delete`.
        
        `DELETE /api/social/content-library/{snippetId}`
        """
        return self._request("DELETE", f"/api/social/content-library/{_seg(snippet_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_template(self, template_id: str, *, options: Optional[RequestOptions] = None) -> SocialDeleteTemplateResponse:
        """Deletes a post template.
        
        Needs `social:delete`.
        
        `DELETE /api/social/templates/{templateId}`
        """
        return self._request("DELETE", f"/api/social/templates/{_seg(template_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def disconnect_account(self, account_id: str, *, options: Optional[RequestOptions] = None) -> SocialDisconnectAccountResponse:
        """Disconnects a social account.
        
        Needs `social:connect_account`. Posts already published stay; nothing more can be posted through the account.
        
        `DELETE /api/social/accounts/{accountId}`
        """
        return self._request("DELETE", f"/api/social/accounts/{_seg(account_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def draft_from_content(self, body: SocialDraftFromContentBody, *, options: Optional[RequestOptions] = None) -> SocialDraftFromContentResponse:
        """Writes a draft post about a live page or database record, with a text for each network.
        
        Needs `social:create`. The text is written from what visitors see (AI when available, else a template); nothing is scheduled or posted. 422 with `reason` when the page or record may not be shared.
        
        `POST /api/social/drafts/from-content`
        """
        return self._request("POST", f"/api/social/drafts/from-content", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_assignment(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialPostAssignment:
        """Returns who a post is assigned to, or null.
        
        Needs `social:read`.
        
        `GET /api/social/posts/{postId}/assignment`
        """
        return _pick(self._request("GET", f"/api/social/posts/{_seg(post_id)}/assignment", query=None, body=None, multipart=False, options=options), "assignment")  # type: ignore[no-any-return]

    def get_auto_repost(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialAutoRepost:
        """Returns a post's repeat schedule, or null.
        
        Needs `social:update`.
        
        `GET /api/social/posts/{postId}/auto-repost`
        """
        return _pick(self._request("GET", f"/api/social/posts/{_seg(post_id)}/auto-repost", query=None, body=None, multipart=False, options=options), "schedule")  # type: ignore[no-any-return]

    def get_post(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialPost:
        """Returns one social post with its targets.
        
        Needs `social:read`.
        
        `GET /api/social/posts/{postId}`
        """
        return _pick(self._request("GET", f"/api/social/posts/{_seg(post_id)}", query=None, body=None, multipart=False, options=options), "post")  # type: ignore[no-any-return]

    def limits(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> SocialLimitsResponse:
        """Returns the organization's daily post quota and connected-account quota with what is used.
        
        Needs `social:read`. `-1` means no limit.
        
        `GET /api/social/limits`
        """
        return self._request("GET", f"/api/social/limits", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_accounts(self, *, organization_id: str, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[SocialAccount]:
        """Lists the connected social accounts of an organization the caller can see, without their tokens.
        
        Needs `social:read`. A private account is listed to the person who connected it only — organization owners and admins included. Also answers which networks the platform offers for connecting.
        
        `GET /api/social/accounts`
        """
        return _pick(self._request("GET", f"/api/social/accounts", query={"organizationId": organization_id, "workspaceId": workspace_id}, body=None, multipart=False, options=options), "accounts")  # type: ignore[no-any-return]

    def list_campaigns(self, *, organization_id: str, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[SocialCampaign]:
        """Lists an organization's social campaigns the caller can see.
        
        Needs `social:read`.
        
        `GET /api/social/campaigns`
        """
        return _pick(self._request("GET", f"/api/social/campaigns", query={"organizationId": organization_id, "workspaceId": workspace_id}, body=None, multipart=False, options=options), "campaigns")  # type: ignore[no-any-return]

    def list_comments(self, post_id: str, *, options: Optional[RequestOptions] = None) -> List[SocialPostComment]:
        """Lists the team's internal comments on a post, oldest first.
        
        Needs `social:read`. These are notes between colleagues, not the network's comments (those are in the inbox).
        
        `GET /api/social/posts/{postId}/comments`
        """
        return _pick(self._request("GET", f"/api/social/posts/{_seg(post_id)}/comments", query=None, body=None, multipart=False, options=options), "comments")  # type: ignore[no-any-return]

    def list_hashtag_sets(self, *, organization_id: str, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[SocialHashtagSet]:
        """Lists an organization's saved hashtag sets the caller can see.
        
        Needs `social:read`.
        
        `GET /api/social/hashtag-sets`
        """
        return _pick(self._request("GET", f"/api/social/hashtag-sets", query={"organizationId": organization_id, "workspaceId": workspace_id}, body=None, multipart=False, options=options), "hashtagSets")  # type: ignore[no-any-return]

    def list_inbox(self, *, organization_id: str, filter: Optional[Literal["unread", "all"]] = None, network: Optional[SocialNetwork] = None, account_id: Optional[str] = None, q: Optional[str] = None, limit: Optional[int] = None, offset: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[SocialInboxItem]:
        """Lists the comments, replies, mentions and messages received on an organization's accounts, newest first.
        
        Needs `social:read`. Also answers the unread count and, per connected network, whether the inbox can read it (`coverage`).
        
        `GET /api/social/inbox`
        """
        return _pick(self._request("GET", f"/api/social/inbox", query={"organizationId": organization_id, "filter": filter, "network": network, "accountId": account_id, "q": q, "limit": limit, "offset": offset}, body=None, multipart=False, options=options), "items")  # type: ignore[no-any-return]

    def list_posts(self, *, organization_id: str, status: Optional[SocialPostStatus] = None, workspace_id: Optional[str] = None, campaign_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[SocialListPostsResponsePostsItem]:
        """Lists an organization's social posts the caller can see, newest first.
        
        Needs `social:read`. At most 500 posts; each carries `assignedTo`, the user it is assigned to.
        
        `GET /api/social/posts`
        """
        return _pick(self._request("GET", f"/api/social/posts", query={"organizationId": organization_id, "status": status, "workspaceId": workspace_id, "campaignId": campaign_id}, body=None, multipart=False, options=options), "posts")  # type: ignore[no-any-return]

    def list_snippets(self, *, organization_id: str, q: Optional[str] = None, tag: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[SocialSnippet]:
        """Lists the reusable text snippets of an organization the caller can see, most recently used first.
        
        Needs `social:read`.
        
        `GET /api/social/content-library`
        """
        return _pick(self._request("GET", f"/api/social/content-library", query={"organizationId": organization_id, "q": q, "tag": tag}, body=None, multipart=False, options=options), "snippets")  # type: ignore[no-any-return]

    def list_templates(self, *, organization_id: str, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[SocialPostTemplate]:
        """Lists an organization's post templates the caller can see.
        
        Needs `social:read`.
        
        `GET /api/social/templates`
        """
        return _pick(self._request("GET", f"/api/social/templates", query={"organizationId": organization_id, "workspaceId": workspace_id}, body=None, multipart=False, options=options), "templates")  # type: ignore[no-any-return]

    def mark_inbox_read(self, item_id: str, *, options: Optional[RequestOptions] = None) -> SocialInboxItem:
        """Marks an inbox item read.
        
        Needs `social:read`.
        
        `POST /api/social/inbox/{itemId}/read`
        """
        return _pick(self._request("POST", f"/api/social/inbox/{_seg(item_id)}/read", query=None, body=None, multipart=False, options=options), "item")  # type: ignore[no-any-return]

    def mark_inbox_unread(self, item_id: str, *, options: Optional[RequestOptions] = None) -> SocialInboxItem:
        """Marks an inbox item unread.
        
        Needs `social:read`.
        
        `DELETE /api/social/inbox/{itemId}/read`
        """
        return _pick(self._request("DELETE", f"/api/social/inbox/{_seg(item_id)}/read", query=None, body=None, multipart=False, options=options), "item")  # type: ignore[no-any-return]

    def patch_post(self, post_id: str, body: SocialPatchPostBody, *, options: Optional[RequestOptions] = None) -> SocialPost:
        """Changes a draft or scheduled post.
        
        Needs `social:update`. A post that was published, failed or cancelled cannot be changed (400) — clone it instead. New `targetAccountIds` reset every target to pending.
        
        `PATCH /api/social/posts/{postId}`
        """
        return _pick(self._request("PATCH", f"/api/social/posts/{_seg(post_id)}", query=None, body=body, multipart=False, options=options), "post")  # type: ignore[no-any-return]

    def poll_inbox(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> SocialPollInboxResponse:
        """Fetches new inbox items from the networks now instead of waiting for the hourly run.
        
        Needs `social:create`. Each network's per-account limit applies as on the schedule.
        
        `POST /api/social/inbox/poll`
        """
        return self._request("POST", f"/api/social/inbox/poll", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def post_insights(self, post_id: str, *, refresh: Optional[Literal["1"]] = None, options: Optional[RequestOptions] = None) -> List[SocialPostInsightsResponseTargetsItem]:
        """Returns each published target's insights from its network: impressions, likes, comments and the like.
        
        Needs `social:view_analytics`. A network without insights answers `supported: false` for its target. A fetch with `refresh=1` stores a snapshot, which the analytics summary reads.
        
        `GET /api/social/insights/post/{postId}`
        """
        return _pick(self._request("GET", f"/api/social/insights/post/{_seg(post_id)}", query={"refresh": refresh}, body=None, multipart=False, options=options), "targets")  # type: ignore[no-any-return]

    def publish_now(self, post_id: str, *, options: Optional[RequestOptions] = None) -> PublishResult:
        """Publishes a post now, or retries the targets that failed.
        
        Needs `social:publish_now` and a verified email. Targets already published are never published again, so it is safe to repeat. Counts once against the daily post quota whatever the number of networks. 403 `publishNeedsApproval` while an approval holds the post; 409 while it is publishing; 400 for a cancelled post.
        
        `POST /api/social/posts/{postId}/publish`
        """
        return self._request("POST", f"/api/social/posts/{_seg(post_id)}/publish", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def reply_inbox(self, item_id: str, body: SocialReplyInboxBody, *, options: Optional[RequestOptions] = None) -> SocialReplyInboxResponse:
        """Replies to an inbox item on its network.
        
        Needs `social:create`. The reply is posted through the account that received the item.
        
        `POST /api/social/inbox/{itemId}/reply`
        """
        return self._request("POST", f"/api/social/inbox/{_seg(item_id)}/reply", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def retry_story(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialRetryStoryResponse:
        """Publishes a story post again to the targets that failed.
        
        Needs `social:publish_now` and stories on the plan. Only a post of kind `story`; targets already published are left alone.
        
        `POST /api/social/posts/{postId}/retry-story`
        """
        return self._request("POST", f"/api/social/posts/{_seg(post_id)}/retry-story", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def schedule(self, post_id: str, body: SocialScheduleBody, *, options: Optional[RequestOptions] = None) -> SocialPost:
        """Schedules a draft post, or moves a scheduled one to another time.
        
        Needs `social:schedule`. A failed or partly published post cannot be scheduled again; clone it.
        
        `POST /api/social/posts/{postId}/schedule`
        """
        return _pick(self._request("POST", f"/api/social/posts/{_seg(post_id)}/schedule", query=None, body=body, multipart=False, options=options), "post")  # type: ignore[no-any-return]

    def set_auto_repost(self, post_id: str, body: SocialSetAutoRepostBody, *, options: Optional[RequestOptions] = None) -> SocialAutoRepost:
        """Repeats a published post at an interval, creating or changing its schedule.
        
        Needs `social:update`. A draft cannot be repeated (400); publish it first.
        
        `PUT /api/social/posts/{postId}/auto-repost`
        """
        return _pick(self._request("PUT", f"/api/social/posts/{_seg(post_id)}/auto-repost", query=None, body=body, multipart=False, options=options), "schedule")  # type: ignore[no-any-return]

    def share_check(self, *, kind: Literal["page", "record"], page_id: Optional[str] = None, database_id: Optional[str] = None, record_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> SocialShareCheckResponse:
        """Tells whether a live page or database record can be shared, what the post would link to, and through which accounts.
        
        Needs `social:create` and access to the page or record (404 otherwise).
        
        `GET /api/social/drafts/from-content`
        """
        return self._request("GET", f"/api/social/drafts/from-content", query={"kind": kind, "pageId": page_id, "databaseId": database_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def unassign(self, post_id: str, *, options: Optional[RequestOptions] = None) -> SocialUnassignResponse:
        """Releases a post's current assignment.
        
        Needs `social:read`.
        
        `DELETE /api/social/posts/{postId}/assignment`
        """
        return self._request("DELETE", f"/api/social/posts/{_seg(post_id)}/assignment", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_account(self, account_id: str, body: SocialUpdateAccountBody, *, options: Optional[RequestOptions] = None) -> SocialAccount:
        """Changes a connected account's visibility, workspace or default Pinterest board.
        
        Needs `social:connect_account`. Tokens are never taken here; reconnect the account instead.
        
        `PATCH /api/social/accounts/{accountId}`
        """
        return _pick(self._request("PATCH", f"/api/social/accounts/{_seg(account_id)}", query=None, body=body, multipart=False, options=options), "account")  # type: ignore[no-any-return]

    def update_snippet(self, snippet_id: str, body: SocialUpdateSnippetBody, *, options: Optional[RequestOptions] = None) -> SocialSnippet:
        """Changes a text snippet.
        
        Needs `social:update`.
        
        `PATCH /api/social/content-library/{snippetId}`
        """
        return _pick(self._request("PATCH", f"/api/social/content-library/{_seg(snippet_id)}", query=None, body=body, multipart=False, options=options), "snippet")  # type: ignore[no-any-return]


class SubmissionsResource(_Resource):
    """Submissions
    """

    def analytics(self, *, project_id: str, days: Optional[int] = None, options: Optional[RequestOptions] = None) -> SubmissionsAnalyticsResponseData:
        """Returns a project's submission figures: totals by status, category and form, response times and SLA breaches per day.
        
        `GET /api/submissions/analytics`
        """
        return _pick(self._request("GET", f"/api/submissions/analytics", query={"projectId": project_id, "days": days}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def bulk_delete(self, *, ids: List[str], options: Optional[RequestOptions] = None) -> SubmissionsBulkDeleteResponseData:
        """Moves up to 500 submissions to the trash at once.
        
        Only submissions of projects the caller can open are touched; the others are skipped. They stay restorable in the trash for the organisation's retention days.
        
        `DELETE /api/submissions/bulk`
        """
        return _pick(self._request("DELETE", f"/api/submissions/bulk", query={"ids": ids}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def bulk_update(self, body: SubmissionsBulkUpdateBody, *, options: Optional[RequestOptions] = None) -> float:
        """Changes the status, priority or assignee of up to 500 submissions, or adds a tag to them.
        
        Submissions the caller may not see are left alone.
        
        `POST /api/submissions/bulk`
        """
        return _pick(self._request("POST", f"/api/submissions/bulk", query=None, body=body, multipart=False, options=options), "data.updated")  # type: ignore[no-any-return]

    def create(self, body: SubmissionsCreateBody, *, options: Optional[RequestOptions] = None) -> Submission:
        """Records a form submission, as if a visitor had sent the form.
        
        Needs `submissions.manage`.
        
        `POST /api/submissions`
        """
        return _pick(self._request("POST", f"/api/submissions", query=None, body=body, multipart=False, options=options), "data.submission")  # type: ignore[no-any-return]

    def create_canned_response(self, body: SubmissionsCreateCannedResponseBody, *, options: Optional[RequestOptions] = None) -> SubmissionCannedResponse:
        """Saves a reply for reuse, for the organization or one project.
        
        `POST /api/submissions/canned-responses`
        """
        return _pick(self._request("POST", f"/api/submissions/canned-responses", query=None, body=body, multipart=False, options=options), "data.template")  # type: ignore[no-any-return]

    def delete(self, id: str, *, options: Optional[RequestOptions] = None) -> SubmissionsDeleteResponseData:
        """Moves a submission and its thread to the trash.
        
        `DELETE /api/submissions/{id}`
        """
        return _pick(self._request("DELETE", f"/api/submissions/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_canned_response(self, canned_response_id: str, *, options: Optional[RequestOptions] = None) -> SubmissionsDeleteCannedResponseResponse:
        """Deletes a saved reply.
        
        `DELETE /api/submissions/canned-responses/{cannedResponseId}`
        """
        return self._request("DELETE", f"/api/submissions/canned-responses/{_seg(canned_response_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def enrich(self, id: str, *, options: Optional[RequestOptions] = None) -> Submission:
        """Runs the AI summary, category and priority of a submission again.
        
        Needs the plan's AI enrichment; counts against the organization's AI budget.
        
        `POST /api/submissions/{id}/enrich`
        """
        return _pick(self._request("POST", f"/api/submissions/{_seg(id)}/enrich", query=None, body=None, multipart=False, options=options), "data.submission")  # type: ignore[no-any-return]

    def erase_personal_data(self, *, email: str, confirm: Literal[True], project_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> SubmissionsErasePersonalDataResponseData:
        """Erases every submission one email address sent, for good (a data subject's right to erasure).
        
        Immediate and permanent — erased submissions do not go to the trash. Only projects the caller can open are searched; `confirm` must be `true`.
        
        `DELETE /api/submissions/gdpr`
        """
        return _pick(self._request("DELETE", f"/api/submissions/gdpr", query={"email": email, "confirm": confirm, "projectId": project_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def export(self, *, project_id: Optional[str] = None, form_id: Optional[str] = None, status: Optional[SubmissionStatus] = None, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the submissions the caller may see as a CSV file.
        
        Needs `submissions.export`. Answers the file itself (`text/csv`).
        
        `GET /api/submissions/export`
        """
        return self._request("GET", f"/api/submissions/export", query={"projectId": project_id, "formId": form_id, "status": status, "q": q}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def export_personal_data(self, body: SubmissionsExportPersonalDataBody, *, options: Optional[RequestOptions] = None) -> SubmissionsExportPersonalDataResponseData:
        """Exports every submission and message from one email address — a data subject's access request.
        
        Needs `submissions.export`.
        
        `POST /api/submissions/gdpr`
        """
        return _pick(self._request("POST", f"/api/submissions/gdpr", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get(self, id: str, *, options: Optional[RequestOptions] = None) -> SubmissionsGetResponseData:
        """Returns a submission with its reply thread; opening a new one marks it read when the caller may update submissions.
        
        `GET /api/submissions/{id}`
        """
        return _pick(self._request("GET", f"/api/submissions/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_form_settings(self, project_id: str, form_id: str, *, options: Optional[RequestOptions] = None) -> SubmissionFormSettings:
        """Returns a form's inbox settings: notifications, auto-tags, auto-reply, SLA.
        
        `GET /api/submissions/forms/{projectId}/{formId}`
        """
        return _pick(self._request("GET", f"/api/submissions/forms/{_seg(project_id)}/{_seg(form_id)}", query=None, body=None, multipart=False, options=options), "data.settings")  # type: ignore[no-any-return]

    def list(self, *, project_id: Optional[str] = None, form_id: Optional[str] = None, status: Optional[SubmissionStatus] = None, q: Optional[str] = None, assignee: Optional[str] = None, limit: Optional[int] = None, cursor: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[Submission]:
        """Lists the form submissions the caller may see, newest first, a page at a time.
        
        `GET /api/submissions`
        """
        return _pick(self._request("GET", f"/api/submissions", query={"projectId": project_id, "formId": form_id, "status": status, "q": q, "assignee": assignee, "limit": limit, "cursor": cursor}, body=None, multipart=False, options=options), "data.submissions")  # type: ignore[no-any-return]

    def list_canned_responses(self, *, project_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[SubmissionCannedResponse]:
        """Lists the saved replies of the caller's organizations, and of a project.
        
        `GET /api/submissions/canned-responses`
        """
        return _pick(self._request("GET", f"/api/submissions/canned-responses", query={"projectId": project_id}, body=None, multipart=False, options=options), "data.templates")  # type: ignore[no-any-return]

    def list_forms(self, *, project_id: str, options: Optional[RequestOptions] = None) -> List[SubmissionsListFormsResponseDataFormsItem]:
        """Lists the forms of a project that have submissions, with counts and settings.
        
        `GET /api/submissions/forms`
        """
        return _pick(self._request("GET", f"/api/submissions/forms", query={"projectId": project_id}, body=None, multipart=False, options=options), "data.forms")  # type: ignore[no-any-return]

    def reply(self, submission_id: str, body: SubmissionsReplyBody, *, options: Optional[RequestOptions] = None) -> SubmissionMessage:
        """Replies to a submission, or adds an internal note to it.
        
        A reply (`outbound`, the default) marks the submission replied; with `sendEmail` it is also emailed to the submitter. An `internal_note` changes nothing else. Rate-limited per submission.
        
        `POST /api/submissions/{submissionId}/messages`
        """
        return _pick(self._request("POST", f"/api/submissions/{_seg(submission_id)}/messages", query=None, body=body, multipart=False, options=options), "data.message")  # type: ignore[no-any-return]

    def set_form_visibility(self, project_id: str, form_id: str, body: SubmissionsSetFormVisibilityBody, *, options: Optional[RequestOptions] = None) -> SubmissionsSetFormVisibilityResponseData:
        """Chooses who sees a form's submissions from now on — the caller only, the workspace, or the project.
        
        Existing submissions keep theirs unless `applyToExisting` — and then only those the caller can see.
        
        `PUT /api/submissions/forms/{projectId}/{formId}/visibility`
        """
        return _pick(self._request("PUT", f"/api/submissions/forms/{_seg(project_id)}/{_seg(form_id)}/visibility", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def thread(self, id: str, *, options: Optional[RequestOptions] = None) -> List[SubmissionsThreadResponseDataRelatedItem]:
        """Lists the other submissions of the same conversation the caller may see.
        
        `GET /api/submissions/{id}/thread`
        """
        return _pick(self._request("GET", f"/api/submissions/{_seg(id)}/thread", query=None, body=None, multipart=False, options=options), "data.related")  # type: ignore[no-any-return]

    def update(self, id: str, body: SubmissionsUpdateBody, *, options: Optional[RequestOptions] = None) -> Submission:
        """Changes a submission's status, priority, tags or assignee.
        
        `PATCH /api/submissions/{id}`
        """
        return _pick(self._request("PATCH", f"/api/submissions/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data.submission")  # type: ignore[no-any-return]

    def update_canned_response(self, canned_response_id: str, body: SubmissionsUpdateCannedResponseBody, *, options: Optional[RequestOptions] = None) -> SubmissionCannedResponse:
        """Changes a saved reply.
        
        `PATCH /api/submissions/canned-responses/{cannedResponseId}`
        """
        return _pick(self._request("PATCH", f"/api/submissions/canned-responses/{_seg(canned_response_id)}", query=None, body=body, multipart=False, options=options), "data.template")  # type: ignore[no-any-return]

    def update_form_settings(self, project_id: str, form_id: str, body: SubmissionsUpdateFormSettingsBody, *, options: Optional[RequestOptions] = None) -> SubmissionFormSettings:
        """Changes a form's inbox settings; only the fields sent change.
        
        Needs `submissions.manage`. Notified and auto-assigned people must be able to see the form's submissions.
        
        `PATCH /api/submissions/forms/{projectId}/{formId}`
        """
        return _pick(self._request("PATCH", f"/api/submissions/forms/{_seg(project_id)}/{_seg(form_id)}", query=None, body=body, multipart=False, options=options), "data.settings")  # type: ignore[no-any-return]


class SubscriptionsResource(_Resource):
    """Subscriptions — Cancelling an organization's paid plan with the platform, and taking a scheduled cancellation back.
    """

    def cancel(self, body: SubscriptionsCancelBody, *, options: Optional[RequestOptions] = None) -> SubscriptionsCancelResponse:
        """Cancels an organization's paid plan at the end of the paid period, or at once.
        
        Needs to be the organization's owner or hold `billing:manage` in it. By default the plan keeps running until the period ends; `immediate: true` ends it now. A scheduled downgrade is withdrawn. 404 `noActiveSubscription` without a paid plan.
        
        `POST /api/subscriptions/cancel`
        """
        return self._request("POST", f"/api/subscriptions/cancel", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def resume(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> SubscriptionsResumeResponse:
        """Takes back a cancellation scheduled for the end of the paid period.
        
        Needs to be the organization's owner or hold `billing:manage` in it. Works only while the plan has not ended; 404 `subscriptionNotCanceling` when nothing is scheduled.
        
        `DELETE /api/subscriptions/cancel`
        """
        return self._request("DELETE", f"/api/subscriptions/cancel", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class SupportResource(_Resource):
    """Support
    """

    def create_ticket(self, body: SupportCreateTicketBody, *, options: Optional[RequestOptions] = None) -> SupportTicket:
        """Opens a support ticket with the platform's support team.
        
        The platform's admins are notified. The ticket belongs to the caller and the first organization they are a member of.
        
        `POST /api/support/tickets`
        """
        return _pick(self._request("POST", f"/api/support/tickets", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_ticket(self, id: str, *, options: Optional[RequestOptions] = None) -> SupportGetTicketResponseData:
        """Returns one of the caller's support tickets with its messages, oldest first.
        
        Internal notes of the support team are left out. `ticketUser` and `assignedAdmin` are only returned to the platform's support staff.
        
        `GET /api/support/tickets/{id}`
        """
        return _pick(self._request("GET", f"/api/support/tickets/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_messages(self, ticket_id: str, *, options: Optional[RequestOptions] = None) -> List[SupportMessage]:
        """Lists the messages of one of the caller's support tickets, oldest first.
        
        Internal notes of the support team are left out.
        
        `GET /api/support/tickets/{ticketId}/messages`
        """
        return _pick(self._request("GET", f"/api/support/tickets/{_seg(ticket_id)}/messages", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_tickets(self, *, status: Optional[str] = None, priority: Optional[Literal["low", "medium", "high", "critical"]] = None, category: Optional[Literal["bug", "feature_request", "question", "billing", "security", "other"]] = None, options: Optional[RequestOptions] = None) -> List[SupportTicket]:
        """Lists the support tickets the caller opened, newest first.
        
        `GET /api/support/tickets`
        """
        return _pick(self._request("GET", f"/api/support/tickets", query={"status": status, "priority": priority, "category": category}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def post_message(self, ticket_id: str, body: SupportPostMessageBody, *, options: Optional[RequestOptions] = None) -> SupportMessage:
        """Adds the caller's reply to one of their support tickets.
        
        A ticket waiting on the caller (or resolved) goes back to waiting on the support team, and the assigned admin is notified.
        
        `POST /api/support/tickets/{ticketId}/messages`
        """
        return _pick(self._request("POST", f"/api/support/tickets/{_seg(ticket_id)}/messages", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_ticket(self, id: str, body: SupportUpdateTicketBody, *, options: Optional[RequestOptions] = None) -> SupportTicket:
        """Closes one of the caller's support tickets.
        
        The ticket's author can only close it (`status: "closed"`); every other change belongs to the platform's support staff.
        
        `PATCH /api/support/tickets/{id}`
        """
        return _pick(self._request("PATCH", f"/api/support/tickets/{_seg(id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def upload(self, body: Union[SupportUploadBody, Dict[str, Any]], *, options: Optional[RequestOptions] = None) -> str:
        """Uploads a screenshot to attach to a support ticket.
        
        PNG, JPEG, GIF or WebP, at most 10 MB. Pass the returned `url` as `screenshotUrl` when opening the ticket.
        
        `POST /api/support/upload`
        """
        return _pick(self._request("POST", f"/api/support/upload", query=None, body=body, multipart=True, options=options), "url")  # type: ignore[no-any-return]


class TasksAutomationResource(_Resource):

    def get(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> TasksAutomationGetResponse:
        """The caller's meeting guardian and waiting-for nudges, and the Tasks spaces they may add to.
        
        `GET /api/tasks/automation-settings` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/automation-settings", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, body: TasksAutomationUpdateBody, *, options: Optional[RequestOptions] = None) -> TasksAutomationUpdateResponse:
        """Changes the caller's meeting guardian and waiting-for nudges.
        
        The guardian needs a Tasks space the caller may add to (400 `tasksGuardianSpaceRequired`).
        
        `PUT /api/tasks/automation-settings` — Token permission: `write:tasks`.
        """
        return self._request("PUT", f"/api/tasks/automation-settings", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksChecklistResource(_Resource):

    def convert(self, body: TasksChecklistConvertBody, *, options: Optional[RequestOptions] = None) -> TasksChecklistConvertResponse:
        """Turns a step of a CRM task's checklist into a task of its own, linked from the step.
        
        Needs edit access to the task; counts against the plan's record limit. The step's text becomes the title, its person and day the assignee and due date. A step that names a task already answers that task (`created: false`). Ticking the new task done ticks the step.
        
        `POST /api/tasks/checklist/convert` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/checklist/convert", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksConditionsResource(_Resource):

    def add(self, body: TaskConditionInput, *, options: Optional[RequestOptions] = None) -> bool:
        """Adds a "done when" condition to a CRM task; a thing already done completes the task at once.
        
        Needs edit access to the task, and the caller must be able to open the watched thing.
        
        `POST /api/tasks/conditions` — Token permission: `write:tasks`.
        """
        return _pick(self._request("POST", f"/api/tasks/conditions", query=None, body=body, multipart=False, options=options), "completed")  # type: ignore[no-any-return]

    def list(self, *, database_id: str, record_id: str, options: Optional[RequestOptions] = None) -> TasksConditionsListResponse:
        """A CRM task's "done when" conditions; what each watches is named only for a reader who may open it.
        
        `GET /api/tasks/conditions` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/conditions", query={"databaseId": database_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def options_(self, *, database_id: str, record_id: str, kind: TaskConditionKind, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> TasksConditionsOptionsResponse:
        """What a "done when" condition of this kind may watch — only things the caller may open.
        
        Needs edit access to the task.
        
        `GET /api/tasks/conditions/options` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/conditions/options", query={"databaseId": database_id, "recordId": record_id, "kind": kind, "q": q}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def remove(self, *, database_id: str, record_id: str, condition_id: str, options: Optional[RequestOptions] = None) -> TasksConditionsRemoveResponse:
        """Removes a "done when" condition from a task.
        
        `DELETE /api/tasks/conditions` — Token permission: `write:tasks`.
        """
        return self._request("DELETE", f"/api/tasks/conditions", query={"databaseId": database_id, "recordId": record_id, "conditionId": condition_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksDealRoomResource(_Resource):

    def get(self, *, database_id: str, record_id: str, options: Optional[RequestOptions] = None) -> TasksDealRoomGetResponse:
        """The deal-room step a CRM task is shown as to the customer.
        
        The deal is named only for a reader who may open it.
        
        `GET /api/tasks/deal-room` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/deal-room", query={"databaseId": database_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def link(self, body: TasksDealRoomLinkBody, *, options: Optional[RequestOptions] = None) -> TasksDealRoomLinkResponse:
        """Shows a CRM task to the customer as a deal-room step: an existing step, or a new one titled like the task.
        
        Needs edit access to the task and the deal, and the deal's room switched on.
        
        `POST /api/tasks/deal-room` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/deal-room", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def options_(self, *, database_id: str, record_id: str, q: Optional[str] = None, options: Optional[RequestOptions] = None) -> TasksDealRoomOptionsResponse:
        """The open deals a CRM task could be linked to — their room on, changeable by the caller — each with its customer steps.
        
        `GET /api/tasks/deal-room/options` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/deal-room/options", query={"databaseId": database_id, "recordId": record_id, "q": q}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def unlink(self, *, database_id: str, record_id: str, options: Optional[RequestOptions] = None) -> TasksDealRoomUnlinkResponse:
        """Stops showing a task in its deal's deal room.
        
        `DELETE /api/tasks/deal-room` — Token permission: `write:tasks`.
        """
        return self._request("DELETE", f"/api/tasks/deal-room", query={"databaseId": database_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksDelegationResource(_Resource):

    def cancel(self, *, database_id: str, record_id: str, options: Optional[RequestOptions] = None) -> TasksDelegationCancelResponse:
        """Calls off the agent working on a task.
        
        `DELETE /api/tasks/delegate` — Token permission: `write:tasks`.
        """
        return self._request("DELETE", f"/api/tasks/delegate", query={"databaseId": database_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, *, database_id: str, record_id: str, options: Optional[RequestOptions] = None) -> TasksDelegationGetResponse:
        """The caller's latest delegation of a CRM task to an agent, and the agents they may run.
        
        `GET /api/tasks/delegate` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/delegate", query={"databaseId": database_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def start(self, body: Union[TasksDelegationStartBody, TasksDelegationStartBody2], *, options: Optional[RequestOptions] = None) -> TasksDelegationStartResponse:
        """Starts an agent on a CRM task, or answers the finished agent's "mark done?".
        
        Starting (`agentId`) needs edit access to the task, the Agent Hub, `agent:execute` and an active agent the caller may see; the run acts as the caller, and steps that need confirming become questions in their Tasks list. Answering (`answer`): `done` ticks the task as the caller — never automatic.
        
        `POST /api/tasks/delegate` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/delegate", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksDetailsResource(_Resource):

    def get(self, *, database_id: str, record_id: str, options: Optional[RequestOptions] = None) -> TasksDetailsGetResponse:
        """What a CRM task carries beside its cells: how it repeats, its own reminders, the caller's snooze, and whether the caller may change them.
        
        `GET /api/tasks/details` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/details", query={"databaseId": database_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, body: TasksDetailsUpdateBody, *, options: Optional[RequestOptions] = None) -> TasksDetailsUpdateResponse:
        """Sets how a CRM task repeats, or replaces its own reminders.
        
        Needs edit access to the task. `recurrence: null` stops it repeating. 400 `tasksRecurrenceInvalid` / `tasksRemindersInvalid`.
        
        `PUT /api/tasks/details` — Token permission: `write:tasks`.
        """
        return self._request("PUT", f"/api/tasks/details", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksFeedResource(_Resource):

    def create(self, body: TasksFeedCreateBody, *, options: Optional[RequestOptions] = None) -> TasksFeedCreateResponse:
        """Creates a calendar feed of the caller's tasks in a workspace; the previous feed stops working.
        
        The feed's URL is answered once: only a hash is kept, so a lost URL is replaced by making a new one. The URL is a secret — whoever has it reads the tasks.
        
        `POST /api/tasks/settings/feed` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/settings/feed", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def revoke(self, *, options: Optional[RequestOptions] = None) -> TaskUserSettings:
        """Ends the caller's calendar feed; every calendar subscribed to it gets 404 from then on.
        
        `DELETE /api/tasks/settings/feed` — Token permission: `write:tasks`.
        """
        return _pick(self._request("DELETE", f"/api/tasks/settings/feed", query=None, body=None, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class TasksFocusResource(_Resource):

    def end(self, *, options: Optional[RequestOptions] = None) -> TasksFocusEndResponse:
        """Ends the caller's focus session now; the profile before comes back.
        
        `DELETE /api/tasks/focus` — Token permission: `write:tasks`.
        """
        return self._request("DELETE", f"/api/tasks/focus", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, *, options: Optional[RequestOptions] = None) -> TasksFocusGetResponse:
        """The caller's running focus session and their focus profiles.
        
        `GET /api/tasks/focus` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/focus", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def start(self, body: TasksFocusStartBody, *, options: Optional[RequestOptions] = None) -> TasksFocusStartResponse:
        """Focuses on a task for 5–240 minutes, optionally switching to one of the caller's focus profiles meanwhile.
        
        `POST /api/tasks/focus` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/focus", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksNudgesResource(_Resource):

    def remind(self, body: Union[TasksNudgesRemindBody, TasksNudgesRemindBody2], *, options: Optional[RequestOptions] = None) -> TasksNudgesRemindResponse:
        """Nudges the people a task or mail waits on: a notification to a task's other assignees, or a reply draft in a mail thread.
        
        A task: once a day (409 `tasksAlreadyReminded`), by who gave it or may change it. A mail: a draft to the people the last message went to — never sent by itself.
        
        `POST /api/tasks/nudges/remind` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/nudges/remind", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksPlanDayResource(_Resource):

    def blocks(self, *, item_id: str, options: Optional[RequestOptions] = None) -> List[TasksPlanDayBlocksResponseBlocksItem]:
        """The caller's booked blocks of a task that are still ahead.
        
        `GET /api/tasks/plan-day/blocks` — Token permission: `read:tasks`.
        """
        return _pick(self._request("GET", f"/api/tasks/plan-day/blocks", query={"itemId": item_id}, body=None, multipart=False, options=options), "blocks")  # type: ignore[no-any-return]

    def book(self, body: TasksPlanDayBookBody, *, options: Optional[RequestOptions] = None) -> TasksPlanDayBookResponse:
        """Books the planned blocks as tentative events in the caller's own default calendar.
        
        A block for a task that already has one moves that event. Only tasks of the caller's own list. Each block answers on its own (`failed`). Needs `calendar:create`; 409 `calendarNoCalendar` without a calendar.
        
        `POST /api/tasks/plan-day/book` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/plan-day/book", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def free_blocks(self, *, item_id: str, options: Optional[RequestOptions] = None) -> Any:
        """Frees a task's planned time: its block events are deleted from the caller's own calendar.
        
        `DELETE /api/tasks/plan-day/blocks` — Token permission: `write:tasks`.
        """
        return _pick(self._request("DELETE", f"/api/tasks/plan-day/blocks", query={"itemId": item_id}, body=None, multipart=False, options=options), "freed")  # type: ignore[no-any-return]

    def get(self, *, workspace_id: str, day: Optional[str] = None, options: Optional[RequestOptions] = None) -> TasksPlanDayGetResponse:
        """"Plan my day": the caller's working window, what is in their own calendars, and a proposal placing their open tasks in the free time.
        
        Nothing is written; booking is `tasks.planDay.book`. Needs the calendar on the plan and `calendar:read`; only the caller's own calendars are read.
        
        `GET /api/tasks/plan-day` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/plan-day", query={"workspaceId": workspace_id, "day": day}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksQuickAddResource(_Resource):

    def ai(self, body: TasksQuickAddAiBody, *, options: Optional[RequestOptions] = None) -> TasksQuickAddAiResponse:
        """Asks the platform AI to read a quick-add line for the parts the plain reader missed: the due date, the priority, the repeat.
        
        A suggestion only; nothing is written (the task is made by `tasks.create`). The person's AI opt-out (403 `ai_opted_out`) and the organisation's AI allowance (429 `aiQuotaExceeded`) apply.
        
        `POST /api/tasks/quick-add/ai` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/quick-add/ai", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def records(self, *, workspace_id: str, q: str, type_: Optional[Literal["person", "company", "deal"]] = None, space_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> TasksQuickAddRecordsResponse:
        """The CRM records a quick-add mention ("+Acme", "about deal Acme") may mean, by name or e-mail; nothing is linked.
        
        `GET /api/tasks/quick-add/records` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/quick-add/records", query={"workspaceId": workspace_id, "q": q, "type": type_, "spaceId": space_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def space(self, *, workspace_id: str, space_id: str, options: Optional[RequestOptions] = None) -> TasksQuickAddSpaceResponse:
        """What a Tasks space takes beyond a title: its label options and the kinds of CRM records it can link.
        
        `GET /api/tasks/quick-add/space` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/quick-add/space", query={"workspaceId": workspace_id, "spaceId": space_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksRecurrenceResource(_Resource):

    def skip(self, body: TasksRecurrenceSkipBody, *, options: Optional[RequestOptions] = None) -> TasksRecurrenceSkipResponse:
        """Skips this occurrence of a repeating CRM task: its due date moves to the rule's next date without it being done.
        
        Needs edit access to the task. 409 `tasksNotRecurring`, `tasksSeriesEnded`, `tasksNoDueColumn`.
        
        `POST /api/tasks/recurrence/skip` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/recurrence/skip", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksSettingsResource(_Resource):

    def get(self, *, options: Optional[RequestOptions] = None) -> TasksSettingsGetResponse:
        """The caller's Tasks settings: default reminders and the daily digest.
        
        `GET /api/tasks/settings` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/settings", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, body: TaskSettingsPatch, *, options: Optional[RequestOptions] = None) -> TaskUserSettings:
        """Changes the caller's Tasks settings.
        
        `PUT /api/tasks/settings` — Token permission: `write:tasks`.
        """
        return _pick(self._request("PUT", f"/api/tasks/settings", query=None, body=body, multipart=False, options=options), "settings")  # type: ignore[no-any-return]


class TasksSlaResource(_Resource):

    def get(self, *, database_id: str, options: Optional[RequestOptions] = None) -> TasksSlaGetResponse:
        """A Tasks space's service levels and escalation ladder, and whether the caller may change them.
        
        `GET /api/tasks/sla` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/sla", query={"databaseId": database_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def put(self, body: TasksSlaPutBody, *, options: Optional[RequestOptions] = None) -> TasksSlaPutResponse:
        """Sets a Tasks space's service levels and escalation ladder.
        
        Needs `crm:manage` and manage level on the space. 400 `tasksSlaInvalid` for a policy it does not take, `tasksSlaMemberUnknown` for a person outside the organisation.
        
        `PUT /api/tasks/sla` — Token permission: `write:tasks`.
        """
        return self._request("PUT", f"/api/tasks/sla", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksViewsResource(_Resource):

    def create(self, body: TasksViewsCreateBody, *, options: Optional[RequestOptions] = None) -> TasksViewsCreateResponse:
        """Saves the hub's current state — scope, filters, grouping, sort, layout, search — as a named view.
        
        409 `tasksViewLimit` at the maximum number of views.
        
        `POST /api/tasks/views` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/views", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete(self, view_id: str, *, options: Optional[RequestOptions] = None) -> TasksViewsDeleteResponse:
        """Deletes a saved view; when it was the default, the hub's own default applies again.
        
        `DELETE /api/tasks/views/{viewId}` — Token permission: `write:tasks`.
        """
        return self._request("DELETE", f"/api/tasks/views/{_seg(view_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, options: Optional[RequestOptions] = None) -> TasksViewsListResponse:
        """The caller's saved views of the Tasks hub, and the one it opens with.
        
        `GET /api/tasks/views` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/views", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set_default(self, body: TasksViewsSetDefaultBody, *, options: Optional[RequestOptions] = None) -> TasksViewsSetDefaultResponse:
        """Which view the hub opens with (null: the hub's own default).
        
        `PUT /api/tasks/views` — Token permission: `write:tasks`.
        """
        return self._request("PUT", f"/api/tasks/views", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, view_id: str, body: TasksViewsUpdateBody, *, options: Optional[RequestOptions] = None) -> TasksViewsUpdateResponse:
        """Renames a saved view, saves a new state into it, or makes it (or stops it being) the default.
        
        `PATCH /api/tasks/views/{viewId}` — Token permission: `write:tasks`.
        """
        return self._request("PATCH", f"/api/tasks/views/{_seg(view_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TasksResource(_Resource):
    """Tasks
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.automation = TasksAutomationResource(request)
        self.checklist = TasksChecklistResource(request)
        self.conditions = TasksConditionsResource(request)
        self.deal_room = TasksDealRoomResource(request)
        self.delegation = TasksDelegationResource(request)
        self.details = TasksDetailsResource(request)
        self.feed = TasksFeedResource(request)
        self.focus = TasksFocusResource(request)
        self.nudges = TasksNudgesResource(request)
        self.plan_day = TasksPlanDayResource(request)
        self.quick_add = TasksQuickAddResource(request)
        self.recurrence = TasksRecurrenceResource(request)
        self.settings = TasksSettingsResource(request)
        self.sla = TasksSlaResource(request)
        self.views = TasksViewsResource(request)

    def bulk(self, body: TaskBulkInput, *, options: Optional[RequestOptions] = None) -> TasksBulkResponse:
        """Completes, reschedules, reprioritises or reassigns several tasks at once; each is checked on its own.
        
        `POST /api/tasks/bulk` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/bulk", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def complete(self, body: Union[TasksCompleteBody, TasksCompleteBody2, TasksCompleteBody3], *, options: Optional[RequestOptions] = None) -> TasksCompleteResponse:
        """Ticks an item off, or opens it again with `done: false`, the way its own hub does it.
        
        For a CRM task: `{ source: "crm", databaseId, recordId }`; a deal-room step adds `stepId`; a calendar follow-up names its `eventId`.
        
        `POST /api/tasks/complete` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/complete", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create(self, body: TaskCreateInput, *, options: Optional[RequestOptions] = None) -> TaskItem:
        """Quick add: creates a CRM task in the workspace's Tasks space, assigned to the caller.
        
        Needs edit level on the Tasks space. With several Tasks spaces and no `spaceId`: 409 `tasksSpaceRequired` with `spaces`; with none: 409 `tasksSetupRequired` or `tasksNoSpace`.
        
        `POST /api/tasks` — Token permission: `write:tasks`.
        """
        return _pick(self._request("POST", f"/api/tasks", query=None, body=body, multipart=False, options=options), "task")  # type: ignore[no-any-return]

    def estimate(self, body: TasksEstimateBody, *, options: Optional[RequestOptions] = None) -> float:
        """Sets how long a CRM task takes; null removes it (Plan my day then counts 30 minutes).
        
        Needs edit access to the task.
        
        `PUT /api/tasks/estimate` — Token permission: `write:tasks`.
        """
        return _pick(self._request("PUT", f"/api/tasks/estimate", query=None, body=body, multipart=False, options=options), "minutes")  # type: ignore[no-any-return]

    def from_source(self, *, workspace_id: str, kind: TaskOriginKind, id: str, document_id: Optional[str] = None, page_id: Optional[str] = None, space_id: Optional[str] = None, record_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> TasksFromSourceResponse:
        """What "Make task" starts with for a mail, message, comment, activity, booking or submission.
        
        `GET /api/tasks/from-source` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/from-source", query={"workspaceId": workspace_id, "kind": kind, "id": id, "documentId": document_id, "pageId": page_id, "spaceId": space_id, "recordId": record_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list(self, *, workspace_id: str, scope: Optional[Literal["mine", "created"]] = None, sources: Optional[str] = None, include: Optional[Literal["done"]] = None, options: Optional[RequestOptions] = None) -> TasksListResponse:
        """What the caller has to do in a workspace, as one list: their CRM tasks and what other hubs wait on them for.
        
        Assigned to them (`mine`, the default) or created by them (`created`). Besides CRM tasks: approvals to decide, mail threads and submissions assigned to them, questions of their agent runs. Every source applies its own rules; `failedSources` names the ones that could not be read.
        
        `GET /api/tasks` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks", query={"workspaceId": workspace_id, "scope": scope, "sources": sources, "include": include}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def next_up(self, *, workspace_id: str, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> TasksNextUpResponse:
        """"Next up": the open items in one order, each with why it is there.
        
        `GET /api/tasks/next-up` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/next-up", query={"workspaceId": workspace_id, "limit": limit}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def pin(self, body: TasksPinBody, *, options: Optional[RequestOptions] = None) -> bool:
        """Keeps an item at the top of "Next up", or lets it go again.
        
        `POST /api/tasks/pin` — Token permission: `write:tasks`.
        """
        return _pick(self._request("POST", f"/api/tasks/pin", query=None, body=body, multipart=False, options=options), "pinned")  # type: ignore[no-any-return]

    def snooze(self, body: TasksSnoozeBody, *, options: Optional[RequestOptions] = None) -> TasksSnoozeResponse:
        """Holds the caller's notices about a CRM task until a time; then one reminder comes.
        
        Only the caller's own notices change. `until` within the next 90 days (400 `tasksSnoozeInvalid`); null ends the snooze.
        
        `POST /api/tasks/snooze` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/snooze", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, body: TaskUpdateInput, *, options: Optional[RequestOptions] = None) -> TasksUpdateResponse:
        """Changes a CRM task's due date, status, priority or assignee.
        
        `POST /api/tasks/update` — Token permission: `write:tasks`.
        """
        return self._request("POST", f"/api/tasks/update", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def workload(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> TasksWorkloadResponse:
        """The team view: the workspace's members and their open, overdue and coming tasks.
        
        `GET /api/tasks/workload` — Token permission: `read:tasks`.
        """
        return self._request("GET", f"/api/tasks/workload", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class TaxRatesResource(_Resource):
    """Tax rates
    """

    def list(self, *, options: Optional[RequestOptions] = None) -> List[TaxRate]:
        """Lists the platform's tax rates, including those that only applied in the past.
        
        Answers without a token. Only enabled rates, sorted by name; `effectiveFrom` and `effectiveTo` say when each applied. Cached for five minutes.
        
        `GET /api/tax-rates` — No token needed.
        """
        return self._request("GET", f"/api/tax-rates", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class TeamsResource(_Resource):
    """Teams
    """

    def add_member(self, team_id: str, body: AddTeamMemberInput, *, options: Optional[RequestOptions] = None) -> TeamMember:
        """Adds a person to a team, optionally with a role in it.
        
        Needs `team.update`.
        
        `POST /api/teams/{teamId}/members` — Token permission: `write:teams`.
        """
        return _pick(self._request("POST", f"/api/teams/{_seg(team_id)}/members", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: CreateTeamInput, *, options: Optional[RequestOptions] = None) -> Team:
        """Creates a team in a workspace.
        
        Needs `team.create`.
        
        `POST /api/teams` — Token permission: `write:teams`.
        """
        return _pick(self._request("POST", f"/api/teams", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, team_id: str, *, options: Optional[RequestOptions] = None) -> TeamsDeleteResponse:
        """Deletes a team and its memberships.
        
        `DELETE /api/teams/{teamId}` — Token permission: `write:teams`.
        """
        return self._request("DELETE", f"/api/teams/{_seg(team_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, team_id: str, *, options: Optional[RequestOptions] = None) -> TeamsGetResponseData:
        """Returns a team with its members.
        
        `GET /api/teams/{teamId}` — Token permission: `read:teams`.
        """
        return _pick(self._request("GET", f"/api/teams/{_seg(team_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, search: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Team]:
        """Lists the teams the caller can see, optionally of one organization.
        
        `GET /api/teams` — Token permission: `read:teams`.
        """
        return _pick(self._request("GET", f"/api/teams", query={"organizationId": organization_id, "search": search, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_members(self, team_id: str, *, options: Optional[RequestOptions] = None) -> List[TeamMember]:
        """Lists a team's members with their user details and roles in the team.
        
        `GET /api/teams/{teamId}/members` — Token permission: `read:teams`.
        """
        return _pick(self._request("GET", f"/api/teams/{_seg(team_id)}/members", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_member(self, team_id: str, member_id: str, *, options: Optional[RequestOptions] = None) -> TeamsRemoveMemberResponse:
        """Removes a person from a team.
        
        `DELETE /api/teams/{teamId}/members/{memberId}` — Token permission: `write:teams`.
        """
        return self._request("DELETE", f"/api/teams/{_seg(team_id)}/members/{_seg(member_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def remove_member_role(self, team_id: str, member_id: str, *, role_id: str, options: Optional[RequestOptions] = None) -> TeamsRemoveMemberRoleResponse:
        """Takes a role in the team away from a member.
        
        `DELETE /api/teams/{teamId}/members/{memberId}/assign-role` — Token permission: `write:teams`.
        """
        return self._request("DELETE", f"/api/teams/{_seg(team_id)}/members/{_seg(member_id)}/assign-role", query={"roleId": role_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, team_id: str, body: UpdateTeamInput, *, options: Optional[RequestOptions] = None) -> Team:
        """Changes a team's name, description or settings.
        
        `PUT /api/teams/{teamId}` — Token permission: `write:teams`.
        """
        return _pick(self._request("PUT", f"/api/teams/{_seg(team_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_member(self, team_id: str, member_id: str, body: TeamsUpdateMemberBody, *, options: Optional[RequestOptions] = None) -> RoleAssignment:
        """Gives a team member a role in the team.
        
        Needs `team.manage_members`; only roles within the caller's own permissions.
        
        `POST /api/teams/{teamId}/members/{memberId}/assign-role` — Token permission: `write:teams`.
        """
        return _pick(self._request("POST", f"/api/teams/{_seg(team_id)}/members/{_seg(member_id)}/assign-role", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class TelephonyCallsResource(_Resource):

    def get(self, call_id: str, *, workspace_id: str, options: Optional[RequestOptions] = None) -> PhoneCallDetail:
        """One call with every CRM record it matched, the call-back task it made, and the lines that can call back.
        
        A call on no line the caller may use answers 404, like a missing one.
        
        `GET /api/telephony/calls/{callId}` — Token permission: `read:telephony`.
        """
        return _pick(self._request("GET", f"/api/telephony/calls/{_seg(call_id)}", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options), "call")  # type: ignore[no-any-return]

    def list(self, *, workspace_id: str, cursor: Optional[str] = None, before: Optional[str] = None, line_id: Optional[str] = None, direction: Optional[Literal["in", "out"]] = None, missed: Optional[Literal["1"]] = None, from_: Optional[str] = None, to: Optional[str] = None, q: Optional[str] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[PhoneCallLogEntry]:
        """The call log of the lines the caller may use in a workspace, newest first, each with the CRM record its number matched.
        
        A telephony manager sees no more than anybody else: configuring a line is not reading it. Page on with `cursor` = the answer's `nextCursor`.
        
        `GET /api/telephony/calls` — Token permission: `read:telephony`.
        """
        return _pick(self._request("GET", f"/api/telephony/calls", query={"workspaceId": workspace_id, "cursor": cursor, "before": before, "lineId": line_id, "direction": direction, "missed": missed, "from": from_, "to": to, "q": q, "limit": limit}, body=None, multipart=False, options=options), "calls")  # type: ignore[no-any-return]


class TelephonyConnectionsResource(_Resource):

    def create(self, body: PhoneConnectionInput, *, options: Optional[RequestOptions] = None) -> PhoneConnection:
        """Connects the customer's own phone provider account to a workspace; the credentials are tested first.
        
        Needs `telephony:manage` in the workspace. The credentials are stored only when they work, never shown again. The connection gets its own webhook URL; where the provider can list the account's lines, they are read at once.
        
        `POST /api/telephony/connections` — Token permission: `write:telephony`.
        """
        return _pick(self._request("POST", f"/api/telephony/connections", query=None, body=body, multipart=False, options=options), "connection")  # type: ignore[no-any-return]

    def delete(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> TelephonyConnectionsDeleteResponse:
        """Deletes a connection with its lines and its call log.
        
        Needs `telephony:manage`.
        
        `DELETE /api/telephony/connections/{connectionId}` — Token permission: `write:telephony`.
        """
        return self._request("DELETE", f"/api/telephony/connections/{_seg(connection_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def sync_lines(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> TelephonyConnectionsSyncLinesResponse:
        """Reads the account's lines from the provider: new ones are added, known ones refreshed, none deleted.
        
        Needs `telephony:manage`. Only where the provider can list lines (409 `telephonyLinesNotSupported` otherwise — add them by hand). New lines only while the plan has room; the rest are counted in `overLimit`. Owners, members and switches are never touched.
        
        `POST /api/telephony/connections/{connectionId}/sync` — Token permission: `write:telephony`.
        """
        return self._request("POST", f"/api/telephony/connections/{_seg(connection_id)}/sync", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def test(self, connection_id: str, *, options: Optional[RequestOptions] = None) -> TelephonyConnectionsTestResponse:
        """Makes one authenticated read of the provider with the stored credentials.
        
        Needs `telephony:manage`. Works: the connection is active again; refused: its status becomes `error`. For a provider that issues the webhook secret itself (Aircall) it is read here once the webhook exists — `webhookSecret` says whether it was found.
        
        `POST /api/telephony/connections/{connectionId}/test` — Token permission: `write:telephony`.
        """
        return self._request("POST", f"/api/telephony/connections/{_seg(connection_id)}/test", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def update(self, connection_id: str, body: PhoneConnectionPatch, *, options: Optional[RequestOptions] = None) -> PhoneConnection:
        """Renames a connection, gives it new credentials, pauses or resumes it, or rotates its webhook URL.
        
        Needs `telephony:manage`. New credentials are tested before they replace the old ones. A paused connection acknowledges and drops the provider's deliveries; after a rotation the old URL answers 404.
        
        `PATCH /api/telephony/connections/{connectionId}` — Token permission: `write:telephony`.
        """
        return _pick(self._request("PATCH", f"/api/telephony/connections/{_seg(connection_id)}", query=None, body=body, multipart=False, options=options), "connection")  # type: ignore[no-any-return]


class TelephonyLinesResource(_Resource):

    def create(self, body: PhoneLineInput, *, options: Optional[RequestOptions] = None) -> TelephonyLinesCreateResponseLine:
        """Adds a line by hand, for a provider or account whose lines cannot be listed.
        
        Needs `telephony:manage` in the connection's workspace and room under the plan's line limit. `providerLineId` is what the provider's webhook names the line by (sipgate: the user id `w0`; Placetel: the SIP user's sipuid); `providerDeviceId` is sipgate's device for click-to-call (`e0`).
        
        `POST /api/telephony/lines` — Token permission: `write:telephony`.
        """
        return _pick(self._request("POST", f"/api/telephony/lines", query=None, body=body, multipart=False, options=options), "line")  # type: ignore[no-any-return]

    def delete(self, line_id: str, *, options: Optional[RequestOptions] = None) -> TelephonyLinesDeleteResponse:
        """Deletes a line.
        
        Needs `telephony:manage`.
        
        `DELETE /api/telephony/lines/{lineId}` — Token permission: `write:telephony`.
        """
        return self._request("DELETE", f"/api/telephony/lines/{_seg(line_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def mine(self, *, workspace_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[PhoneUsableLine]:
        """The lines the caller may use right now, with whether click-to-call works on each.
        
        An empty list (never an error) when the caller has none.
        
        `GET /api/telephony/lines/mine` — Token permission: `read:telephony`.
        """
        return _pick(self._request("GET", f"/api/telephony/lines/mine", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options), "lines")  # type: ignore[no-any-return]

    def update(self, line_id: str, body: PhoneLinePatch, *, options: Optional[RequestOptions] = None) -> TelephonyLinesUpdateResponse:
        """Changes a line: its label, number, owner and members, whether its calls show in the CRM, and the missed-call task.
        
        Label, number, device, owner and members need `telephony:manage` (owner and members must be in the workspace). `crmSync` is the line owner's switch (a telephony manager's for a line nobody owns). `missedCallTask` and `taskSpaceId`: the owner or a telephony manager.
        
        `PATCH /api/telephony/lines/{lineId}` — Token permission: `write:telephony`.
        """
        return self._request("PATCH", f"/api/telephony/lines/{_seg(line_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class TelephonyResource(_Resource):
    """Telephony
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.calls = TelephonyCallsResource(request)
        self.connections = TelephonyConnectionsResource(request)
        self.lines = TelephonyLinesResource(request)

    def dial(self, body: TelephonyDialBody, *, options: Optional[RequestOptions] = None) -> TelephonyDialResponse:
        """Click-to-call: the provider rings the caller's own phone on that line, then the number.
        
        Needs a line the caller may use (404 otherwise). Nothing is stored; the call arrives in the log through the provider's webhook. Never retried on a server error, so a phone is not rung twice. Rate-limited.
        
        `POST /api/telephony/dial` — Token permission: `write:telephony`.
        """
        return self._request("POST", f"/api/telephony/dial", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def overview(self, *, workspace_id: str, options: Optional[RequestOptions] = None) -> TelephonyOverviewResponse:
        """A workspace's telephony: the providers that can be connected, the connections and the lines.
        
        A telephony manager sees every line and each connection's webhook URL; anybody else only the lines they own or were added to.
        
        `GET /api/telephony/overview` — Token permission: `read:telephony`.
        """
        return self._request("GET", f"/api/telephony/overview", query={"workspaceId": workspace_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class TemplatesResource(_Resource):
    """Templates
    """

    def create(self, body: CreateTemplateInput, *, options: Optional[RequestOptions] = None) -> Template:
        """Saves a component, page or workflow as a template.
        
        Needs `template.create`.
        
        `POST /api/templates`
        """
        return _pick(self._request("POST", f"/api/templates", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, template_id: str, *, options: Optional[RequestOptions] = None) -> TemplatesDeleteResponse:
        """Deletes a template.
        
        `DELETE /api/templates/{templateId}`
        """
        return self._request("DELETE", f"/api/templates/{_seg(template_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, template_id: str, *, options: Optional[RequestOptions] = None) -> Template:
        """Returns a template with its content.
        
        `GET /api/templates/{templateId}`
        """
        return _pick(self._request("GET", f"/api/templates/{_seg(template_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, workspace_id: Optional[str] = None, visibility: Optional[Literal["private", "workspace", "organization", "public"]] = None, category: Optional[str] = None, type_: Optional[Literal["component", "page", "workflow"]] = None, tags: Optional[str] = None, search: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Template]:
        """Lists the templates the caller may use in an organization — their private ones, the organization's and its workspaces', and public ones.
        
        The list leaves out each template's content; `templates.get` has it.
        
        `GET /api/templates`
        """
        return _pick(self._request("GET", f"/api/templates", query={"organizationId": organization_id, "workspaceId": workspace_id, "visibility": visibility, "category": category, "type": type_, "tags": tags, "search": search, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def replace(self, template_id: str, body: UpdateTemplateInput, *, options: Optional[RequestOptions] = None) -> Template:
        """Changes a template, exactly as `templates.update` does.
        
        `PUT /api/templates/{templateId}`
        """
        return _pick(self._request("PUT", f"/api/templates/{_seg(template_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, template_id: str, body: UpdateTemplateInput, *, options: Optional[RequestOptions] = None) -> Template:
        """Changes a template's details or content; only the fields sent change.
        
        Needs `template.update`; making it public needs `template.publish`.
        
        `PATCH /api/templates/{templateId}`
        """
        return _pick(self._request("PATCH", f"/api/templates/{_seg(template_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def use(self, template_id: str, body: TemplatesUseBody, *, options: Optional[RequestOptions] = None) -> Template:
        """Records that the template was used and returns it with its content.
        
        `POST /api/templates/{templateId}`
        """
        return _pick(self._request("POST", f"/api/templates/{_seg(template_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class TrashSettingsResource(_Resource):

    def get(self, *, organization_id: str, options: Optional[RequestOptions] = None) -> TrashSettingsGetResponseData:
        """How many days the organisation's trash keeps things, and the platform's limits.
        
        `GET /api/trash/settings`
        """
        return _pick(self._request("GET", f"/api/trash/settings", query={"organizationId": organization_id}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update(self, body: TrashSettingsUpdateBody, *, options: Optional[RequestOptions] = None) -> TrashSettingsUpdateResponseData:
        """Sets how many days the organisation's trash keeps things.
        
        Needs the `retention_policies:manage` permission. The days are held to the platform's limits; the answer says what was applied.
        
        `PUT /api/trash/settings`
        """
        return _pick(self._request("PUT", f"/api/trash/settings", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class TrashResource(_Resource):
    """Trash — What was deleted across every hub, until it is deleted for good: restore it, or delete it now.
    """

    def __init__(self, request: Requester) -> None:
        super().__init__(request)
        self.settings = TrashSettingsResource(request)

    def apply(self, body: TrashApplyBody, *, options: Optional[RequestOptions] = None) -> List[TrashActionResult]:
        """Restores items from the trash, or deletes them for good.
        
        Answers per item. A restore that clashes with something live (a page at its address, a file of the same name) answers `conflict` with what clashes; send that item again with `resolution`: `keepBoth` restores it under the suggested free name, `replace` moves the live one to the trash instead. Items the caller may not touch answer `forbidden` and are left alone. Deleting for good cannot be undone.
        
        `POST /api/trash`
        """
        return _pick(self._request("POST", f"/api/trash", query=None, body=body, multipart=False, options=options), "data.results")  # type: ignore[no-any-return]

    def empty(self, *, organization_id: str, kind: Optional[TrashKind] = None, options: Optional[RequestOptions] = None) -> TrashEmptyResponseData:
        """Empties the trash: deletes for good everything in it the caller may delete.
        
        Cannot be undone. With `kind`, only the items of that kind.
        
        `DELETE /api/trash`
        """
        return _pick(self._request("DELETE", f"/api/trash", query={"organizationId": organization_id, "kind": kind}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: str, kind: Optional[TrashKind] = None, options: Optional[RequestOptions] = None) -> List[TrashItem]:
        """Lists what the caller may restore from the organisation's trash, newest first, each with the day it goes for good.
        
        Per kind, an item is listed to whoever could have deleted it in the first place.
        
        `GET /api/trash`
        """
        return _pick(self._request("GET", f"/api/trash", query={"organizationId": organization_id, "kind": kind}, body=None, multipart=False, options=options), "data.items")  # type: ignore[no-any-return]


class UserResource(_Resource):
    """Current user
    """

    def add_ai_memory(self, body: UserAddAiMemoryBody, *, options: Optional[RequestOptions] = None) -> UserAddAiMemoryResponse:
        """Adds a note to what the AI assistant remembers.
        
        Workspace and organization notes need the right to manage that level's AI persona. With memory switched off nothing is stored: `stored: false` says why.
        
        `POST /api/user/ai-memory`
        """
        return self._request("POST", f"/api/user/ai-memory", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def claim_handle(self, body: UserClaimHandleBody, *, options: Optional[RequestOptions] = None) -> UserClaimHandleResponse:
        """Claims a public creator handle for the caller.
        
        `PUT /api/user/handle`
        """
        return self._request("PUT", f"/api/user/handle", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def clear_presence(self, *, options: Optional[RequestOptions] = None) -> UserClearPresenceResponse:
        """Clears the presence the caller set, back to automatic.
        
        `DELETE /api/user/presence`
        """
        return self._request("DELETE", f"/api/user/presence", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def count_ai_events(self, *, options: Optional[RequestOptions] = None) -> float:
        """Counts the records of the caller's AI generations kept for audit.
        
        `GET /api/user/ai-events`
        """
        return _pick(self._request("GET", f"/api/user/ai-events", query=None, body=None, multipart=False, options=options), "data.count")  # type: ignore[no-any-return]

    def create_signature(self, body: UserCreateSignatureBody, *, options: Optional[RequestOptions] = None) -> UserCreateSignatureResponseDataSignature:
        """Saves a signature image for signing documents.
        
        At most 8 per person, each a PNG data URL of at most 200 KB.
        
        `POST /api/user/signatures`
        """
        return _pick(self._request("POST", f"/api/user/signatures", query=None, body=body, multipart=False, options=options), "data.signature")  # type: ignore[no-any-return]

    def delete_ai_events(self, *, options: Optional[RequestOptions] = None) -> float:
        """Erases the records of the caller's AI generations.
        
        Only the audit records: what was generated (files, drafts) stays.
        
        `DELETE /api/user/ai-events`
        """
        return _pick(self._request("DELETE", f"/api/user/ai-events", query=None, body=None, multipart=False, options=options), "data.deleted")  # type: ignore[no-any-return]

    def delete_ai_memory(self, *, id: str, options: Optional[RequestOptions] = None) -> UserDeleteAiMemoryResponse:
        """Makes the AI assistant forget a note.
        
        `DELETE /api/user/ai-memory`
        """
        return self._request("DELETE", f"/api/user/ai-memory", query={"id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_avatar(self, *, options: Optional[RequestOptions] = None) -> UserDeleteAvatarResponse:
        """Removes the caller's profile picture.
        
        `DELETE /api/user/avatar`
        """
        return self._request("DELETE", f"/api/user/avatar", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_signature(self, signature_id: str, *, options: Optional[RequestOptions] = None) -> UserDeleteSignatureResponse:
        """Deletes a saved signature; the newest other one becomes the default.
        
        `DELETE /api/user/signatures/{signatureId}`
        """
        return self._request("DELETE", f"/api/user/signatures/{_seg(signature_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def export_activity_logs(self, *, format: Optional[Literal["json", "csv"]] = None, range: Optional[Literal["1d", "7d", "30d", "90d"]] = None, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> Any:
        """Downloads the activity the caller may see as a JSON or CSV file.
        
        Answers the file itself (`application/json` or `text/csv`).
        
        `GET /api/user/activity-logs/export`
        """
        return self._request("GET", f"/api/user/activity-logs/export", query={"format": format, "range": range, "organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def forget_recognized_device(self, *, id: str, options: Optional[RequestOptions] = None) -> UserForgetRecognizedDeviceResponse:
        """Forgets a recognized device, so the next sign-in from it is reported as new.
        
        `DELETE /api/user/recognized-devices`
        """
        return self._request("DELETE", f"/api/user/recognized-devices", query={"id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_ai_memory(self, *, options: Optional[RequestOptions] = None) -> UserGetAiMemoryResponse:
        """Lists what the AI assistant remembers — about the caller, and at the workspaces and organizations they belong to.
        
        `GET /api/user/ai-memory`
        """
        return self._request("GET", f"/api/user/ai-memory", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_ai_memory_switch(self, *, options: Optional[RequestOptions] = None) -> UserGetAiMemorySwitchResponse:
        """Returns whether the AI assistant may remember things about the caller.
        
        `GET /api/user/ai-memory/switch`
        """
        return self._request("GET", f"/api/user/ai-memory/switch", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_handoff(self, *, options: Optional[RequestOptions] = None) -> UserGetHandoffResponse:
        """Returns until when the caller is away, and their away message.
        
        `GET /api/user/handoff`
        """
        return self._request("GET", f"/api/user/handoff", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_preferences(self, *, options: Optional[RequestOptions] = None) -> UserPreferences:
        """Returns the caller's preferences — look, language, regional formats, notifications, defaults.
        
        `GET /api/user/preferences`
        """
        return self._request("GET", f"/api/user/preferences", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_presence(self, *, user_ids: Optional[str] = None, options: Optional[RequestOptions] = None) -> List[UserGetPresenceResponseDataItem]:
        """Returns the presence — online, away, do not disturb — of the caller and up to 200 other people.
        
        `GET /api/user/presence`
        """
        return _pick(self._request("GET", f"/api/user/presence", query={"userIds": user_ids}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_presence_settings(self, *, options: Optional[RequestOptions] = None) -> UserGetPresenceSettingsResponseData:
        """Returns what sets the caller's presence automatically and who sees it.
        
        `GET /api/user/presence/settings`
        """
        return _pick(self._request("GET", f"/api/user/presence/settings", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_profile(self, *, options: Optional[RequestOptions] = None) -> UserProfile:
        """Returns the caller's own profile.
        
        `GET /api/user/profile`
        """
        return _pick(self._request("GET", f"/api/user/profile", query=None, body=None, multipart=False, options=options), "profile")  # type: ignore[no-any-return]

    def get_security(self, *, options: Optional[RequestOptions] = None) -> UserGetSecurityResponse:
        """Returns whether the caller has two-factor sign-in on.
        
        `GET /api/user/security`
        """
        return self._request("GET", f"/api/user/security", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_activity_logs(self, *, range: Optional[Literal["1d", "7d", "30d", "90d"]] = None, organization_id: Optional[str] = None, resource_type: Optional[str] = None, action: Optional[str] = None, result: Optional[str] = None, search: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[ActivityLog]:
        """Lists the activity the caller may see in the audit log — their own, and their organizations' for administrators.
        
        `GET /api/user/activity-logs`
        """
        return _pick(self._request("GET", f"/api/user/activity-logs", query={"range": range, "organizationId": organization_id, "resourceType": resource_type, "action": action, "result": result, "search": search, "page": page, "limit": limit}, body=None, multipart=False, options=options), "logs")  # type: ignore[no-any-return]

    def list_recognized_devices(self, *, options: Optional[RequestOptions] = None) -> List[UserListRecognizedDevicesResponseDevicesItem]:
        """Lists the devices and places the caller has signed in from.
        
        `GET /api/user/recognized-devices`
        """
        return _pick(self._request("GET", f"/api/user/recognized-devices", query=None, body=None, multipart=False, options=options), "devices")  # type: ignore[no-any-return]

    def list_signatures(self, *, options: Optional[RequestOptions] = None) -> List[UserListSignaturesResponseDataSignaturesItem]:
        """Lists the caller's saved signatures for signing documents.
        
        `GET /api/user/signatures`
        """
        return _pick(self._request("GET", f"/api/user/signatures", query=None, body=None, multipart=False, options=options), "data.signatures")  # type: ignore[no-any-return]

    def patch_preferences(self, body: UserPreferences, *, options: Optional[RequestOptions] = None) -> UserPreferences:
        """Merges the given keys into the caller's preferences, exactly as `user.updatePreferences` does.
        
        `PATCH /api/user/preferences`
        """
        return self._request("PATCH", f"/api/user/preferences", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def release_handle(self, *, options: Optional[RequestOptions] = None) -> UserReleaseHandleResponse:
        """Gives up the caller's public creator handle.
        
        `DELETE /api/user/handle`
        """
        return self._request("DELETE", f"/api/user/handle", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set_ai_memory_switch(self, body: UserSetAiMemorySwitchBody, *, options: Optional[RequestOptions] = None) -> UserSetAiMemorySwitchResponse:
        """Lets the AI assistant remember things about the caller, or stops it.
        
        `PUT /api/user/ai-memory/switch`
        """
        return self._request("PUT", f"/api/user/ai-memory/switch", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def set_handoff(self, body: UserSetHandoffBody, *, options: Optional[RequestOptions] = None) -> UserSetHandoffResponse:
        """Marks the caller away until a date, with a message — or back with `until: null`.
        
        `PUT /api/user/handoff`
        """
        return self._request("PUT", f"/api/user/handoff", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def set_presence(self, body: UserSetPresenceBody, *, options: Optional[RequestOptions] = None) -> UserSetPresenceResponse:
        """Sets the caller's own presence and status text, optionally until a time.
        
        `PUT /api/user/presence`
        """
        return self._request("PUT", f"/api/user/presence", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_ai_memory(self, body: UserUpdateAiMemoryBody, *, id: str, options: Optional[RequestOptions] = None) -> UserUpdateAiMemoryResponse:
        """Changes a note the AI assistant remembers.
        
        `PATCH /api/user/ai-memory`
        """
        return self._request("PATCH", f"/api/user/ai-memory", query={"id": id}, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_avatar(self, body: Union[UserUpdateAvatarBody, Dict[str, Any]], *, options: Optional[RequestOptions] = None) -> str:
        """Uploads a new profile picture for the caller.
        
        An image of at most 5 MB; SVG is refused.
        
        `POST /api/user/avatar`
        """
        return _pick(self._request("POST", f"/api/user/avatar", query=None, body=body, multipart=True, options=options), "avatarUrl")  # type: ignore[no-any-return]

    def update_preferences(self, body: UserPreferences, *, options: Optional[RequestOptions] = None) -> UserPreferences:
        """Merges the given keys into the caller's preferences and returns them all.
        
        A shallow merge: keys left out keep their value. Keys the platform does not know are dropped, and security notifications cannot be switched off.
        
        `PUT /api/user/preferences`
        """
        return self._request("PUT", f"/api/user/preferences", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def update_presence_settings(self, body: UserUpdatePresenceSettingsBody, *, options: Optional[RequestOptions] = None) -> UserUpdatePresenceSettingsResponseData:
        """Changes what sets the caller's presence automatically and who sees it.
        
        `PUT /api/user/presence/settings`
        """
        return _pick(self._request("PUT", f"/api/user/presence/settings", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def update_profile(self, body: UpdateProfileInput, *, options: Optional[RequestOptions] = None) -> UserProfile:
        """Changes the caller's profile.
        
        `fullName` is required. The email address is changed elsewhere, with confirmation. Send `If-Unmodified-Since` with the profile's `updatedAt` to get a 409 instead of overwriting a newer save.
        
        `PUT /api/user/profile`
        """
        return _pick(self._request("PUT", f"/api/user/profile", query=None, body=body, multipart=False, options=options), "profile")  # type: ignore[no-any-return]

    def update_signature(self, signature_id: str, body: UserUpdateSignatureBody, *, options: Optional[RequestOptions] = None) -> UserUpdateSignatureResponse:
        """Renames a saved signature or makes it the default.
        
        `PATCH /api/user/signatures/{signatureId}`
        """
        return self._request("PATCH", f"/api/user/signatures/{_seg(signature_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class UsersResource(_Resource):
    """Users
    """

    def list_organizations(self, user_id: str, *, options: Optional[RequestOptions] = None) -> List[Organization]:
        """Lists the organizations a user belongs to — only for the caller.
        
        `GET /api/users/{userId}/organizations`
        """
        return _pick(self._request("GET", f"/api/users/{_seg(user_id)}/organizations", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_roles(self, user_id: str, *, options: Optional[RequestOptions] = None) -> List[Role]:
        """Lists the roles a user holds, directly and through teams — only for the caller.
        
        `GET /api/users/{userId}/roles`
        """
        return _pick(self._request("GET", f"/api/users/{_seg(user_id)}/roles", query=None, body=None, multipart=False, options=options), "roles")  # type: ignore[no-any-return]

    def list_workspaces(self, user_id: str, *, options: Optional[RequestOptions] = None) -> List[Workspace]:
        """Lists the workspaces a user is a member of — only for the caller.
        
        `GET /api/users/{userId}/workspaces`
        """
        return _pick(self._request("GET", f"/api/users/{_seg(user_id)}/workspaces", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class VariablesResource(_Resource):
    """Workflow variables — Values workflows store and read between runs.
    """

    def get(self, *, key: str, options: Optional[RequestOptions] = None) -> VariablesGetResponse:
        """Reads a workflow variable by its key.
        
        Needs `workflow.read` in the variable's workspace; an expired variable reads as not found.
        
        `GET /api/variables/get`
        """
        return self._request("GET", f"/api/variables/get", query={"key": key}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def save(self, body: VariablesSaveBody, *, options: Optional[RequestOptions] = None) -> VariablesSaveResponse:
        """Creates or replaces a workflow variable.
        
        Needs `workflow.update` in the workspace. `key` must be the one `workspaceId`, `name` and (for `workflow` scope) `workflowId` make.
        
        `POST /api/variables/save`
        """
        return self._request("POST", f"/api/variables/save", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]


class WebhooksResource(_Resource):
    """Webhooks — Subscriptions that post platform events to your URL.
    """

    def get_subscription(self, id: str, *, options: Optional[RequestOptions] = None) -> WebhookSubscription:
        """Returns one of the caller's webhook subscriptions, without its secret.
        
        `GET /api/webhooks/subscribe/{id}`
        """
        return _pick(self._request("GET", f"/api/webhooks/subscribe/{_seg(id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_subscriptions(self, *, event: Optional[Literal["project.created", "project.updated", "project.deleted", "page.created", "page.updated", "page.deleted", "page.published", "workflow.created", "workflow.updated", "workflow.deleted", "workflow.completed", "workflow.failed", "database.created", "database.updated", "database.deleted", "database_record.created", "database_record.updated", "database_record.deleted", "asset.uploaded", "asset.deleted", "member.added", "member.removed", "form.submitted"]] = None, options: Optional[RequestOptions] = None) -> List[WebhookSubscription]:
        """Lists the caller's webhook subscriptions, without their secrets.
        
        `GET /api/webhooks/subscribe`
        """
        return _pick(self._request("GET", f"/api/webhooks/subscribe", query={"event": event}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def subscribe(self, body: WebhooksSubscribeBody, *, options: Optional[RequestOptions] = None) -> WebhooksSubscribeResponseData:
        """Subscribes a URL to an event of an organization; the answer carries the signing secret, once.
        
        Counts against the plan's `max_webhook_subscriptions`.
        
        `POST /api/webhooks/subscribe`
        """
        return _pick(self._request("POST", f"/api/webhooks/subscribe", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def unsubscribe(self, id: str, *, options: Optional[RequestOptions] = None) -> WebhooksUnsubscribeResponse:
        """Deletes a webhook subscription.
        
        `DELETE /api/webhooks/subscribe/{id}`
        """
        return self._request("DELETE", f"/api/webhooks/subscribe/{_seg(id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class WorkflowsResource(_Resource):
    """Workflows
    """

    def create(self, body: WorkflowsCreateBody, *, options: Optional[RequestOptions] = None) -> Workflow:
        """Creates a workflow.
        
        Needs `workflow.create`; counts against the plan's `max_workflows`. Connections a node names must be ones the caller may use.
        
        `POST /api/workflows`
        """
        return self._request("POST", f"/api/workflows", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def create_alert(self, workflow_id: str, body: WorkflowsCreateAlertBody, *, options: Optional[RequestOptions] = None) -> WorkflowsCreateAlertResponseAlert:
        """Emails the given addresses when a workflow fails a number of times within a window.
        
        `POST /api/workflows/{workflowId}/alerts`
        """
        return _pick(self._request("POST", f"/api/workflows/{_seg(workflow_id)}/alerts", query=None, body=body, multipart=False, options=options), "alert")  # type: ignore[no-any-return]

    def create_version(self, workflow_id: str, body: WorkflowsCreateVersionBody, *, options: Optional[RequestOptions] = None) -> WorkflowVersion:
        """Saves a version of a workflow.
        
        `POST /api/workflows/{workflowId}/versions`
        """
        return self._request("POST", f"/api/workflows/{_seg(workflow_id)}/versions", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> WorkflowsDeleteResponse:
        """Moves a workflow to the trash; it stops running.
        
        `DELETE /api/workflows/{workflowId}`
        """
        return self._request("DELETE", f"/api/workflows/{_seg(workflow_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_alert(self, workflow_id: str, *, alert_id: str, options: Optional[RequestOptions] = None) -> WorkflowsDeleteAlertResponse:
        """Removes a workflow's failure alert.
        
        `DELETE /api/workflows/{workflowId}/alerts`
        """
        return self._request("DELETE", f"/api/workflows/{_seg(workflow_id)}/alerts", query={"alertId": alert_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_dead_letter(self, *, id: str, options: Optional[RequestOptions] = None) -> WorkflowsDeleteDeadLetterResponse:
        """Removes an entry from the dead-letter queue.
        
        `DELETE /api/workflows/dead-letter-queue`
        """
        return self._request("DELETE", f"/api/workflows/dead-letter-queue", query={"id": id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_version(self, workflow_id: str, version_id: str, *, options: Optional[RequestOptions] = None) -> WorkflowsDeleteVersionResponse:
        """Deletes one saved version of a workflow.
        
        `DELETE /api/workflows/{workflowId}/versions/{versionId}`
        """
        return self._request("DELETE", f"/api/workflows/{_seg(workflow_id)}/versions/{_seg(version_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def delete_versions(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> WorkflowsDeleteVersionsResponse:
        """Deletes every saved version of a workflow.
        
        `DELETE /api/workflows/{workflowId}/versions`
        """
        return self._request("DELETE", f"/api/workflows/{_seg(workflow_id)}/versions", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def duplicate(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> Workflow:
        """Copies a workflow as a new draft.
        
        Counts against the plan's `max_workflows`.
        
        `POST /api/workflows/{workflowId}/duplicate`
        """
        return self._request("POST", f"/api/workflows/{_seg(workflow_id)}/duplicate", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def execute(self, workflow_id: str, body: WorkflowsExecuteBody, *, options: Optional[RequestOptions] = None) -> WorkflowsExecuteResponse:
        """Runs a workflow now with the given trigger data; the run is queued.
        
        Needs `workflow.execute` or `workflow.update`. Poll `workflows.listExecutions` for the outcome.
        
        `POST /api/workflows/{workflowId}/executions`
        """
        return self._request("POST", f"/api/workflows/{_seg(workflow_id)}/executions", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def export(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> WorkflowExport:
        """Exports a workflow as JSON for `workflows.import`, without stored credentials.
        
        `GET /api/workflows/{workflowId}/export`
        """
        return self._request("GET", f"/api/workflows/{_seg(workflow_id)}/export", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> Workflow:
        """Returns a workflow — trigger, nodes and edges — with its run counts.
        
        `GET /api/workflows/{workflowId}`
        """
        return self._request("GET", f"/api/workflows/{_seg(workflow_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get_version(self, workflow_id: str, version_id: str, *, options: Optional[RequestOptions] = None) -> WorkflowVersion:
        """Returns one saved version of a workflow.
        
        `GET /api/workflows/{workflowId}/versions/{versionId}`
        """
        return self._request("GET", f"/api/workflows/{_seg(workflow_id)}/versions/{_seg(version_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def import_(self, body: WorkflowsImportBody, *, options: Optional[RequestOptions] = None) -> Workflow:
        """Creates a workflow from an export.
        
        Takes the export as it is (`{ workflow: {…} }`) or its fields at the top level.
        
        `POST /api/workflows/import`
        """
        return _pick(self._request("POST", f"/api/workflows/import", query=None, body=body, multipart=False, options=options), "workflow")  # type: ignore[no-any-return]

    def install_recipe(self, body: WorkflowsInstallRecipeBody, *, options: Optional[RequestOptions] = None) -> WorkflowsInstallRecipeResponseData:
        """Creates a draft workflow from a recipe and the answers to its inputs.
        
        `POST /api/workflows/recipes`
        """
        return _pick(self._request("POST", f"/api/workflows/recipes", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, workspace_id: Optional[str] = None, visibility: Optional[Literal["private", "organization", "workspace", "public"]] = None, status: Optional[Literal["draft", "active", "inactive", "archived"]] = None, created_by: Optional[str] = None, category: Optional[str] = None, tags: Optional[str] = None, search: Optional[str] = None, folder: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Workflow]:
        """Lists the workflows the caller may open, with their run counts.
        
        `GET /api/workflows`
        """
        return _pick(self._request("GET", f"/api/workflows", query={"organizationId": organization_id, "workspaceId": workspace_id, "visibility": visibility, "status": status, "createdBy": created_by, "category": category, "tags": tags, "search": search, "folder": folder, "page": page, "limit": limit}, body=None, multipart=False, options=options), "workflows")  # type: ignore[no-any-return]

    def list_alerts(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> List[WorkflowsListAlertsResponseAlertsItem]:
        """Lists a workflow's failure alerts.
        
        `GET /api/workflows/{workflowId}/alerts`
        """
        return _pick(self._request("GET", f"/api/workflows/{_seg(workflow_id)}/alerts", query=None, body=None, multipart=False, options=options), "alerts")  # type: ignore[no-any-return]

    def list_all_dead_letters(self, *, options: Optional[RequestOptions] = None) -> List[DeadLetterJob]:
        """Lists the runs that failed for good, of every workflow the caller may open.
        
        `GET /api/workflows/dead-letter-queue`
        """
        return self._request("GET", f"/api/workflows/dead-letter-queue", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_dead_letter_queue(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> List[DeadLetterJob]:
        """Lists a workflow's runs that failed for good.
        
        `GET /api/workflows/{workflowId}/dead-letter-queue`
        """
        return self._request("GET", f"/api/workflows/{_seg(workflow_id)}/dead-letter-queue", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_executions(self, workflow_id: str, *, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[WorkflowExecution]:
        """Lists a workflow's latest runs with their steps.
        
        With an execution id (`exec-…`) in place of the workflow id it answers that one run instead.
        
        `GET /api/workflows/{workflowId}/executions`
        """
        return self._request("GET", f"/api/workflows/{_seg(workflow_id)}/executions", query={"limit": limit}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def list_recipes(self, *, options: Optional[RequestOptions] = None) -> List[WorkflowsListRecipesResponseDataRecipesItem]:
        """Lists the ready-made workflows that can be installed with a few answers.
        
        `GET /api/workflows/recipes`
        """
        return _pick(self._request("GET", f"/api/workflows/recipes", query=None, body=None, multipart=False, options=options), "data.recipes")  # type: ignore[no-any-return]

    def list_versions(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> List[WorkflowVersion]:
        """Lists a workflow's saved versions, newest first.
        
        `GET /api/workflows/{workflowId}/versions`
        """
        return self._request("GET", f"/api/workflows/{_seg(workflow_id)}/versions", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def queue(self, workflow_id: str, *, action: Optional[Literal["rateLimit"]] = None, options: Optional[RequestOptions] = None) -> Any:
        """Lists a workflow's queued runs, or with `action=rateLimit` its rate-limit state.
        
        `GET /api/workflows/{workflowId}/queue`
        """
        return self._request("GET", f"/api/workflows/{_seg(workflow_id)}/queue", query={"action": action}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def replay_execution(self, workflow_id: str, execution_id: str, body: WorkflowsReplayExecutionBody, *, options: Optional[RequestOptions] = None) -> Dict[str, Any]:
        """Runs a past execution again from one of its nodes, with the data it had there.
        
        `POST /api/workflows/{workflowId}/executions/{executionId}/replay`
        """
        return _pick(self._request("POST", f"/api/workflows/{_seg(workflow_id)}/executions/{_seg(execution_id)}/replay", query=None, body=body, multipart=False, options=options), "data.execution")  # type: ignore[no-any-return]

    def restore_version(self, workflow_id: str, version_id: str, body: WorkflowsRestoreVersionBody, *, options: Optional[RequestOptions] = None) -> Workflow:
        """Puts a saved version back as the workflow.
        
        `POST /api/workflows/{workflowId}/versions/{versionId}`
        """
        return _pick(self._request("POST", f"/api/workflows/{_seg(workflow_id)}/versions/{_seg(version_id)}", query=None, body=body, multipart=False, options=options), "workflow")  # type: ignore[no-any-return]

    def retry_dead_job(self, workflow_id: str, body: WorkflowsRetryDeadJobBody, *, options: Optional[RequestOptions] = None) -> WorkflowExecution:
        """Runs a failed run of the dead-letter queue again.
        
        `POST /api/workflows/{workflowId}/dead-letter-queue`
        """
        return _pick(self._request("POST", f"/api/workflows/{_seg(workflow_id)}/dead-letter-queue", query=None, body=body, multipart=False, options=options), "executionLog")  # type: ignore[no-any-return]

    def set_status(self, workflow_id: str, body: WorkflowsSetStatusBody, *, options: Optional[RequestOptions] = None) -> Workflow:
        """Activates, pauses or drafts a workflow.
        
        `PATCH /api/workflows/{workflowId}/status`
        """
        return _pick(self._request("PATCH", f"/api/workflows/{_seg(workflow_id)}/status", query=None, body=body, multipart=False, options=options), "workflow")  # type: ignore[no-any-return]

    def toggle_status(self, workflow_id: str, *, options: Optional[RequestOptions] = None) -> Workflow:
        """Switches a workflow between active and paused.
        
        `POST /api/workflows/{workflowId}/status`
        
        .. deprecated:: 0.2.0 Toggling depends on the state the caller last saw; set the status explicitly. Use `workflows.setStatus`.
        """
        _deprecated("workflows.toggleStatus")
        return _pick(self._request("POST", f"/api/workflows/{_seg(workflow_id)}/status", query=None, body=None, multipart=False, options=options), "workflow")  # type: ignore[no-any-return]

    def update(self, workflow_id: str, body: WorkflowsUpdateBody, *, options: Optional[RequestOptions] = None) -> Workflow:
        """Changes a workflow; only the fields sent change.
        
        Needs `workflow.update`. A trigger or status change reaches the scheduler at once.
        
        `PUT /api/workflows/{workflowId}`
        """
        return self._request("PUT", f"/api/workflows/{_seg(workflow_id)}", query=None, body=body, multipart=False, options=options)  # type: ignore[no-any-return]

    def usage(self, *, organization_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> WorkflowsUsageResponse:
        """Returns an organization's workflow runs per day against its daily cap.
        
        `GET /api/workflows/usage`
        """
        return self._request("GET", f"/api/workflows/usage", query={"organizationId": organization_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]


class WorkspacesResource(_Resource):
    """Workspaces
    """

    def add_member(self, workspace_id: str, body: WorkspacesAddMemberBody, *, options: Optional[RequestOptions] = None) -> WorkspaceMember:
        """Adds a member of the organization to a workspace, optionally with a role in it.
        
        Needs `workspace.manage_members`.
        
        `POST /api/workspaces/{workspaceId}/members`
        """
        return _pick(self._request("POST", f"/api/workspaces/{_seg(workspace_id)}/members", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def assign_member_role(self, workspace_id: str, member_id: str, body: WorkspacesAssignMemberRoleBody, *, options: Optional[RequestOptions] = None) -> RoleAssignment:
        """Gives a workspace member a role in the workspace.
        
        Needs `role.assign`; only roles within the caller's own permissions.
        
        `POST /api/workspaces/{workspaceId}/members/{memberId}/assign-role`
        """
        return _pick(self._request("POST", f"/api/workspaces/{_seg(workspace_id)}/members/{_seg(member_id)}/assign-role", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def assign_team(self, workspace_id: str, body: WorkspacesAssignTeamBody, *, options: Optional[RequestOptions] = None) -> TeamRoleAssignment:
        """Gives a team a role in a workspace.
        
        Needs `team.assign`.
        
        `POST /api/workspaces/{workspaceId}/teams`
        """
        return _pick(self._request("POST", f"/api/workspaces/{_seg(workspace_id)}/teams", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def cancel_deletion(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> WorkspacesCancelDeletionResponseData:
        """Cancels a workspace's scheduled deletion.
        
        `DELETE /api/workspaces/{workspaceId}/scheduled-deletion`
        """
        return _pick(self._request("DELETE", f"/api/workspaces/{_seg(workspace_id)}/scheduled-deletion", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def create(self, body: WorkspacesCreateBody, *, options: Optional[RequestOptions] = None) -> Workspace:
        """Creates a workspace in an organization, with the caller as its first member.
        
        Needs `workspace.create`; counts against the plan's `max_workspaces`.
        
        `POST /api/workspaces`
        """
        return _pick(self._request("POST", f"/api/workspaces", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> WorkspacesDeleteResponseData:
        """Schedules a workspace for deletion in 14 days.
        
        Needs `workspace.delete`. Until then it can be cancelled with `workspaces.cancelDeletion`.
        
        `DELETE /api/workspaces/{workspaceId}`
        """
        return _pick(self._request("DELETE", f"/api/workspaces/{_seg(workspace_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def delete_env_var(self, workspace_id: str, *, key: str, options: Optional[RequestOptions] = None) -> WorkspacesDeleteEnvVarResponse:
        """Removes a workspace variable.
        
        `DELETE /api/workspaces/{workspaceId}/env-vars`
        """
        return self._request("DELETE", f"/api/workspaces/{_seg(workspace_id)}/env-vars", query={"key": key}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def get(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> Workspace:
        """Returns one workspace.
        
        `GET /api/workspaces/{workspaceId}` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/workspaces/{_seg(workspace_id)}", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def get_scheduled_deletion(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> WorkspacesGetScheduledDeletionResponseData:
        """Returns when a workspace is due to be deleted, if it is.
        
        `GET /api/workspaces/{workspaceId}/scheduled-deletion`
        """
        return _pick(self._request("GET", f"/api/workspaces/{_seg(workspace_id)}/scheduled-deletion", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list(self, *, organization_id: Optional[str] = None, search: Optional[str] = None, page: Optional[int] = None, limit: Optional[int] = None, options: Optional[RequestOptions] = None) -> List[Workspace]:
        """Lists the workspaces the caller can open, optionally of one organization.
        
        `GET /api/workspaces` — Token permission: `read:projects`.
        """
        return _pick(self._request("GET", f"/api/workspaces", query={"organizationId": organization_id, "search": search, "page": page, "limit": limit}, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_env_vars(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> List[WorkspaceEnvVar]:
        """Lists a workspace's variables, which its workflows read as `{{env.NAME}}`.
        
        Needs `workflow.read` in the workspace. A secret's value is never answered.
        
        `GET /api/workspaces/{workspaceId}/env-vars`
        """
        return _pick(self._request("GET", f"/api/workspaces/{_seg(workspace_id)}/env-vars", query=None, body=None, multipart=False, options=options), "envVars")  # type: ignore[no-any-return]

    def list_members(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> List[WorkspaceMember]:
        """Lists a workspace's members with their user details and roles.
        
        `GET /api/workspaces/{workspaceId}/members`
        """
        return _pick(self._request("GET", f"/api/workspaces/{_seg(workspace_id)}/members", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def list_teams(self, workspace_id: str, *, options: Optional[RequestOptions] = None) -> List[WorkspacesListTeamsResponseDataItem]:
        """Lists the teams with a role in a workspace.
        
        `GET /api/workspaces/{workspaceId}/teams`
        """
        return _pick(self._request("GET", f"/api/workspaces/{_seg(workspace_id)}/teams", query=None, body=None, multipart=False, options=options), "data")  # type: ignore[no-any-return]

    def remove_member(self, workspace_id: str, member_id: str, *, options: Optional[RequestOptions] = None) -> WorkspacesRemoveMemberResponse:
        """Removes a member from a workspace.
        
        `DELETE /api/workspaces/{workspaceId}/members/{memberId}`
        """
        return self._request("DELETE", f"/api/workspaces/{_seg(workspace_id)}/members/{_seg(member_id)}", query=None, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def remove_member_role(self, workspace_id: str, member_id: str, *, role_id: str, options: Optional[RequestOptions] = None) -> WorkspacesRemoveMemberRoleResponse:
        """Takes a role in the workspace away from a member.
        
        `DELETE /api/workspaces/{workspaceId}/members/{memberId}/assign-role`
        """
        return self._request("DELETE", f"/api/workspaces/{_seg(workspace_id)}/members/{_seg(member_id)}/assign-role", query={"roleId": role_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def remove_team(self, workspace_id: str, team_id: str, *, role_id: Optional[str] = None, options: Optional[RequestOptions] = None) -> WorkspacesRemoveTeamResponse:
        """Takes a team's roles in a workspace away — all of them, or one with `roleId`.
        
        `DELETE /api/workspaces/{workspaceId}/teams/{teamId}`
        """
        return self._request("DELETE", f"/api/workspaces/{_seg(workspace_id)}/teams/{_seg(team_id)}", query={"roleId": role_id}, body=None, multipart=False, options=options)  # type: ignore[no-any-return]

    def set_env_var(self, workspace_id: str, body: WorkspacesSetEnvVarBody, *, options: Optional[RequestOptions] = None) -> WorkspaceEnvVar:
        """Creates or replaces a workspace variable.
        
        Needs `workflow.update` in the workspace. A secret is sealed at rest; sending the mask back as its value keeps the stored one.
        
        `POST /api/workspaces/{workspaceId}/env-vars`
        """
        return _pick(self._request("POST", f"/api/workspaces/{_seg(workspace_id)}/env-vars", query=None, body=body, multipart=False, options=options), "envVar")  # type: ignore[no-any-return]

    def update(self, workspace_id: str, body: WorkspacesUpdateBody, *, options: Optional[RequestOptions] = None) -> Workspace:
        """Changes a workspace's name, description, icon, color or settings.
        
        `PUT /api/workspaces/{workspaceId}`
        """
        return _pick(self._request("PUT", f"/api/workspaces/{_seg(workspace_id)}", query=None, body=body, multipart=False, options=options), "data")  # type: ignore[no-any-return]


class Resources:
    """Every top-level resource — what `Crafvy` exposes."""

    def __init__(self, request: Requester) -> None:
        self.ab_tests = AbTestsResource(request)
        self.ads = AdsResource(request)
        self.agents = AgentsResource(request)
        self.ai = AiResource(request)
        self.analytics = AnalyticsResource(request)
        self.announcements = AnnouncementsResource(request)
        self.approvals = ApprovalsResource(request)
        self.apps = AppsResource(request)
        self.asset_folders = AssetFoldersResource(request)
        self.assets = AssetsResource(request)
        self.asset_shares = AssetSharesResource(request)
        self.audit_logs = AuditLogsResource(request)
        self.banking = BankingResource(request)
        self.billing = BillingResource(request)
        self.builder_blocks = BuilderBlocksResource(request)
        self.calendar = CalendarResource(request)
        self.code = CodeResource(request)
        self.community = CommunityResource(request)
        self.connections = ConnectionsResource(request)
        self.countries = CountriesResource(request)
        self.creators = CreatorsResource(request)
        self.crm = CrmResource(request)
        self.currencies = CurrenciesResource(request)
        self.dashboards = DashboardsResource(request)
        self.data = DataResource(request)
        self.databases = DatabasesResource(request)
        self.documents = DocumentsResource(request)
        self.endpoints = EndpointsResource(request)
        self.feature_gates = FeatureGatesResource(request)
        self.feature_requests = FeatureRequestsResource(request)
        self.help = HelpResource(request)
        self.invoicing = InvoicingResource(request)
        self.item_folders = ItemFoldersResource(request)
        self.languages = LanguagesResource(request)
        self.mail = MailResource(request)
        self.marketplace = MarketplaceResource(request)
        self.messenger = MessengerResource(request)
        self.milestones = MilestonesResource(request)
        self.notifications = NotificationsResource(request)
        self.oauth = OauthResource(request)
        self.organizations = OrganizationsResource(request)
        self.pages = PagesResource(request)
        self.pdf = PdfResource(request)
        self.permissions = PermissionsResource(request)
        self.privacy_requests = PrivacyRequestsResource(request)
        self.products = ProductsResource(request)
        self.projects = ProjectsResource(request)
        self.push = PushResource(request)
        self.referrals = ReferralsResource(request)
        self.regional_settings = RegionalSettingsResource(request)
        self.reports = ReportsResource(request)
        self.retention_policies = RetentionPoliciesResource(request)
        self.roles = RolesResource(request)
        self.share = ShareResource(request)
        self.social = SocialResource(request)
        self.submissions = SubmissionsResource(request)
        self.subscriptions = SubscriptionsResource(request)
        self.support = SupportResource(request)
        self.tasks = TasksResource(request)
        self.tax_rates = TaxRatesResource(request)
        self.teams = TeamsResource(request)
        self.telephony = TelephonyResource(request)
        self.templates = TemplatesResource(request)
        self.trash = TrashResource(request)
        self.user = UserResource(request)
        self.users = UsersResource(request)
        self.variables = VariablesResource(request)
        self.webhooks = WebhooksResource(request)
        self.workflows = WorkflowsResource(request)
        self.workspaces = WorkspacesResource(request)
