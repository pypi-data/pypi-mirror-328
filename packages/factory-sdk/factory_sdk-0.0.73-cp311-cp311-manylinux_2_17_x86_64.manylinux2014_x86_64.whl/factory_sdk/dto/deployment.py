from pydantic import BaseModel
from typing import Optional, Union, List, Type, Dict, Any, Mapping, Tuple

class DeploymentArgs(BaseModel):
    """Arguments for vLLM engine."""
    port: Optional[int] = 9000
    #model: str = 'facebook/opt-125m'
    #served_model_name: Optional[Union[str, List[str]]] = None
    tokenizer: Optional[str] = None
    task: str = "generate"
    skip_tokenizer_init: bool = False
    tokenizer_mode: str = 'auto'
    trust_remote_code: bool = False
    allowed_local_media_path: str = ""
    download_dir: Optional[str] = None
    load_format: str = 'auto'
    #config_format: ConfigFormat = ConfigFormat.AUTO
    dtype: str = 'auto'
    kv_cache_dtype: str = 'auto'
    seed: int = 0
    max_model_len: Optional[int] = None
    # Note: Specifying a custom executor backend by passing a class
    # is intended for expert use only. The API may change without
    # notice.
    #distributed_executor_backend: Optional[Union[str,
    #                                             Type[ExecutorBase]]] = None
    # number of P/D disaggregation (or other disaggregation) workers
    pipeline_parallel_size: int = 1
    tensor_parallel_size: int = 1
    max_parallel_loading_workers: Optional[int] = None
    block_size: Optional[int] = None
    enable_prefix_caching: Optional[bool] = None
    disable_sliding_window: bool = False
    use_v2_block_manager: bool = True
    swap_space: float = 4  # GiB
    cpu_offload_gb: float = 0  # GiB
    gpu_memory_utilization: float = 0.90
    max_num_batched_tokens: Optional[int] = None
    max_num_seqs: Optional[int] = None
    max_logprobs: int = 20  # Default value for OpenAI Chat Completions API
    disable_log_stats: bool = False
    revision: Optional[str] = None
    code_revision: Optional[str] = None
    rope_scaling: Optional[Dict[str, Any]] = None
    rope_theta: Optional[float] = None
    #hf_overrides: Optional[HfOverrides] = None
    tokenizer_revision: Optional[str] = None
    quantization: Optional[str] = None
    enforce_eager: Optional[bool] = None
    max_seq_len_to_capture: int = 8192
    disable_custom_all_reduce: bool = False
    tokenizer_pool_size: int = 0
    # Note: Specifying a tokenizer pool by passing a class
    # is intended for expert use only. The API may change without
    # notice.
    #tokenizer_pool_type: Union[str, Type["BaseTokenizerGroup"]] = "ray"
    tokenizer_pool_extra_config: Optional[Dict[str, Any]] = None
    limit_mm_per_prompt: Optional[Mapping[str, int]] = None
    mm_processor_kwargs: Optional[Dict[str, Any]] = None
    disable_mm_preprocessor_cache: bool = False
    #enable_lora: bool = False
    enable_lora_bias: bool = True
    max_loras: int = 1
    max_lora_rank: int = 256
    enable_prompt_adapter: bool = False
    max_prompt_adapters: int = 1
    max_prompt_adapter_token: int = 0
    fully_sharded_loras: bool = False
    lora_extra_vocab_size: int = 256
    long_lora_scaling_factors: Optional[Tuple[float]] = None
    lora_dtype: Optional[str] = 'auto'
    max_cpu_loras: Optional[int] = None
    device: str = 'auto'
    num_scheduler_steps: int = 1
    multi_step_stream_outputs: bool = True
    ray_workers_use_nsight: bool = False
    num_gpu_blocks_override: Optional[int] = None
    num_lookahead_slots: int = 0
    model_loader_extra_config: Optional[dict] = None
    ignore_patterns: Optional[Union[str, List[str]]] = None
    preemption_mode: Optional[str] = None

    scheduler_delay_factor: float = 0.0
    enable_chunked_prefill: Optional[bool] = None

    guided_decoding_backend: str = 'xgrammar'
    logits_processor_pattern: Optional[str] = None
    # Speculative decoding configuration.
    speculative_model: Optional[str] = None
    speculative_model_quantization: Optional[str] = None
    speculative_draft_tensor_parallel_size: Optional[int] = None
    num_speculative_tokens: Optional[int] = None
    speculative_disable_mqa_scorer: Optional[bool] = False
    speculative_max_model_len: Optional[int] = None
    speculative_disable_by_batch_size: Optional[int] = None
    ngram_prompt_lookup_max: Optional[int] = None
    ngram_prompt_lookup_min: Optional[int] = None
    spec_decoding_acceptance_method: str = 'rejection_sampler'
    typical_acceptance_sampler_posterior_threshold: Optional[float] = None
    typical_acceptance_sampler_posterior_alpha: Optional[float] = None
    qlora_adapter_name_or_path: Optional[str] = None
    disable_logprobs_during_spec_decoding: Optional[bool] = None

    otlp_traces_endpoint: Optional[str] = None
    collect_detailed_traces: Optional[str] = None
    disable_async_output_proc: bool = False
    #scheduling_policy: Literal["fcfs", "priority"] = "fcfs"

    #override_neuron_config: Optional[Dict[str, Any]] = None
    #override_pooler_config: Optional[PoolerConfig] = None
    #compilation_config: Optional[CompilationConfig] = None
    worker_cls: str = "auto"

    #kv_transfer_config: Optional[KVTransferConfig] = None

    generation_config: Optional[str] = None
    override_generation_config: Optional[Dict[str, Any]] = None
    enable_sleep_mode: bool = False
    model_impl: str = "auto"

    calculate_kv_scales: Optional[bool] = None