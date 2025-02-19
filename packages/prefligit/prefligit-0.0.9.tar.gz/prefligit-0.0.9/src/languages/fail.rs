use std::{collections::HashMap, sync::Arc};

use crate::hook::Hook;
use crate::languages::LanguageImpl;

#[derive(Debug, Copy, Clone)]
pub struct Fail;

impl LanguageImpl for Fail {
    fn supports_dependency(&self) -> bool {
        false
    }

    async fn install(&self, _hook: &Hook) -> anyhow::Result<()> {
        Ok(())
    }

    async fn check_health(&self) -> anyhow::Result<()> {
        Ok(())
    }

    async fn run(
        &self,
        hook: &Hook,
        filenames: &[&String],
        _env_vars: Arc<HashMap<&'static str, String>>,
    ) -> anyhow::Result<(i32, Vec<u8>)> {
        let mut out = hook.entry.as_bytes().to_vec();
        out.extend(b"\n\n");
        for f in filenames {
            out.extend(f.as_bytes());
            out.push(b'\n');
        }
        out.push(b'\n');

        Ok((1, out))
    }
}
