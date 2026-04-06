import { render, screen } from "@testing-library/react";
import { App } from "./App";

describe("App", () => {
  it("shows the generated project name", () => {
    render(<App />);
    expect(screen.getByRole("heading", { name: "__PROJECT_NAME__" })).toBeInTheDocument();
  });
});

