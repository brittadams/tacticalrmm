<template>
  <div class="q-pa-xs q-ma-xs">
    <q-bar>
      <q-btn-group flat>
        <q-btn size="md" dense no-caps flat label="File">
          <q-menu>
            <q-list dense style="min-width: 100px">
              <q-item clickable>
                <q-item-section>Add</q-item-section>
                <q-item-section side>
                  <q-icon name="keyboard_arrow_right" />
                </q-item-section>
                <q-menu anchor="top right" self="top left">
                  <q-list dense style="min-width: 100px">
                    <q-item clickable v-close-popup @click="showAddClientModal = true">
                      <q-item-section>Add Client</q-item-section>
                    </q-item>
                    <q-item clickable v-close-popup @click="showAddSiteModal = true">
                      <q-item-section>Add Site</q-item-section>
                    </q-item>
                  </q-list>
                </q-menu>
              </q-item>

              <q-item clickable>
                <q-item-section>Delete</q-item-section>
                <q-item-section side>
                  <q-icon name="keyboard_arrow_right" />
                </q-item-section>
                <q-menu anchor="top right" self="top left">
                  <q-list dense style="min-width: 100px">
                    <q-item clickable v-close-popup @click="showDeleteClientModal = true">
                      <q-item-section>Delete Client</q-item-section>
                    </q-item>
                    <q-item clickable v-close-popup @click="showDeleteSiteModal = true">
                      <q-item-section>Delete Site</q-item-section>
                    </q-item>
                  </q-list>
                </q-menu>
              </q-item>

              <q-item clickable v-close-popup @click="showUploadMesh = true">
                <q-item-section>Upload MeshAgent</q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="showAuditManager = true">
                <q-item-section>Audit Log</q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="getLog">
                <q-item-section>Debug Log</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>
        <!-- edit -->
        <q-btn size="md" dense no-caps flat label="Edit">
          <q-menu>
            <q-list dense style="min-width: 100px">
              <q-item clickable v-close-popup @click="showEditClientsModal = true">
                <q-item-section>Edit Clients</q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="showEditSitesModal = true">
                <q-item-section>Edit Sites</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>
        <!-- view -->
        <q-btn size="md" dense no-caps flat label="View">
          <q-menu auto-close>
            <q-list dense style="min-width: 100px">
              <q-item clickable v-close-popup @click="showPendingActions">
                <q-item-section>Pending Actions</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>
        <!-- agents -->
        <q-btn size="md" dense no-caps flat label="Agents">
          <q-menu auto-close>
            <q-list dense style="min-width: 100px">
              <q-item clickable v-close-popup @click="showInstallAgent = true">
                <q-item-section>Install Agent</q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="showDeployment = true">
                <q-item-section>Manage Deployments</q-item-section>
              </q-item>
              <q-item clickable v-close-popup @click="showUpdateAgentsModal = true">
                <q-item-section>Update Agents</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>

        <!-- settings -->
        <q-btn size="md" dense no-caps flat label="Settings">
          <q-menu auto-close>
            <q-list dense style="min-width: 100px">
              <!-- script manager -->
              <q-item clickable v-close-popup @click="showScriptManager">
                <q-item-section>Script Manager</q-item-section>
              </q-item>
              <!-- automation manager -->
              <q-item clickable v-close-popup @click="showAutomationManager = true">
                <q-item-section>Automation Manager</q-item-section>
              </q-item>
              <!-- admin manager -->
              <q-item clickable v-close-popup @click="showAdminManager = true">
                <q-item-section>User Administration</q-item-section>
              </q-item>
              <!-- core settings -->
              <q-item clickable v-close-popup @click="showEditCoreSettingsModal = true">
                <q-item-section>Global Settings</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>
        <!-- tools -->
        <q-btn size="md" dense no-caps flat label="Tools">
          <q-menu auto-close>
            <q-list dense style="min-width: 100px">
              <!-- bulk command -->
              <q-item clickable v-close-popup @click="showBulkCommand = true">
                <q-item-section>Bulk Command</q-item-section>
              </q-item>
              <!-- bulk script -->
              <q-item clickable v-close-popup @click="showBulkScript = true">
                <q-item-section>Bulk Script</q-item-section>
              </q-item>
              <!-- bulk patch management -->
              <q-item clickable v-close-popup @click="showBulkPatchManagement = true">
                <q-item-section>Bulk Patch Management</q-item-section>
              </q-item>
            </q-list>
          </q-menu>
        </q-btn>
      </q-btn-group>
      <q-space />
      <!-- add client modal -->
      <q-dialog v-model="showAddClientModal">
        <AddClient @close="showAddClientModal = false" />
      </q-dialog>
      <q-dialog v-model="showEditClientsModal">
        <EditClients @close="showEditClientsModal = false" @edited="edited" />
      </q-dialog>
      <!-- add site modal -->
      <q-dialog v-model="showAddSiteModal">
        <AddSite @close="showAddSiteModal = false" :clients="clients" />
      </q-dialog>
      <q-dialog v-model="showEditSitesModal">
        <EditSites @close="showEditSitesModal = false" @edited="edited" />
      </q-dialog>
      <!-- delete -->
      <q-dialog v-model="showDeleteClientModal">
        <DeleteClient @close="showDeleteClientModal = false" @edited="edited" />
      </q-dialog>
      <q-dialog v-model="showDeleteSiteModal">
        <DeleteSite @close="showDeleteSiteModal = false" @edited="edited" />
      </q-dialog>
      <!-- edit core settings modal -->
      <q-dialog v-model="showEditCoreSettingsModal">
        <EditCoreSettings @close="showEditCoreSettingsModal = false" />
      </q-dialog>
      <!-- debug log modal -->
      <LogModal />
      <!-- audit log modal -->
      <div class="q-pa-md q-gutter-sm">
        <q-dialog v-model="showAuditManager" maximized transition-show="slide-up" transition-hide="slide-down">
          <AuditManager @close="showAuditManager = false" />
        </q-dialog>
      </div>
      <!-- Install Agents -->
      <div class="q-pa-md q-gutter-sm">
        <q-dialog v-model="showInstallAgent">
          <InstallAgent @close="showInstallAgent = false" />
        </q-dialog>
      </div>
      <!-- Update Agents Modal -->
      <div class="q-pa-md q-gutter-sm">
        <q-dialog v-model="showUpdateAgentsModal" maximized transition-show="slide-up" transition-hide="slide-down">
          <UpdateAgents @close="showUpdateAgentsModal = false" />
        </q-dialog>
      </div>
      <!-- Script Manager -->
      <ScriptManager />

      <!-- Automation Manager -->
      <div class="q-pa-md q-gutter-sm">
        <q-dialog v-model="showAutomationManager">
          <AutomationManager @close="showAutomationManager = false" />
        </q-dialog>
      </div>
      <!-- Admin Manager -->
      <div class="q-pa-md q-gutter-sm">
        <q-dialog v-model="showAdminManager">
          <AdminManager @close="showAdminManager = false" />
        </q-dialog>
      </div>
      <!-- Upload new mesh agent -->
      <q-dialog v-model="showUploadMesh">
        <UploadMesh @close="showUploadMesh = false" />
      </q-dialog>

      <!-- Bulk command modal -->
      <q-dialog v-model="showBulkCommand" position="top">
        <BulkCommand @close="showBulkCommand = false" />
      </q-dialog>

      <!-- Bulk script modal -->
      <q-dialog v-model="showBulkScript" position="top">
        <BulkScript @close="showBulkScript = false" />
      </q-dialog>

      <!-- Bulk patch management -->
      <q-dialog v-model="showBulkPatchManagement" position="top">
        <BulkPatchManagement @close="showBulkPatchManagement = false" />
      </q-dialog>

      <!-- Agent Deployment -->
      <q-dialog v-model="showDeployment">
        <Deployment @close="showDeployment = false" />
      </q-dialog>
    </q-bar>
  </div>
