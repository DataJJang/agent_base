export type BootstrapSummary = {
  repositoryName: string;
  projectName: string;
  projectFamily: string;
};

export function createBootstrapSummary(): BootstrapSummary {
  return {
    repositoryName: "__REPOSITORY_NAME__",
    projectName: "__PROJECT_NAME__",
    projectFamily: "__PROJECT_FAMILY__"
  };
}

