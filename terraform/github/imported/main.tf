terraform {
  required_version = ">= 1.2.0"
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 4.0"
    }
  }
}

variable "github_token" {
  type = string
  sensitive = true
  nullable = false
}

provider "github" {
  token = var.github_token
  owner = "ilya-siluyanov"
}

resource "github_repository" "devops-core-course-labs" {
    name = "devops-core-course-labs"
    allow_merge_commit = false
}

data "github_user" "self" {
  username = "ilya-siluyanov"
}

resource "github_team" "devs" {
    name = "Developers"
    create_default_maintainer = true
}

resource "github_team" "ops" {
    name = "Operation managers"
    create_default_maintainer = true
}

resource "github_team_repository" "devops-core-course-labs-devs" {
    repository = github_repository.devops-core-course-labs.name
    team_id = github_team.devs.id
    permission = "push"
}

resource "github_team_repository" "devops-core-course-labs-ops" {
    repository = github_repository.devops-core-course-labs.name
    team_id = github_team.ops.id
    permission = "pull"
}

resource "github_team_membership" "devs-ilya" {
    team_id = github_team.devs.id
    username = data.github_user.self.username
    role = "maintainer"
}

resource "github_team_membership" "ops-ilya" {
    team_id = github_team.ops.id
    username = data.github_user.self.username
    role = "member"
}

output "url" {
  value = github_repository.devops-core-course-labs.html_url
}