</template>

<script>
import LogModal from "@/components/modals/logs/LogModal";
import AddClient from "@/components/modals/clients/AddClient";
import EditClients from "@/components/modals/clients/EditClients";
import AddSite from "@/components/modals/clients/AddSite";
import EditSites from "@/components/modals/clients/EditSites";
import DeleteClient from "@/components/modals/clients/DeleteClient";
import DeleteSite from "@/components/modals/clients/DeleteSite";
import UpdateAgents from "@/components/modals/agents/UpdateAgents";
import ScriptManager from "@/components/ScriptManager";
import EditCoreSettings from "@/components/modals/coresettings/EditCoreSettings";
import AutomationManager from "@/components/automation/AutomationManager";
import AdminManager from "@/components/AdminManager";
import InstallAgent from "@/components/modals/agents/InstallAgent";
import UploadMesh from "@/components/modals/core/UploadMesh";
import AuditManager from "@/components/AuditManager";
import BulkCommand from "@/components/modals/agents/BulkCommand";
import BulkScript from "@/components/modals/agents/BulkScript";
import BulkPatchManagement from "@/components/modals/agents/BulkPatchManagement";
import Deployment from "@/components/Deployment";

export default {
  name: "FileBar",
  components: {
    LogModal,
    AddClient,
    EditClients,
    AddSite,
    EditSites,
    DeleteClient,
    DeleteSite,
    UpdateAgents,
    ScriptManager,
    EditCoreSettings,
    AutomationManager,
    InstallAgent,
    UploadMesh,
    AdminManager,
    AuditManager,
    BulkCommand,
    BulkScript,
    BulkPatchManagement,
    Deployment,
  },
  props: ["clients"],
  data() {
    return {
      showAddClientModal: false,
      showEditClientsModal: false,
      showAddSiteModal: false,
      showEditSitesModal: false,
      showDeleteClientModal: false,
      showDeleteSiteModal: false,
      showUpdateAgentsModal: false,
      showEditCoreSettingsModal: false,
      showAutomationManager: false,
      showAdminManager: false,
      showInstallAgent: false,
      showUploadMesh: false,
      showAuditManager: false,
      showBulkCommand: false,
      showBulkScript: false,
      showBulkPatchManagement: false,
      showDeployment: false,
    };
  },
  methods: {
    getLog() {
      this.$store.commit("logs/TOGGLE_LOG_MODAL", true);
    },
    showPendingActions() {
      const data = { action: true, agentpk: null, hostname: null };
      this.$store.commit("logs/TOGGLE_PENDING_ACTIONS", data);
    },
    showScriptManager() {
      this.$store.commit("TOGGLE_SCRIPT_MANAGER", true);
    },
    edited() {
      this.$emit("edited");
    },
  },
};
</script>
