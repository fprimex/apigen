class TFCAPI(object):
    "Class generated from TFC API documentation. See api_gen.py."

    def __init__(self):
        pass

    def call(self, path, query=None, method='GET', data=None,
             files=None, get_all_pages=False, complete_response=False,
             **kwargs):
        pass

    def account_details_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/account"
        api_path = "/account/details"
        return self.call(api_path, **kwargs)

    def admin_organization(self, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/organizations"
        api_path = "/admin/organizations/{name}"
        api_path = api_path.format(name=name)
        return self.call(api_path, method="DELETE", **kwargs)

    def admin_user(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/admin/users/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def admin_user_actions_disable_two_factor(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/admin/users/{id}/actions/disable_two_factor"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def admin_user_actions_grant_admin(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/admin/users/{id}/actions/grant_admin"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def admin_user_actions_impersonate(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/admin/users/{id}/actions/impersonate"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def admin_user_actions_revoke_admin(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/admin/users/{id}/actions/revoke_admin"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def admin_user_actions_suspend(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/admin/users/{id}/actions/suspend"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def admin_user_actions_unsuspend(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/admin/users/{id}/actions/unsuspend"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def admin_users_actions_unimpersonate(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/admin/users/actions/unimpersonate"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def admin_workspace(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/workspaces"
        api_path = "/admin/workspaces/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def agent_delete(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agents"
        api_path = "/agents/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def agent_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agents"
        api_path = "/agents/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def api_v2_admin_organization(self, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/organizations"
        api_path = "/api/v2/admin/organizations/{name}"
        api_path = api_path.format(name=name)
        return self.call(api_path, **kwargs)

    def api_v2_admin_organizations(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/organizations"
        api_path = "/api/v2/admin/organizations"
        return self.call(api_path, **kwargs)

    def api_v2_admin_runs(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/runs"
        api_path = "/api/v2/admin/runs"
        return self.call(api_path, **kwargs)

    def api_v2_admin_users(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/users"
        api_path = "/api/v2/admin/users"
        return self.call(api_path, **kwargs)

    def api_v2_admin_workspace(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/workspaces"
        api_path = "/api/v2/admin/workspaces/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def api_v2_admin_workspaces(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/workspaces"
        api_path = "/api/v2/admin/workspaces"
        return self.call(api_path, **kwargs)

    def apply(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/applies"
        api_path = "/applies/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization_create(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_delete(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations/{organization_name}"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_invoices_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/invoices"
        api_path = "/organizations/{organization_name}/invoices"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_invoices_next_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/invoices"
        api_path = "/organizations/{organization_name}/invoices/next"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_policies_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policies"
        api_path = "/organizations/{organization_name}/policies"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_policy_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policies"
        api_path = "/organizations/{organization_name}/policies"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_show(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations/{organization_name}"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_subscription_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/subscriptions"
        api_path = "/organizations/{organization_name}/subscription"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_tags_delete(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-tags"
        api_path = "/organizations/{organization_name}/tags"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_tags_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-tags"
        api_path = "/organizations/{organization_name}/tags"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_task_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-tasks"
        api_path = "/organizations/{organization_name}/tasks"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_tasks_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-tasks"
        api_path = "/organizations/{organization_name}/tasks"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_team_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/teams"
        api_path = "/organizations/{organization_name}/teams"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_teams_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/teams"
        api_path = "organizations/{organization_name}/teams"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_varset_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "organizations/{organization_name}/varsets"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_varsets_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "organizations/{organization_name}/varsets"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_workspace_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/organizations/{organization_name}/workspaces"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_workspace_delete(self, organization_name, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/organizations/{organization_name}/workspaces/{name}"
        api_path = api_path.format(organization_name=organization_name, name=name)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_workspace_show(self, organization_name, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/organizations/{organization_name}/workspaces/{name}"
        api_path = api_path.format(organization_name=organization_name, name=name)
        return self.call(api_path, **kwargs)

    def organization_workspaces_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/organizations/{organization_name}/workspaces"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organizations_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations"
        return self.call(api_path, **kwargs)

    def plan_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/plans"
        api_path = "/plans/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def policy_delete(self, policy_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policies"
        api_path = "/policies/{policy_id}"
        api_path = api_path.format(policy_id=policy_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def policy_show(self, policy_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policies"
        api_path = "/policies/{policy_id}"
        api_path = api_path.format(policy_id=policy_id)
        return self.call(api_path, **kwargs)

    def policy_upload(self, policy_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policies"
        api_path = "/policies/{policy_id}/upload"
        api_path = api_path.format(policy_id=policy_id)
        return self.call(api_path, method="PUT", data=data, **kwargs)

    def run_actions_apply(self, run_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs/{run_id}/actions/apply"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def run_actions_cancel(self, run_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs/{run_id}/actions/cancel"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def run_actions_discard(self, run_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs/{run_id}/actions/discard"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def run_create(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def run_show(self, run_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs/{run_id}"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, **kwargs)

    def subscription_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/subscriptions"
        api_path = "/subscriptions/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def tag_relationships_workspace_create(self, tag_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-tags"
        api_path = "/tags/{tag_id}/relationships/workspaces"
        api_path = api_path.format(tag_id=tag_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def task_delete(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-tasks"
        api_path = "/tasks/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def task_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-tasks"
        api_path = "/tasks/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def team_delete(self, team_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/teams"
        api_path = "/teams/{team_id}"
        api_path = api_path.format(team_id=team_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def team_relationships_user_create(self, team_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/team-members"
        api_path = "/teams/{team_id}/relationships/users"
        api_path = api_path.format(team_id=team_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def team_relationships_users_delete(self, team_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/team-members"
        api_path = "/teams/{team_id}/relationships/users"
        api_path = api_path.format(team_id=team_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def team_show(self, team_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/teams"
        api_path = "/teams/{team_id}"
        api_path = api_path.format(team_id=team_id)
        return self.call(api_path, **kwargs)

    def user_show(self, user_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/users"
        api_path = "/users/{user_id}"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, **kwargs)

    def var_create(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variables"
        api_path = "/vars"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def var_delete(self, variable_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variables"
        api_path = "/vars/{variable_id}"
        api_path = api_path.format(variable_id=variable_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def vars_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variables"
        api_path = "/vars"
        return self.call(api_path, **kwargs)

    def varset_delete(self, varset_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "varsets/{varset_id}"
        api_path = api_path.format(varset_id=varset_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def varset_relationships_var_create(self, varset_external_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "varsets/{varset_external_id}/relationships/vars"
        api_path = api_path.format(varset_external_id=varset_external_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def varset_relationships_vars_list(self, varset_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "varsets/{varset_id}/relationships/vars"
        api_path = api_path.format(varset_id=varset_id)
        return self.call(api_path, **kwargs)

    def varset_relationships_workspace_create(self, varset_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "varsets/{varset_id}/relationships/workspaces"
        api_path = api_path.format(varset_id=varset_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def varset_relationships_workspaces_delete(self, varset_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "varsets/{varset_id}/relationships/workspaces"
        api_path = api_path.format(varset_id=varset_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def varset_show(self, varset_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "varsets/{varset_id}"
        api_path = api_path.format(varset_id=varset_id)
        return self.call(api_path, **kwargs)

    def workspace_actions_lock(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/actions/lock"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_actions_unlock(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/actions/unlock"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_delete(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def workspace_relationships_remote_state_consumer_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/relationships/remote_state_consumers"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_relationships_remote_state_consumers_delete(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/relationships/remote_state_consumers"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def workspace_relationships_remote_state_consumers_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/relationships/remote_state_consumers"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_relationships_tag_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/relationships/tags"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_relationships_tags_delete(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/relationships/tags"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def workspace_relationships_tags_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/relationships/tags"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_resources_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspace-resources"
        api_path = "/workspaces/{workspace_id}/resources"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_runs_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/workspaces/{workspace_id}/runs"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_show(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_task_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-tasks"
        api_path = "/workspaces/{workspace_id}/tasks"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_task_delete(self, workspace_id, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-tasks"
        api_path = "/workspaces/{workspace_id}/tasks/{id}"
        api_path = api_path.format(workspace_id=workspace_id, id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def workspace_task_show(self, workspace_id, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-tasks"
        api_path = "/workspaces/{workspace_id}/tasks/{id}"
        api_path = api_path.format(workspace_id=workspace_id, id=id)
        return self.call(api_path, **kwargs)

    def workspace_tasks_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-tasks"
        api_path = "/workspaces/{workspace_id}/tasks"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_var_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspace-variables"
        api_path = "/workspaces/{workspace_id}/vars"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_var_delete(self, workspace_id, variable_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspace-variables"
        api_path = "/workspaces/{workspace_id}/vars/{variable_id}"
        api_path = api_path.format(workspace_id=workspace_id, variable_id=variable_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def workspace_vars_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspace-variables"
        api_path = "/workspaces/{workspace_id}/vars"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_varsets_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/variable-sets"
        api_path = "workspaces/{workspace_id}/varsets"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)


