# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..modelgen import SpecifyModel


def test_SpecifyModel_inputs():
    input_map = dict(
        bids_amplitude_column=dict(
            exists=True,
            mandatory=False,
        ),
        bids_condition_column=dict(
            exists=True,
            mandatory=False,
            usedefault=True,
        ),
        bids_event_file=dict(
            mandatory=True,
            xor=['subject_info', 'event_files', 'bids_event_file'],
        ),
        event_files=dict(
            mandatory=True,
            xor=['subject_info', 'event_files', 'bids_event_file'],
        ),
        functional_runs=dict(
            copyfile=False,
            mandatory=True,
        ),
        high_pass_filter_cutoff=dict(mandatory=True, ),
        input_units=dict(mandatory=True, ),
        outlier_files=dict(copyfile=False, ),
        parameter_source=dict(usedefault=True, ),
        realignment_parameters=dict(copyfile=False, ),
        subject_info=dict(
            mandatory=True,
            xor=['subject_info', 'event_files', 'bids_event_file'],
        ),
        time_repetition=dict(mandatory=True, ),
    )
    inputs = SpecifyModel.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_SpecifyModel_outputs():
    output_map = dict(session_info=dict(), )
    outputs = SpecifyModel.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
