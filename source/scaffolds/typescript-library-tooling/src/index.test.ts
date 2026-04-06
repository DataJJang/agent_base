import { describe, expect, it } from "vitest";
import { createBootstrapSummary } from "./index";

describe("createBootstrapSummary", () => {
  it("returns the generated repository metadata", () => {
    expect(createBootstrapSummary().repositoryName).toBe("__REPOSITORY_NAME__");
  });
});
