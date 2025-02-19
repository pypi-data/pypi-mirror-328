use serde::Deserialize;

#[derive(Deserialize, Debug)]
pub struct Settings {
    pub database_url: String,
    pub server: String,
    /// Example:
    pub ui_cors_origin: Option<String>,
}
