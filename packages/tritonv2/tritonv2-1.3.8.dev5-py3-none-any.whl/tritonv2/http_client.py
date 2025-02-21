# !/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2022 Baidu.com, Inc. All Rights Reserved
"""
triton http client
"""

from tenacity import retry, stop_after_attempt, stop_after_delay, wait_fixed
import tritonclient.http as http_client

from .client import TritonClient
from .exceptions import TritonClientException
from .utils import parse_model
from .constants import LimiterConfig

NUMBER_RETRIES = 3
MAX_INTERVAL_SECS = 20
BASE_INTERVAL_SECS = 0.3


class TritonHTTPClient(TritonClient):
    """
    Concrete implementation of TritonClient
    for HTTP
    """

    def __init__(
        self,
        server_url,
        verbose=False,
        concurrency=1,
        connection_timeout=60.0,
        network_timeout=60.0,
        max_greenlets=None,
        ssl=False,
        ssl_options=None,
        ssl_context_factory=None,
        insecure=False,
        limiter_config: LimiterConfig = None,
    ):
        """
        Parameters
        :param server_url:
        :param verbose:
        :param concurrency:
        :param connection_timeout:
        :param network_timeout:
        :param max_greenlets:
        :param ssl:
        :param ssl_options:
        :param ssl_context_factory:
        :param insecure:
        :param request_rate:
        """
        super().__init__(limiter_config)

        self._client = http_client.InferenceServerClient(
            url=server_url,
            verbose=verbose,
            concurrency=concurrency,
            connection_timeout=connection_timeout,
            network_timeout=network_timeout,
            max_greenlets=max_greenlets,
            ssl=ssl,
            ssl_options=ssl_options,
            ssl_context_factory=ssl_context_factory,
            insecure=insecure,
        )

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def server_ready(self, headers=None, query_params=None):
        """
        check if the server is ready
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.is_server_ready(
                        headers=headers, query_params=query_params
                    )
            return self._client.is_server_ready(
                headers=headers, query_params=query_params
            )
        except Exception as e:
            raise TritonClientException(
                "Failed to check server ready: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def server_live(self, headers=None, query_params=None):
        """
        check if the server live
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.is_server_live(
                        headers=headers, query_params=query_params
                    )
            else:
                return self._client.is_server_live(
                    headers=headers, query_params=query_params
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to check server live: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def server_meta(self, headers=None, query_params=None):
        """
        get server metadata
        Returns
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.get_server_metadata(
                        headers=headers, query_params=query_params
                    )
            else:
                return self._client.get_server_metadata(
                    headers=headers, query_params=query_params
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get server meta: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def model_ready(
        self, model_name, model_version="", headers=None, query_params=None
    ):
        """
        check if model is ready
        :param model_name:
        :param model_version:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.is_model_ready(
                        model_name,
                        model_version,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.is_model_ready(
                    model_name,
                    model_version,
                    headers=headers,
                    query_params=query_params,
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get model ready: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def model_meta(self, model_name, model_version="", headers=None, query_params=None):
        """
        get model meta
        Parameters
        :param model_name:
        :param model_version:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.get_model_metadata(
                        model_name,
                        model_version,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.get_model_metadata(
                    model_name,
                    model_version,
                    headers=headers,
                    query_params=query_params,
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get model meta: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def model_config(
        self, model_name, model_version="", headers=None, query_params=None
    ):
        """
        get model config
        Parameters
        :param model_name:
        :param model_version:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.get_model_config(
                        model_name,
                        model_version,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.get_model_config(
                    model_name,
                    model_version,
                    headers=headers,
                    query_params=query_params,
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get model config: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def model_infer(
        self,
        model_name,
        inputs,
        model_version="",
        outputs=None,
        request_id="",
        sequence_id=0,
        sequence_start=False,
        sequence_end=False,
        priority=0,
        timeout=None,
        headers=None,
        query_params=None,
        request_compression_algorithm=None,
        response_compression_algorithm=None,
    ):
        """
        model infer
        :param model_name:
        :param inputs:
        :param model_version:
        :param outputs:
        :param request_id:
        :param sequence_id:
        :param sequence_start:
        :param sequence_end:
        :param priority:
        :param timeout:
        :param headers:
        :param query_params:
        :param request_compression_algorithm:
        :param response_compression_algorithm:
        :return:
        """

        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.infer(
                        model_name=model_name,
                        inputs=inputs,
                        model_version=model_version,
                        outputs=outputs,
                        request_id=request_id,
                        sequence_id=sequence_id,
                        sequence_start=sequence_start,
                        sequence_end=sequence_end,
                        priority=priority,
                        timeout=timeout,
                        headers=headers,
                        query_params=query_params,
                        request_compression_algorithm=request_compression_algorithm,
                        response_compression_algorithm=response_compression_algorithm,
                    )
            else:
                return self._client.infer(
                    model_name=model_name,
                    inputs=inputs,
                    model_version=model_version,
                    outputs=outputs,
                    request_id=request_id,
                    sequence_id=sequence_id,
                    sequence_start=sequence_start,
                    sequence_end=sequence_end,
                    priority=priority,
                    timeout=timeout,
                    headers=headers,
                    query_params=query_params,
                    request_compression_algorithm=request_compression_algorithm,
                    response_compression_algorithm=response_compression_algorithm,
                )
        except Exception as e:
            raise TritonClientException("Failed to model infer: {}".format(e)) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def model_statistics(
        self, model_name, model_version="", headers=None, query_params=None
    ):
        """
        get model statistics
        :param model_name:
        :param model_version:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.get_inference_statistics(
                        model_name,
                        model_version,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.get_inference_statistics(
                    model_name,
                    model_version,
                    headers=headers,
                    query_params=query_params,
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get model statistics: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def repository_index(self, headers=None, query_params=None):
        """
        get repository index
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.get_model_repository_index(
                        headers=headers, query_params=query_params
                    )
            else:
                return self._client.get_model_repository_index(
                    headers=headers, query_params=query_params
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get repository index: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def repository_model_load(
        self, model_name, headers=None, query_params=None, config="", files=None
    ):
        """
        load model
        :param model_name:
        :param headers:
        :param query_params:
        :param config:
        :param files:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.load_model(
                        model_name=model_name,
                        headers=headers,
                        query_params=query_params,
                        config=config,
                        files=files,
                    )

            else:
                return self._client.load_model(
                    model_name=model_name,
                    headers=headers,
                    query_params=query_params,
                    config=config,
                    files=files,
                )
        except Exception as e:
            raise TritonClientException("Failed to load model: {}".format(e)) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def repository_model_unload(
        self, model_name, headers=None, query_params=None, unload_dependents=False
    ):
        """
        unload model
        :param model_name:
        :param headers:
        :param query_params:
        :param unload_dependents:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.unload_model(
                        model_name=model_name,
                        headers=headers,
                        query_params=query_params,
                        unload_dependents=unload_dependents,
                    )
            else:
                return self._client.unload_model(
                    model_name=model_name,
                    headers=headers,
                    query_params=query_params,
                    unload_dependents=unload_dependents,
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to unload model: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def system_shared_memory_status(
        self, region_name="", headers=None, query_params=None
    ):
        """
        get system shared memory status
        :param region_name:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.get_system_shared_memory_status(
                        region_name=region_name,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.get_system_shared_memory_status(
                    region_name=region_name, headers=headers, query_params=query_params
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get system shared memory status: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def system_shared_memory_register(
        self, name, key, byte_size, offset=0, headers=None, query_params=None
    ):
        """
        register system shared memory
        :param name:
        :param key:
        :param byte_size:
        :param offset:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.register_system_shared_memory(
                        name=name,
                        key=key,
                        byte_size=byte_size,
                        offset=offset,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.register_system_shared_memory(
                    name=name,
                    key=key,
                    byte_size=byte_size,
                    offset=offset,
                    headers=headers,
                    query_params=query_params,
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to register system shared memory: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def system_shared_memory_unregister(self, name, headers=None, query_params=None):
        """
        unregister system shared memory
        :param name:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.unregister_system_shared_memory(
                        name=name, headers=headers, query_params=query_params
                    )
            else:
                return self._client.unregister_system_shared_memory(
                    name=name, headers=headers, query_params=query_params
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to unregister system shared memory: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def cuda_shared_memory_status(
        self, region_name="", headers=None, query_params=None
    ):
        """
        get cuda shared memory status
        :param region_name:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.get_cuda_shared_memory_status(
                        region_name=region_name,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.get_cuda_shared_memory_status(
                    region_name=region_name, headers=headers, query_params=query_params
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get cuda shared memory status: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def cuda_shared_memory_register(
        self, name, raw_handle, byte_size, device_id, headers=None, query_params=None
    ):
        """
        register cuda shared memory
        :param name:
        :param raw_handle:
        :param byte_size:
        :param device_id:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.register_cuda_shared_memory(
                        name=name,
                        raw_handle=raw_handle,
                        device_id=device_id,
                        byte_size=byte_size,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.register_cuda_shared_memory(
                    name=name,
                    raw_handle=raw_handle,
                    device_id=device_id,
                    byte_size=byte_size,
                    headers=headers,
                    query_params=query_params,
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to register cuda shared memory: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def cuda_shared_memory_unregister(self, name, headers=None, query_params=None):
        """
        unregister cuda shared memory
        :param name:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.unregister_cuda_shared_memory(
                        name=name, headers=headers, query_params=query_params
                    )
            else:
                return self._client.unregister_cuda_shared_memory(
                    name=name, headers=headers, query_params=query_params
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to  unregister cuda shared memory: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def trace_setting(
        self, model_name="", settings=None, headers=None, query_params=None
    ):
        """
        update trace setting
        :param model_name:
        :param settings:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if settings is None:
                settings = {}
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.update_trace_settings(
                        model_name=model_name,
                        settings=settings,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.update_trace_settings(
                    model_name=model_name,
                    settings=settings,
                    headers=headers,
                    query_params=query_params,
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to update trace setting: {}".format(e)
            ) from None

    @retry(
        stop=(
            stop_after_attempt(NUMBER_RETRIES + 1) | stop_after_delay(MAX_INTERVAL_SECS)
        ),
        wait=wait_fixed(BASE_INTERVAL_SECS),
        reraise=True,
    )
    def get_trace_settings(self, model_name="", headers=None, query_params=None):
        """
        get_trace_settings
        :param model_name:
        :param headers:
        :param query_params:
        :return:
        """
        try:
            if self._limiter is not None:
                with self._limiter.ratelimit(
                    self._identifier,
                    delay=self._limiter_delay,
                    max_delay=self._limiter_max_delay,
                ):
                    return self._client.get_trace_settings(
                        model_name=model_name,
                        headers=headers,
                        query_params=query_params,
                    )
            else:
                return self._client.get_trace_settings(
                    model_name=model_name, headers=headers, query_params=query_params
                )
        except Exception as e:
            raise TritonClientException(
                "Failed to get trace settings: {}".format(e)
            ) from None

    def get_inputs_and_outputs_detail(self, model_name, model_version=""):
        """
        get inputs and outputs detail
        :param model_name:
        :param model_version:
        :return:
        """
        try:
            model_meta = self.model_meta(model_name, model_version)
            model_config = self.model_config(model_name, model_version)
            return parse_model(model_meta, model_config)
        except Exception as e:
            raise TritonClientException(
                "Failed to get inputs and outputs detail: {}".format(e)
            ) from None
