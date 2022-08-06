class TFCAPI(object):
    "Class generated from TFC API documentation. See api_gen.py."

    def __init__(self):
        pass

    def call(self, path, query=None, method='GET', data=None,
             files=None, get_all_pages=False, complete_response=False,
             **kwargs):
        pass


    # Duplicate API endpoint that differs:
    #  admin_terraform-version from
    #  https://www.terraform.io/cloud-docs/api-docs/admin/terraform-versions
    # Original definition located here:
    #  admin_terraform-version from
    #  https://www.terraform.io/cloud-docs/api-docs/admin/terraform-versions
    # admin_terraform-version
    #    Path: /admin/terraform-versions/{id}
    #    Method: DELETE
    #    Parameters:
    #        id
    #    Query Parameters:
    # Original definition:
    #    Path: /admin/terraform-versions
    #    Method: POST
    #    Parameters:
    #    Query Parameters:

    # Duplicate API endpoint discarded:
    # authentication-token_show from
    # https://www.terraform.io/cloud-docs/api-docs/user-tokens

    # Duplicate API endpoint discarded:
    # organization_registry-module_create from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # organization_registry-module_delete from
    # https://www.terraform.io/cloud-docs/api-docs/modules

    # Duplicate API endpoint discarded:
    # organization_registry-module_delete from
    # https://www.terraform.io/cloud-docs/api-docs/modules

    # Duplicate API endpoint discarded:
    # organization_registry-module_delete from
    # https://www.terraform.io/cloud-docs/api-docs/modules

    # Duplicate API endpoint discarded:
    # organization_registry-module_delete from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # organization_registry-module_delete from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # organization_registry-module_show from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # organization_registry-module_version_create from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # organization_registry-modules_list from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # organization_registry-modules_vc_create from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # registry-module_create from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # registry-module_version_create from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # registry-modules_actions_delete_create from
    # https://www.terraform.io/cloud-docs/api-docs/modules

    # Duplicate API endpoint discarded:
    # registry-modules_actions_delete_create from
    # https://www.terraform.io/cloud-docs/api-docs/modules

    # Duplicate API endpoint discarded:
    # registry-modules_actions_delete_create from
    # https://www.terraform.io/cloud-docs/api-docs/modules

    # Duplicate API endpoint discarded:
    # registry-modules_actions_delete_create from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # registry-modules_actions_delete_create from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    # Duplicate API endpoint discarded:
    # registry-modules_show from
    # https://www.terraform.io/cloud-docs/api-docs/private-registry/modules

    def account_details_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/account"
        api_path = "/account/details"
        return self.call(api_path, **kwargs)

    def admin_organization(self, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/organizations"
        api_path = "/admin/organizations/{name}"
        api_path = api_path.format(name=name)
        return self.call(api_path, method="DELETE", **kwargs)

    def admin_run_actions_force-cancel(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/runs"
        api_path = "/admin/runs/{id}/actions/force-cancel"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def admin_terraform-version(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/terraform-versions"
        api_path = "/admin/terraform-versions"
        return self.call(api_path, method="POST", data=data, **kwargs)

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

    def agent-pool_agents_list(self, agent_pool_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agents"
        api_path = "/agent-pools/{agent_pool_id}/agents"
        api_path = api_path.format(agent_pool_id=agent_pool_id)
        return self.call(api_path, **kwargs)

    def agent-pool_authentication-token_create(self, agent_pool_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agent-tokens"
        api_path = "/agent-pools/{agent_pool_id}/authentication-tokens"
        api_path = api_path.format(agent_pool_id=agent_pool_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def agent-pool_authentication-tokens_list(self, agent_pool_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agent-tokens"
        api_path = "/agent-pools/{agent_pool_id}/authentication-tokens"
        api_path = api_path.format(agent_pool_id=agent_pool_id)
        return self.call(api_path, **kwargs)

    def agent-pool_delete(self, agent_pool_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agents"
        api_path = "/agent-pools/{agent_pool_id}"
        api_path = api_path.format(agent_pool_id=agent_pool_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def agent-pool_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agents"
        api_path = "/agent-pools/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

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

    def api_registry_v2_gpg-key_create(self, registry_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/gpg-keys"
        api_path = "/api/registry/{registry_name}/v2/gpg-keys"
        api_path = api_path.format(registry_name=registry_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def api_registry_v2_gpg-key_delete(self, registry_name, namespace, key_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/gpg-keys"
        api_path = "/api/registry/{registry_name}/v2/gpg-keys/{namespace}/{key_id}"
        api_path = api_path.format(registry_name=registry_name, namespace=namespace, key_id=key_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def api_registry_v2_gpg-key_show(self, registry_name, namespace, key_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/gpg-keys"
        api_path = "/api/registry/{registry_name}/v2/gpg-keys/{namespace}/{key_id}"
        api_path = api_path.format(registry_name=registry_name, namespace=namespace, key_id=key_id)
        return self.call(api_path, **kwargs)

    def api_v2_admin_cost-estimation-settings(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/settings"
        api_path = "/api/v2/admin/cost-estimation-settings"
        return self.call(api_path, **kwargs)

    def api_v2_admin_customization-settings(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/settings"
        api_path = "/api/v2/admin/customization-settings"
        return self.call(api_path, **kwargs)

    def api_v2_admin_general-settings(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/settings"
        api_path = "/api/v2/admin/general-settings"
        return self.call(api_path, **kwargs)

    def api_v2_admin_organization(self, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/organizations"
        api_path = "/api/v2/admin/organizations/{name}"
        api_path = api_path.format(name=name)
        return self.call(api_path, **kwargs)

    def api_v2_admin_organization_relationships_module-consumers(self, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/organizations"
        api_path = "/api/v2/admin/organizations/{name}/relationships/module-consumers"
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

    def api_v2_admin_saml-settings(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/settings"
        api_path = "/api/v2/admin/saml-settings"
        return self.call(api_path, **kwargs)

    def api_v2_admin_saml-settings_actions_revoke-old-certificate(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/settings"
        api_path = "/api/v2/admin/saml-settings/actions/revoke-old-certificate"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def api_v2_admin_smtp-settings(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/settings"
        api_path = "/api/v2/admin/smtp-settings"
        return self.call(api_path, **kwargs)

    def api_v2_admin_terraform-version(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/terraform-versions"
        api_path = "/api/v2/admin/terraform-versions/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def api_v2_admin_terraform-versions(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/terraform-versions"
        api_path = "/api/v2/admin/terraform-versions"
        return self.call(api_path, **kwargs)

    def api_v2_admin_twilio-settings(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/settings"
        api_path = "/api/v2/admin/twilio-settings"
        return self.call(api_path, **kwargs)

    def api_v2_admin_twilio-settings_verify(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/admin/settings"
        api_path = "/api/v2/admin/twilio-settings/verify"
        return self.call(api_path, method="POST", data=data, **kwargs)

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

    def api_v2_authentication-token_delete(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agent-tokens"
        api_path = "/api/v2/authentication-tokens/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def apply(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/applies"
        api_path = "/applies/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def authentication-token_delete(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/user-tokens"
        api_path = "/authentication-tokens/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def authentication-token_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agent-tokens"
        api_path = "/authentication-tokens/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def comment_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/comments"
        api_path = "/comments/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def configuration-version_actions_archive_create(self, configuration_version_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/configuration-versions"
        api_path = "/configuration-versions/{configuration_version_id}/actions/archive"
        api_path = api_path.format(configuration_version_id=configuration_version_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def configuration-version_download_list(self, configuration_version_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/configuration-versions"
        api_path = "/configuration-versions/{configuration_version_id}/download"
        api_path = api_path.format(configuration_version_id=configuration_version_id)
        return self.call(api_path, **kwargs)

    def configuration-version_ingress-attributes_list(self, configuration-id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/configuration-versions"
        api_path = "/configuration-versions/{configuration-id}/ingress-attributes"
        api_path = api_path.format(configuration-id=configuration-id)
        return self.call(api_path, **kwargs)

    def configuration-version_show(self, configuration-id, include=None, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/configuration-versions"
        api_path = "/configuration-versions/{configuration-id}"
        api_path = api_path.format(configuration-id=configuration-id)
        api_query = {}
        if "query" in kwargs.keys():
            api_query.update(kwargs["query"])
            del kwargs["query"]
        if include:
            api_query.update({
                "include": include,
            })
        return self.call(api_path, query=api_query, **kwargs)

    def cost-estimate_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/cost-estimates"
        api_path = "/cost-estimates/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def feature-sets_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/feature-sets"
        api_path = "/feature-sets"
        return self.call(api_path, **kwargs)

    def meta_ip-ranges_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/ip-ranges"
        api_path = "/meta/ip-ranges"
        return self.call(api_path, **kwargs)

    def notification-configuration_actions_verify_create(self, notification-configuration-id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/notification-configurations"
        api_path = "/notification-configurations/{notification-configuration-id}/actions/verify"
        api_path = api_path.format(notification-configuration-id=notification-configuration-id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def notification-configuration_delete(self, notification-configuration-id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/notification-configurations"
        api_path = "/notification-configurations/{notification-configuration-id}"
        api_path = api_path.format(notification-configuration-id=notification-configuration-id)
        return self.call(api_path, method="DELETE", **kwargs)

    def notification-configuration_show(self, notification-configuration-id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/notification-configurations"
        api_path = "/notification-configurations/{notification-configuration-id}"
        api_path = api_path.format(notification-configuration-id=notification-configuration-id)
        return self.call(api_path, **kwargs)

    def oauth-client_delete(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/oauth-clients"
        api_path = "/oauth-clients/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def oauth-client_oauth-tokens_list(self, oauth_client_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/oauth-tokens"
        api_path = "/oauth-clients/{oauth_client_id}/oauth-tokens"
        api_path = api_path.format(oauth_client_id=oauth_client_id)
        return self.call(api_path, **kwargs)

    def oauth-client_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/oauth-clients"
        api_path = "/oauth-clients/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def oauth-token_delete(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/oauth-tokens"
        api_path = "/oauth-tokens/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def oauth-token_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/oauth-tokens"
        api_path = "/oauth-tokens/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def organization-membership_delete(self, organization_membership_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-memberships"
        api_path = "/organization-memberships/{organization_membership_id}"
        api_path = api_path.format(organization_membership_id=organization_membership_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization-membership_show(self, organization_membership_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-memberships"
        api_path = "/organization-memberships/{organization_membership_id}"
        api_path = api_path.format(organization_membership_id=organization_membership_id)
        return self.call(api_path, **kwargs)

    def organization-memberships_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-memberships"
        api_path = "/organization-memberships"
        return self.call(api_path, **kwargs)

    def organization_agent-pool_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agents"
        api_path = "/organizations/{organization_name}/agent-pools"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_agent-pools_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/agents"
        api_path = "/organizations/{organization_name}/agent-pools"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_audit-trail_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/audit-trails"
        api_path = "/organization/audit-trail"
        return self.call(api_path, **kwargs)

    def organization_authentication-token_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-tokens"
        api_path = "/organizations/{organization_name}/authentication-token"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_authentication-token_delete(self, organization, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-tokens"
        api_path = "/organizations/{organization}/authentication-token"
        api_path = api_path.format(organization=organization)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_create(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_delete(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations/{organization_name}"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_entitlement-set_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations/{organization_name}/entitlement-set"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_feature-sets_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/feature-sets"
        api_path = "/organizations/{organization_name}/feature-sets"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

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

    def organization_oauth-client_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/oauth-clients"
        api_path = "/organizations/{organization_name}/oauth-clients"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_oauth-clients_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/oauth-clients"
        api_path = "/organizations/{organization_name}/oauth-clients"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_organization-membership_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-memberships"
        api_path = "/organizations/{organization_name}/organization-memberships"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_organization-memberships_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organization-memberships"
        api_path = "/organizations/{organization_name}/organization-memberships"
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

    def organization_registry-module_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/organizations/{organization_name}/registry-modules"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_registry-module_delete(self, organization_name, registry_name, namespace, name, provider=None, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/organizations/{organization_name}/registry-modules/{registry_name}/{name}space/{name}"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name)
        if provider:
            api_opt_path = "/organizations/{organization_name}/registry-modules/{registry_name}/{name}space/{name}/{provider}"
            api_path = api_opt_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, provider=provider)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_registry-module_show(self, organization_name, registry_name, namespace, name, provider, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/organizations/{organization_name}/registry-modules/{registry_name}/{name}space/{name}/{provider}"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, provider=provider)
        return self.call(api_path, **kwargs)

    def organization_registry-module_version_create(self, organization_name, registry_name, namespace, name, provider, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/organizations/{organization_name}/registry-modules/{registry_name}/{name}space/{name}/{provider}/versions"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, provider=provider)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_registry-modules_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/organizations/{organization_name}/registry-modules"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_registry-modules_vc_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/organizations/{organization_name}/registry-modules/vcs"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_registry-provider_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/providers"
        api_path = "/organizations/{organization_name}/registry-providers"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_registry-provider_delete(self, organization_name, registry_name, namespace, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/providers"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_registry-provider_show(self, organization_name, registry_name, namespace, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/providers"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name)
        return self.call(api_path, **kwargs)

    def organization_registry-provider_version_create(self, organization_name, registry_name, namespace, name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/provider-versions-platforms"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}/versions"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_registry-provider_version_delete(self, organization_name, registry_name, namespace, name, provider_version, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/provider-versions-platforms"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}/versions/{provider_version}"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, provider_version=provider_version)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_registry-provider_version_platform_create(self, organization_name, registry_name, namespace, name, version, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/provider-versions-platforms"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}/versions/{version}/platforms"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, version=version)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_registry-provider_version_platform_delete(self, organization_name, registry_name, namespace, name, version, os, arch, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/provider-versions-platforms"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}/versions/{version}/platforms/{os}/{arch}"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, version=version, os=os, arch=arch)
        return self.call(api_path, method="DELETE", **kwargs)

    def organization_registry-provider_version_platform_show(self, organization_name, registry_name, namespace, name, version, os, arch, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/provider-versions-platforms"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}/versions/{version}/platforms/{os}/{arch}"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, version=version, os=os, arch=arch)
        return self.call(api_path, **kwargs)

    def organization_registry-provider_version_platforms(self, organization_name, registry_name, namespace, name, version, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/provider-versions-platforms"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}/versions/{version}/platforms"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, version=version)
        return self.call(api_path, **kwargs)

    def organization_registry-provider_version_show(self, organization_name, registry_name, namespace, name, version, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/provider-versions-platforms"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}/versions/{version}"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name, version=version)
        return self.call(api_path, **kwargs)

    def organization_registry-provider_versions_(self, organization_name, registry_name, namespace, name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/provider-versions-platforms"
        api_path = "/organizations/{organization_name}/registry-providers/{registry_name}/{name}space/{name}/versions/"
        api_path = api_path.format(organization_name=organization_name, registry_name=registry_name, namespace=namespace, name=name)
        return self.call(api_path, **kwargs)

    def organization_registry-providers_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/private-registry/providers"
        api_path = "/organizations/{organization_name}/registry-providers"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_relationships_module-producers_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations/{organization_name}/relationships/module-producers"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_show(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/organizations"
        api_path = "/organizations/{organization_name}"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, **kwargs)

    def organization_ssh-key_create(self, organization_name, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/ssh-keys"
        api_path = "/organizations/{organization_name}/ssh-keys"
        api_path = api_path.format(organization_name=organization_name)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def organization_ssh-keys_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/ssh-keys"
        api_path = "/organizations/{organization_name}/ssh-keys"
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

    def organization_vcs-events_list(self, organization_name, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/vcs-events"
        api_path = "/organizations/{organization_name}/vcs-events"
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

    def plan-export_create(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/plan-exports"
        api_path = "/plan-exports"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def plan-export_delete(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/plan-exports"
        api_path = "/plan-exports/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def plan-export_download_list(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/plan-exports"
        api_path = "/plan-exports/{id}/download"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def plan-export_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/plan-exports"
        api_path = "/plan-exports/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def plan_json-output_list(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/plans"
        api_path = "/plans/{id}/json-output"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def plan_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/plans"
        api_path = "/plans/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def policy-check_actions_override_create(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policy-checks"
        api_path = "/policy-checks/{id}/actions/override"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def policy-check_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policy-checks"
        api_path = "/policy-checks/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def policy-set_parameter_create(self, policy_set_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policy-set-params"
        api_path = "/policy-sets/{policy_set_id}/parameters"
        api_path = api_path.format(policy_set_id=policy_set_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def policy-set_parameter_delete(self, policy_set_id, parameter_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policy-set-params"
        api_path = "/policy-sets/{policy_set_id}/parameters/{parameter_id}"
        api_path = api_path.format(policy_set_id=policy_set_id, parameter_id=parameter_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def policy-set_parameters_list(self, policy_set_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policy-set-params"
        api_path = "/policy-sets/{policy_set_id}/parameters"
        api_path = api_path.format(policy_set_id=policy_set_id)
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

    def registry-module_create(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/registry-modules"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def registry-module_version_create(self, organization_name, name, provider, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/registry-modules/{organization_name}/{name}/{provider}/versions"
        api_path = api_path.format(organization_name=organization_name, name=name, provider=provider)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def registry-modules_actions_delete_create(self, organization_name, name, data, provider=None, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/registry-modules/actions/delete/{organization_name}/{name}"
        api_path = api_path.format(organization_name=organization_name, name=name)
        if provider:
            api_opt_path = "/registry-modules/actions/delete/{organization_name}/{name}/{provider}"
            api_path = api_opt_path.format(organization_name=organization_name, name=name, provider=provider)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def registry-modules_show(self, organization_name, name, provider, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/modules"
        api_path = "/registry-modules/show/{organization_name}/{name}/{provider}"
        api_path = api_path.format(organization_name=organization_name, name=name, provider=provider)
        return self.call(api_path, **kwargs)

    def run-trigger_delete(self, run_trigger_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-triggers"
        api_path = "/run-triggers/{run_trigger_id}"
        api_path = api_path.format(run_trigger_id=run_trigger_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def run-trigger_show(self, run_trigger_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-triggers"
        api_path = "/run-triggers/{run_trigger_id}"
        api_path = api_path.format(run_trigger_id=run_trigger_id)
        return self.call(api_path, **kwargs)

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

    def run_actions_force-cancel_create(self, run_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs/{run_id}/actions/force-cancel"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def run_actions_force-execute_create(self, run_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs/{run_id}/actions/force-execute"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def run_comment_create(self, id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/comments"
        api_path = "/runs/{id}/comments"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def run_comments_list(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/comments"
        api_path = "/runs/{id}/comments"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def run_configuration-version_download_list(self, run_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/configuration-versions"
        api_path = "/runs/{run_id}/configuration-version/download"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, **kwargs)

    def run_create(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def run_plan_json-output_list(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/plans"
        api_path = "/runs/{id}/plan/json-output"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def run_policy-checks_list(self, run_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/policy-checks"
        api_path = "/runs/{run_id}/policy-checks"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, **kwargs)

    def run_show(self, run_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run"
        api_path = "/runs/{run_id}"
        api_path = api_path.format(run_id=run_id)
        return self.call(api_path, **kwargs)

    def ssh-key_delete(self, ssh_key_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/ssh-keys"
        api_path = "/ssh-keys/{ssh_key_id}"
        api_path = api_path.format(ssh_key_id=ssh_key_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def ssh-key_show(self, ssh_key_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/ssh-keys"
        api_path = "/ssh-keys/{ssh_key_id}"
        api_path = api_path.format(ssh_key_id=ssh_key_id)
        return self.call(api_path, **kwargs)

    def state-version-output_show(self, state_version_output_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/state-version-outputs"
        api_path = "/state-version-outputs/{state_version_output_id}"
        api_path = api_path.format(state_version_output_id=state_version_output_id)
        return self.call(api_path, **kwargs)

    def state-version_outputs_list(self, state_version_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/state-version-outputs"
        api_path = "/state-versions/{state_version_id}/outputs"
        api_path = api_path.format(state_version_id=state_version_id)
        return self.call(api_path, **kwargs)

    def state-version_show(self, state_version_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/state-versions"
        api_path = "/state-versions/{state_version_id}"
        api_path = api_path.format(state_version_id=state_version_id)
        return self.call(api_path, **kwargs)

    def state-versions_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/state-versions"
        api_path = "/state-versions"
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

    def team-workspace_create(self, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/team-access"
        api_path = "/team-workspaces"
        return self.call(api_path, method="POST", data=data, **kwargs)

    def team-workspace_delete(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/team-access"
        api_path = "/team-workspaces/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, method="DELETE", **kwargs)

    def team-workspace_show(self, id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/team-access"
        api_path = "/team-workspaces/{id}"
        api_path = api_path.format(id=id)
        return self.call(api_path, **kwargs)

    def team-workspaces_list(self, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/team-access"
        api_path = "/team-workspaces"
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

    def user_authentication-token_create(self, user_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/user-tokens"
        api_path = "/users/{user_id}/authentication-tokens"
        api_path = api_path.format(user_id=user_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def user_authentication-tokens_list(self, user_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/user-tokens"
        api_path = "/users/{user_id}/authentication-tokens"
        api_path = api_path.format(user_id=user_id)
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

    def workspace_actions_force-unlock_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}/actions/force-unlock"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

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

    def workspace_configuration-version_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/configuration-versions"
        api_path = "/workspaces/{workspace_id}/configuration-versions"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_configuration-versions_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/configuration-versions"
        api_path = "/workspaces/{workspace_id}/configuration-versions"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_current-state-version_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/state-versions"
        api_path = "/workspaces/{workspace_id}/current-state-version"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

    def workspace_delete(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/workspaces"
        api_path = "/workspaces/{workspace_id}"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="DELETE", **kwargs)

    def workspace_notification-configuration_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/notification-configurations"
        api_path = "/workspaces/{workspace_id}/notification-configurations"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_notification-configurations_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/notification-configurations"
        api_path = "/workspaces/{workspace_id}/notification-configurations"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, **kwargs)

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

    def workspace_run-trigger_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-triggers"
        api_path = "/workspaces/{workspace_id}/run-triggers"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

    def workspace_run-triggers_list(self, workspace_id, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/run-triggers"
        api_path = "/workspaces/{workspace_id}/run-triggers"
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

    def workspace_state-version_create(self, workspace_id, data, **kwargs):
        "https://www.terraform.io/cloud-docs/api-docs/state-versions"
        api_path = "/workspaces/{workspace_id}/state-versions"
        api_path = api_path.format(workspace_id=workspace_id)
        return self.call(api_path, method="POST", data=data, **kwargs)

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


