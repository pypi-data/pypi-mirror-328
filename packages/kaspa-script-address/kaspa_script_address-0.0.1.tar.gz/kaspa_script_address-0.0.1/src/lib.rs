pub mod script_address;
use pyo3::prelude::*;
use script_address::to_address;
use script_address::to_script;

#[pymodule]
fn kaspa_script_address(module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(to_address, module)?)?;
    module.add_function(wrap_pyfunction!(to_script, module)?)?;
    Ok(())
}
